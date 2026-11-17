"""Combine 24-hour path counts into an Excel dataset for fuzzer boxplots."""

from pathlib import Path
from copy import copy

import pandas as pd


# Configuration
ROOT_DIR = Path("path/to/experiment/results")
OUTPUT_XLSX = ROOT_DIR / "boxplot_data.xlsx"
FUZZER_ORDER = (
    "SEAFuzz", "AFL", "AFLFast", "EcoFuzz",
    "DiPri", "AFL-DiPri", "Entropic",
)
EXPECTED_RUNS = 10
PANEL_COLS = 4
MAX_PANELS = 16
OUTPUT_COLUMNS = [
    "Program", "PanelRow", "PanelCol", "Fuzzer", "Paths", "FuzzerOrder"
]


def read_input_csv(path):
    try:
        df = pd.read_csv(path, encoding="utf-8-sig")
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding="gbk")
    df.columns = df.columns.astype(str).str.strip().str.casefold()
    if not {"name", "value"}.issubset(df.columns):
        raise ValueError(f"Missing name or value columns: {path}")
    df = df[["name", "value"]].copy()
    df["name"] = df["name"].astype("string").str.strip().str.casefold()
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df.dropna(subset=["name"])


def main():
    if not ROOT_DIR.is_dir():
        raise NotADirectoryError(f"Directory not found: {ROOT_DIR}")

    prepared = []
    valid_names = {fuzzer.casefold() for fuzzer in FUZZER_ORDER}
    for program_dir in sorted(
        (p for p in ROOT_DIR.iterdir() if p.is_dir()), key=lambda p: p.name.casefold()
    ):
        path = program_dir / f"{program_dir.name}1.csv"
        if not path.is_file():
            continue
        df = read_input_csv(path)
        df = df[df["name"].isin(valid_names)]
        if df["value"].notna().any():
            prepared.append((program_dir.name, df))
        else:
            print(f"Skipping {program_dir.name}: no valid values")

    if not prepared:
        raise RuntimeError("No valid program data found.")
    if len(prepared) > MAX_PANELS:
        raise ValueError(f"Expected at most {MAX_PANELS} programs, found {len(prepared)}")

    rows = []
    for panel_idx, (program, df) in enumerate(prepared):
        for order, fuzzer in enumerate(FUZZER_ORDER, start=1):
            values = df.loc[df["name"] == fuzzer.casefold(), "value"]
            valid = values.notna().sum()
            if len(values) != EXPECTED_RUNS or valid != EXPECTED_RUNS:
                print(f"  {program} / {fuzzer}: {int(valid)}/{EXPECTED_RUNS} valid runs")

            for value in values:
                rows.append({
                    "Program": program,
                    "PanelRow": panel_idx // PANEL_COLS + 1,
                    "PanelCol": panel_idx % PANEL_COLS + 1,
                    "Fuzzer": fuzzer,
                    "Paths": float(value) if pd.notna(value) else None,
                    "FuzzerOrder": order,
                })

    if not rows:
        raise RuntimeError("No boxplot records found.")
    result = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    OUTPUT_XLSX.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(OUTPUT_XLSX, engine="openpyxl") as writer:
        result.to_excel(writer, sheet_name="BoxplotData", index=False)
        sheet = writer.sheets["BoxplotData"]
        sheet.freeze_panes = "A2"
        sheet.auto_filter.ref = sheet.dimensions
        for column, width in {"A": 20, "B": 13, "C": 13,
                              "D": 20, "E": 16, "F": 16}.items():
            sheet.column_dimensions[column].width = width
        for cell in sheet[1]:
            font = copy(cell.font)
            font.bold = True
            cell.font = font

    print(f"Saved: {OUTPUT_XLSX} ({len(prepared)} programs, {len(result)} rows)")


if __name__ == "__main__":
    main()
