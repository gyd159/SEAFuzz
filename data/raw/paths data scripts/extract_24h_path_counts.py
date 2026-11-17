"""Extract one 24-hour path count from each fuzzer run for boxplot analysis."""

from pathlib import Path
import re

import numpy as np
import pandas as pd


# Configuration
ROOT_DIR = Path("path/to/experiment/results")
FUZZER_ORDER = (
    "SEAFuzz", "AFL", "AFLFast", "EcoFuzz",
    "DiPri", "AFL-DiPri", "Entropic",
)
PLOT_DATA_NAMES = ("plot_data", "plot_data.csv", "plot_data.txt", "plot_data.dat")
RUN_COUNT = 10
TARGET_SECONDS = 24 * 3600
TIME_ZERO_MODE = "first_row"  # "first_row" or "absolute"
SAMPLE_METHOD = "previous"    # "previous", "nearest", or "linear"
FILL_AFTER_LAST = True


def read_plot_data(path):
    with path.open("r", encoding="utf-8-sig", errors="ignore") as stream:
        first = stream.readline().strip()
    parts = first.split(",") if "," in first else first.split()
    if len(parts) < 4:
        raise ValueError(f"Expected at least four columns: {path}")
    try:
        float(parts[0])
        float(parts[3])
        header = None
    except ValueError:
        header = 0

    separator = "," if "," in first else r"\s+"
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


def sample_24h_value(path):
    times, values = read_plot_data(path)
    if TIME_ZERO_MODE == "first_row":
        times -= times[0]
    elif TIME_ZERO_MODE != "absolute":
        raise ValueError(f"Invalid TIME_ZERO_MODE: {TIME_ZERO_MODE}")

    target = TARGET_SECONDS
    if target < times[0] or (not FILL_AFTER_LAST and target > times[-1]):
        return np.nan

    if SAMPLE_METHOD == "previous":
        position = np.searchsorted(times, target, side="right") - 1
        return float(values[position]) if position >= 0 else np.nan
    if SAMPLE_METHOD == "nearest":
        return float(values[np.abs(times - target).argmin()])
    if SAMPLE_METHOD == "linear":
        return float(np.interp(target, times, values))
    raise ValueError(f"Invalid SAMPLE_METHOD: {SAMPLE_METHOD}")


def get_run_folders(fuzzer_dir):
    folders = [p for p in fuzzer_dir.iterdir()
               if p.is_dir() and re.fullmatch(r"out\d+", p.name, flags=re.I)]
    return sorted(folders, key=lambda p: (int(p.name[3:]), p.name.casefold()))[:RUN_COUNT]


def find_plot_data(run_dir):
    for filename in PLOT_DATA_NAMES:
        candidate = run_dir / filename
        if candidate.is_file():
            return candidate
    return None


def process_program(program_dir):
    folders = {p.name.casefold(): p for p in program_dir.iterdir() if p.is_dir()}
    rows = []

    for fuzzer in FUZZER_ORDER:
        folder = folders.get(fuzzer.casefold())
        runs = get_run_folders(folder) if folder else []
        if folder is None:
            print(f"  Missing fuzzer: {fuzzer}")
        if len(runs) != RUN_COUNT:
            print(f"  {fuzzer}: found {len(runs)}/{RUN_COUNT} run folders")

        for run_dir in runs:
            path = find_plot_data(run_dir)
            value = np.nan
            if path is not None:
                try:
                    value = sample_24h_value(path)
                except (OSError, ValueError, pd.errors.ParserError) as exc:
                    print(f"  Could not read {path}: {exc}")
            else:
                print(f"  Missing plot_data: {run_dir}")
            rows.append({"name": fuzzer, "value": value})

        # Keep exactly RUN_COUNT rows per fuzzer, including missing runs.
        rows.extend({"name": fuzzer, "value": np.nan}
                    for _ in range(RUN_COUNT - len(runs)))

    output = program_dir / f"{program_dir.name}1.csv"
    pd.DataFrame(rows, columns=["name", "value"]).to_csv(
        output, index=False, encoding="utf-8-sig"
    )
    print(f"  Saved: {output}")


def main():
    if not ROOT_DIR.is_dir():
        raise NotADirectoryError(f"Directory not found: {ROOT_DIR}")
    for program_dir in sorted(p for p in ROOT_DIR.iterdir() if p.is_dir()):
        child_names = {p.name.casefold() for p in program_dir.iterdir() if p.is_dir()}
        if not any(fuzzer.casefold() in child_names for fuzzer in FUZZER_ORDER):
            continue
        print(f"Processing program: {program_dir.name}")
        process_program(program_dir)
    print("24-hour path extraction completed.")


if __name__ == "__main__":
    main()
