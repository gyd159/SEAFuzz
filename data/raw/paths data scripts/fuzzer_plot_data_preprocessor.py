from pathlib import Path
import re
import numpy as np
import pandas as pd


# Configuration
BASE_ROOT = Path("path/to/experiment/results")
OUTPUT_FOLDER = "xinjia"
START_MINUTE = 0
END_MINUTE = 1440


def natural_sort_key(path):
    return [
        int(x) if x.isdigit() else x.lower()
        for x in re.split(r"(\d+)", path.name)
    ]


def get_sorted_dirs(folder):
    return sorted(
        [p for p in folder.iterdir() if p.is_dir()],
        key=natural_sort_key
    )


def find_plot_data(folder):
    for name in ["plot_data", "plot_data.csv", "plot_data.txt", "plot_data.dat"]:
        path = folder / name
        if path.is_file():
            return path
    return None


def read_plot_data(file):
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        sep = "," if "," in f.readline() else r"\s+"

    df = pd.read_csv(file, sep=sep, header=None)

    result = pd.DataFrame({
        "time": pd.to_numeric(df.iloc[:, 0], errors="coerce"),
        "value": pd.to_numeric(df.iloc[:, 3], errors="coerce")
    })

    return result.dropna()


def sample_plot(file, minutes):
    df = read_plot_data(file)

    if df.empty:
        return None

    # Normalize timestamps and sample at one-minute intervals
    t = df["time"].to_numpy()
    v = df["value"].to_numpy()
    t = t - t[0]

    result = []
    for minute in minutes:
        indices = np.where(t <= minute * 60)[0]
        result.append(v[indices[-1]] if len(indices) else np.nan)

    return result


def process_fuzzer(fuzzer_folder, output_dir):
    print(f"Processing fuzzer: {fuzzer_folder.name}")

    minutes = np.arange(START_MINUTE, END_MINUTE + 1)
    runs = []

    for output_folder in get_sorted_dirs(fuzzer_folder):
        plot = find_plot_data(output_folder)
        if plot is None:
            continue

        data = sample_plot(plot, minutes)
        if data is not None:
            runs.append(data)

    if not runs:
        print("  No valid plot_data found.")
        return

    # Each row represents one run; each column represents one minute
    df = pd.DataFrame(runs, columns=minutes)

    output_file = output_dir / f"{fuzzer_folder.name}.csv"
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print(f"  Saved: {output_file}")


def process_program(program_folder):
    print(f"\nProcessing program: {program_folder.name}")

    output_dir = program_folder / OUTPUT_FOLDER
    output_dir.mkdir(exist_ok=True)

    for fuzzer in get_sorted_dirs(program_folder):
        if fuzzer.name != OUTPUT_FOLDER:
            process_fuzzer(fuzzer, output_dir)


def main():
    for program in get_sorted_dirs(BASE_ROOT):
        process_program(program)

    print("\nProcessing completed.")


if __name__ == "__main__":
    main()