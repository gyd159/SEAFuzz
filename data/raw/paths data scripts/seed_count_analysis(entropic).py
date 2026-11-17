"""Analyze seed counts across independent fuzzing runs."""

from pathlib import Path
import re

import numpy as np
import pandas as pd


# Configuration: directory containing out1/, out2/, etc.
INPUT_ROOT = Path("path/to/experiment/runs")
SEED_COUNT_FILE = "seed_count.csv"
START_MINUTE = 0
END_MINUTE = 1440
TARGET_24H_SECONDS = 24 * 60 * 60
DECIMAL_PLACES = 3


def natural_sort_key(path):
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", path.name)
    ]


def find_seed_count(run_folder):
    direct = run_folder / SEED_COUNT_FILE
    if direct.is_file():
        return direct
    return next(
        (p for p in sorted(run_folder.rglob(SEED_COUNT_FILE)) if p.is_file()),
        None,
    )


def read_seed_count(file):
    df = pd.read_csv(file)

    # Prefer named columns; fall back to the second and fifth columns.
    if "elapsed_seconds" in df.columns:
        time_col = df["elapsed_seconds"]
    elif df.shape[1] >= 2:
        time_col = df.iloc[:, 1]
    else:
        raise ValueError("Missing elapsed_seconds and the second column")

    if "total_seeds" in df.columns:
        value_col = df["total_seeds"]
    elif df.shape[1] >= 5:
        value_col = df.iloc[:, 4]
    else:
        raise ValueError("Missing total_seeds and the fifth column")

    data = pd.DataFrame({
        "elapsed_seconds": pd.to_numeric(time_col, errors="coerce"),
        "total_seeds": pd.to_numeric(value_col, errors="coerce"),
    }).dropna()

    data = data.loc[data["elapsed_seconds"] >= 0]
    data = (data.sort_values("elapsed_seconds", kind="stable")
            .drop_duplicates("elapsed_seconds", keep="last"))

    if data.empty:
        raise ValueError("No valid seed count records")
    return data


def interpolate_to_minutes(df, minutes):
    times = df["elapsed_seconds"].to_numpy(dtype=float)
    values = df["total_seeds"].to_numpy(dtype=float)
    target_seconds = minutes.astype(float) * 60

    # Interpolate only within the observed time range (no extrapolation).
    if len(times) == 1:
        sampled = np.full(len(minutes), np.nan)
        sampled[np.isclose(target_seconds, times[0])] = values[0]
        return sampled

    sampled = np.interp(target_seconds, times, values)
    sampled[(target_seconds < times[0]) | (target_seconds > times[-1])] = np.nan
    return sampled


def get_24h_final_record(df):
    # Use the first observed record at or after 24 hours, never interpolation.
    matches = df.loc[df["elapsed_seconds"] >= TARGET_24H_SECONDS]
    if matches.empty:
        return None

    row = matches.iloc[0]
    seconds = float(row["elapsed_seconds"])
    return {
        "actual_time_sec": seconds,
        "actual_time_min": seconds / 60,
        "difference_from_24h_sec": seconds - TARGET_24H_SECONDS,
        "total_seeds": float(row["total_seeds"]),
    }


def main():
    if not INPUT_ROOT.is_dir():
        raise NotADirectoryError(f"Directory not found: {INPUT_ROOT}")

    run_folders = sorted(
        (p for p in INPUT_ROOT.iterdir() if p.is_dir()),
        key=natural_sort_key,
    )
    if not run_folders:
        raise RuntimeError("No run folders found")

    minutes = np.arange(START_MINUTE, END_MINUTE + 1)
    all_runs = {"time_min": minutes}
    final_rows = []

    for run_folder in run_folders:
        seed_file = find_seed_count(run_folder)
        if seed_file is None:
            print(f"Skipping {run_folder.name}: {SEED_COUNT_FILE} not found")
            continue

        try:
            data = read_seed_count(seed_file)
        except (OSError, ValueError, pd.errors.ParserError) as exc:
            print(f"Skipping {run_folder.name}: {exc}")
            continue

        all_runs[run_folder.name] = interpolate_to_minutes(data, minutes)
        final = get_24h_final_record(data)
        if final is None:
            print(f"{run_folder.name}: no record at or after 24 hours")
        else:
            final_rows.append({"out": run_folder.name, **final})
        print(f"Processed: {run_folder.name}")

    if len(all_runs) == 1:
        raise RuntimeError("No valid seed_count.csv files found")

    # Calculate means at full precision and round only when saving.
    all_result = pd.DataFrame(all_runs)
    mean_result = pd.DataFrame({
        "time_min": minutes,
        "mean_total_seeds": all_result.drop(columns="time_min").mean(axis=1),
    })

    final_columns = [
        "out", "actual_time_sec", "actual_time_min",
        "difference_from_24h_sec", "total_seeds",
    ]
    final_result = pd.DataFrame(final_rows, columns=final_columns)
    if not final_result.empty:
        final_result.loc[len(final_result)] = {
            "out": "mean",
            "total_seeds": final_result["total_seeds"].mean(),
        }
    else:
        print("Warning: no runs have a valid 24-hour final record")

    for filename, result in (
        ("all.csv", all_result),
        ("mean.csv", mean_result),
        ("final.csv", final_result),
    ):
        output = INPUT_ROOT / filename
        result.round(DECIMAL_PLACES).to_csv(
            output, index=False, encoding="utf-8-sig",
            float_format=f"%.{DECIMAL_PLACES}f",
        )
        print(f"Saved: {output}")

    print("Seed count analysis completed.")


if __name__ == "__main__":
    main()
