from pathlib import Path
import pandas as pd
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests


# Configuration
ROOT_DIR = Path("path/to/results")
OUR_METHOD = "afl4"


def vargha_delaney_a12(x, y):
    """Calculate A12 = P(X > Y) + 0.5 * P(X = Y)."""
    wins = 0
    ties = 0

    for a in x:
        for b in y:
            if a > b:
                wins += 1
            elif a == b:
                ties += 1

    return (wins + 0.5 * ties) / (len(x) * len(y))


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

        ours = df.loc[df["name"] == OUR_METHOD, "value"].to_numpy()

        if len(ours) == 0:
            print(f"Skipping: No valid data for {OUR_METHOD} in {folder_name}")
            continue

        baselines = [
            name for name in df["name"].unique()
            if name != OUR_METHOD
        ]

        raw_p_values = []
        results = []

        for baseline in baselines:
            baseline_values = df.loc[
                df["name"] == baseline, "value"
            ].to_numpy()

            if len(baseline_values) == 0:
                continue

            _, p_value = mannwhitneyu(
                ours,
                baseline_values,
                alternative="two-sided",
                method="auto"
            )

            a12 = vargha_delaney_a12(ours, baseline_values)

            raw_p_values.append(p_value)
            results.append({
                "comparison": f"{OUR_METHOD} vs {baseline}",
                "baseline": baseline,
                "A12": a12,
                "raw_p": p_value
            })

        if not results:
            print(f"Skipping: No baselines found in {folder_name}")
            continue

        # Apply Holm correction to all baseline comparisons
        reject, adjusted_p, _, _ = multipletests(
            raw_p_values,
            alpha=0.05,
            method="holm"
        )

        for i, row in enumerate(results):
            row["Holm_adjusted_p"] = adjusted_p[i]
            row["significant"] = "Yes" if reject[i] else "No"

        result_df = pd.DataFrame(results)
        result_df["A12"] = result_df["A12"].round(4)

        output_csv = sub_dir / f"{folder_name}_statistics.csv"
        result_df.to_csv(output_csv, index=False, encoding="utf-8-sig")

        print(f"Saved: {output_csv} ({len(result_df)} comparisons)")

    print("\nStatistical analysis completed.")


if __name__ == "__main__":
    main()