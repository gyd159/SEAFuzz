"""Aggregate fuzzer path discovery data into one-minute mean time series."""

from pathlib import Path
import re

import numpy as np
import pandas as pd


# Configuration
BASE_ROOT = Path("path/to/experiment/results")
FUZZER_ORDER = (
    "SEAFuzz", "AFL", "AFLFast", "EcoFuzz",
    "DiPri", "AFL-DiPri", "Entropic",
)
PLOT_DATA_NAMES = ("plot_data", "plot_data.csv", "plot_data.txt", "plot_data.dat")
START_MINUTE = 0
END_MINUTE = 1440
MAX_RUNS = 10
TIME_ZERO_MODE = "first_row"  # "first_row" or "absolute"
SAMPLE_METHOD = "previous"    # "previous", "nearest", or "linear"
FILL_AFTER_LAST = True


def natural_key(path):
    return [int(x) if x.isdigit() else x.casefold()
            for x in re.split(r"(\d+)", path.name)]


def sorted_dirs(folder):
    return sorted((p for p in folder.iterdir() if p.is_dir()), key=natural_key)


def find_plot_data(run_dir):
    for name in PLOT_DATA_NAMES:
        candidate = run_dir / name
        if candidate.is_file():
            return candidate
    for name in PLOT_DATA_NAMES:
        matches = sorted(p for p in run_dir.rglob(name) if p.is_file())
        if matches:
            return matches[0]
    return None


def read_plot_data(path):
    with path.open("r", encoding="utf-8-sig", errors="ignore") as stream:
        first = stream.readline().strip()
    parts = first.split(",") if "," in first else first.split()
    if len(parts) < 4:
        raise ValueError(f"Expected at least four columns: {path}")

    separator = "," if "," in first else r"\s+"
    try:
        float(parts[0])
        float(parts[3])
        header = None
    except ValueError:
        header = 0

    df = pd.read_csv(path, sep=separator, header=header, encoding="utf-8-sig")
    if df.shape[1] < 4:
        raise ValueError(f"Expected at least four columns: {path}")

    data = pd.DataFrame({
        "time": pd.to_numeric(df.iloc[:, 0], errors="coerce"),
        "value": pd.to_numeric(df.iloc[:, 3], errors="coerce"),
    }).dropna()
    data = data.sort_values("time", kind="stable").drop_duplicates("time", keep="last")
    if data.empty:
        raise ValueError(f"No valid data: {path}")
    return data["time"].to_numpy(float), data["value"].to_numpy(float)


def sample_plot(path, target_seconds):
    times, values = read_plot_data(path)
    if TIME_ZERO_MODE == "first_row":
        times -= times[0]
    elif TIME_ZERO_MODE != "absolute":
        raise ValueError(f"Invalid TIME_ZERO_MODE: {TIME_ZERO_MODE}")

    sampled = np.full(len(target_seconds), np.nan)
    if SAMPLE_METHOD == "previous":
        positions = np.searchsorted(times, target_seconds, side="right") - 1
        valid = positions >= 0
        if not FILL_AFTER_LAST:
            valid &= target_seconds <= times[-1]
        sampled[valid] = values[positions[valid]]
    elif SAMPLE_METHOD == "nearest":
        for i, second in enumerate(target_seconds):
            if not FILL_AFTER_LAST and second > times[-1]:
                continue
            sampled[i] = values[np.abs(times - second).argmin()]
    elif SAMPLE_METHOD == "linear":
        sampled = np.interp(target_seconds, times, values)
        sampled[target_seconds < times[0]] = np.nan
        if not FILL_AFTER_LAST:
            sampled[target_seconds > times[-1]] = np.nan
    else:
        raise ValueError(f"Invalid SAMPLE_METHOD: {SAMPLE_METHOD}")
    return sampled


def mean_over_runs(fuzzer_dir, target_seconds):
    runs = []
    for run_dir in sorted_dirs(fuzzer_dir)[:MAX_RUNS]:
        plot_file = find_plot_data(run_dir)
        if plot_file is None:
            print(f"  Missing plot_data: {run_dir}")
            continue
        try:
            runs.append(sample_plot(plot_file, target_seconds))
        except (OSError, ValueError, pd.errors.ParserError) as exc:
            print(f"  Could not read {plot_file}: {exc}")
    if not runs:
        return None

    # Average available runs at each minute.
    return pd.DataFrame(np.column_stack(runs)).mean(axis=1).to_numpy()


def process_program(program_dir, minutes):
    result = pd.DataFrame({"time": minutes})
    folders = {p.name.casefold(): p for p in sorted_dirs(program_dir)}
    seconds = minutes.astype(float) * 60

    for fuzzer in FUZZER_ORDER:
        folder = folders.get(fuzzer.casefold())
        if folder is None:
            print(f"  Missing fuzzer: {fuzzer}")
            result[fuzzer] = np.nan
            continue
        values = mean_over_runs(folder, seconds)
        result[fuzzer] = values if values is not None else np.nan
        if values is None:
            print(f"  No valid runs: {fuzzer}")
        else:
            print(f"  Processed: {fuzzer}")

    if result.drop(columns="time").notna().sum().sum() == 0:
        print(f"  Skipping {program_dir.name}: no valid data")
        return

    output = program_dir / f"{program_dir.name}.csv"
    result.to_csv(output, index=False, encoding="utf-8-sig")
    print(f"  Saved: {output}")


def main():
    if not BASE_ROOT.is_dir():
        raise NotADirectoryError(f"Directory not found: {BASE_ROOT}")
    minutes = np.arange(START_MINUTE, END_MINUTE + 1)
    for program_dir in sorted_dirs(BASE_ROOT):
        print(f"Processing program: {program_dir.name}")
        process_program(program_dir, minutes)
    print("Time-series processing completed.")


if __name__ == "__main__":
    main()
