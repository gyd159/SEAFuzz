from pathlib import Path
import pandas as pd


# Configuration
ROOT_DIR = Path("path/to/results")


def main():
    if not ROOT_DIR.is_dir():
        raise NotADirectoryError(f"Directory not found: {ROOT_DIR}")

    for sub_dir in sorted(ROOT_DIR.iterdir()):
        if not sub_dir.is_dir():
            continue

        folder_name = sub_dir.name
        input_csv = sub_dir / f"{folder_name}1.csv"

        if not input_csv.is_file():
            print(f"Skipping: {input_csv} not found")
            continue

        try:
            df = pd.read_csv(input_csv, encoding="utf-8-sig")
        except UnicodeDecodeError:
            df = pd.read_csv(input_csv, encoding="gbk")

        df.columns = df.columns.astype(str).str.strip().str.lower()

        if not {"name", "value"}.issubset(df.columns):
            print(f"Skipping: Missing columns in {input_csv}")
            continue

        # Normalize fuzzer names and values
        df["name"] = df["name"].astype("string").str.strip().str.lower()
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        df = df.dropna(subset=["name", "value"])

        if df.empty:
            print(f"Skipping: No valid data in {folder_name}")
            continue

        # Calculate sample standard deviation (ddof=1)
        result = (
            df.groupby("name", sort=False)["value"]
            .std(ddof=1)
            .reset_index(name="sd")
        )

        result["sd"] = result["sd"].round(2)

        output_csv = sub_dir / f"{folder_name}_sd.csv"
        result.to_csv(output_csv, index=False, encoding="utf-8-sig")

        print(f"Saved: {output_csv} ({len(result)} fuzzers)")

    print("\nStandard deviation calculation completed.")


if __name__ == "__main__":
    main()