"""Generate ranking and statistical tables for SEAFuzz and six named baselines."""

from pathlib import Path
import pandas as pd


# Configuration
ROOT_DIR = Path("path/to/results")
OUR_METHOD = "SEAFuzz"

# Only these seven fuzzer names are included.
FUZZER_ORDER = [
    "SEAFuzz", "AFL", "AFLFast", "EcoFuzz",
    "DiPri", "AFL-DiPri", "Entropic",
]

PROGRAM_ORDER = [
    "libpng", "libsndfile", "lua", "php", "poppler", "sqlite",
    "bloaty", "re2", "cxxfilt", "gas", "nm", "objcopy",
    "objdump", "readelf", "size", "strip",
]


def read_csv(path):
    try:
        df = pd.read_csv(path, encoding="utf-8-sig", sep=None, engine="python")
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding="gbk", sep=None, engine="python")
    df.columns = df.columns.astype(str).str.strip().str.lower()
    return df


def normalize_fuzzer(value):
    """Match the seven names without using aliases or internal IDs."""
    name = str(value).strip()
    for fuzzer in FUZZER_ORDER:
        if name.casefold() == fuzzer.casefold():
            return fuzzer
    return None


def latex_escape(value):
    special = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
        "$": r"\$", "#": r"\#", "_": r"\_",
        "{": r"\{", "}": r"\}",
    }
    return "".join(special.get(char, char) for char in str(value))


def format_mean_sd(mean, sd):
    if pd.isna(mean):
        return "--"
    if pd.isna(sd):
        return f"{mean:.1f}"
    return f"{mean:.1f}" + r"$\pm$" + f"{sd:.1f}"


def format_rank(value):
    if pd.isna(value):
        return ""
    value = float(value)
    return str(int(value)) if value.is_integer() else f"{value:.1f}"


def format_p(value):
    if pd.isna(value):
        return "--"
    value = float(value)
    result = r"$<.001$" if value < 0.001 else f"{value:.3f}".lstrip("0")
    return result + (r"$^{*}$" if value < 0.05 else "")


def holm_adjust(p_values):
    """Calculate Holm-adjusted p-values in the original order."""
    ordered = sorted(enumerate(p_values), key=lambda pair: pair[1])
    adjusted = [None] * len(ordered)
    previous = 0.0
    for position, (index, p_value) in enumerate(ordered):
        previous = max(previous, min(1.0, (len(ordered) - position) * float(p_value)))
        adjusted[index] = previous
    return adjusted


def load_program(folder):
    name = folder.name
    main_file = folder / f"{name}1.csv"
    sd_file = folder / f"{name}_sd.csv"
    stats_file = folder / f"{name}_statistics.csv"

    if not main_file.is_file() or not sd_file.is_file():
        print(f"Skipping {name}: missing input CSV")
        return None

    raw = read_csv(main_file)
    if not {"name", "value"}.issubset(raw.columns):
        print(f"Skipping {name}: missing name/value columns")
        return None

    raw["name"] = raw["name"].map(normalize_fuzzer)
    raw["value"] = pd.to_numeric(raw["value"], errors="coerce")
    raw = raw[raw["name"].isin(FUZZER_ORDER)].dropna(subset=["value"])
    means = raw.groupby("name", as_index=False)["value"].mean()
    means = means.rename(columns={"value": "Mean"})

    if OUR_METHOD not in set(means["name"]):
        print(f"Skipping {name}: no {OUR_METHOD} data")
        return None

    sd = read_csv(sd_file)
    if not {"name", "sd"}.issubset(sd.columns):
        print(f"Skipping {name}: missing name/sd columns")
        return None

    sd["name"] = sd["name"].map(normalize_fuzzer)
    sd["sd"] = pd.to_numeric(sd["sd"], errors="coerce")
    sd = sd[sd["name"].isin(FUZZER_ORDER)].drop_duplicates("name")
    merged = means.merge(sd[["name", "sd"]], on="name", how="left")

    if stats_file.is_file():
        stats = read_csv(stats_file)
    else:
        print(f"Note: {name} has no statistics CSV")
        stats = pd.DataFrame()

    if {"baseline", "a12", "holm_adjusted_p"}.issubset(stats.columns):
        stats["baseline"] = stats["baseline"].map(normalize_fuzzer)
        stats = stats[
            stats["baseline"].isin(FUZZER_ORDER)
            & stats["baseline"].ne(OUR_METHOD)
        ].drop_duplicates("baseline").copy()
        stats["a12"] = pd.to_numeric(stats["a12"], errors="coerce")
        stats["holm_adjusted_p"] = pd.to_numeric(
            stats["holm_adjusted_p"], errors="coerce"
        )

        # Reapply Holm correction to the six selected baselines.
        if "raw_p" in stats.columns:
            stats["raw_p"] = pd.to_numeric(stats["raw_p"], errors="coerce")
            valid = stats["raw_p"].notna()
            if valid.any():
                stats.loc[valid, "holm_adjusted_p"] = holm_adjust(
                    stats.loc[valid, "raw_p"].tolist()
                )
            if not valid.all():
                print(f"Warning: {name} has missing raw p-values")
        elif not stats.empty:
            print(f"Warning: {name} uses existing Holm p-values (raw_p missing)")

        stats = stats.rename(columns={
            "a12": "A12", "holm_adjusted_p": "Holm_p"
        })
        merged = merged.merge(
            stats[["baseline", "A12", "Holm_p"]],
            left_on="name", right_on="baseline", how="left"
        )
    else:
        if stats_file.is_file():
            print(f"Warning: {name} has invalid statistics columns")
        merged["A12"] = float("nan")
        merged["Holm_p"] = float("nan")

    return merged[["name", "Mean", "sd", "A12", "Holm_p"]]


def build_rank_table(data, programs, fuzzers, mean_ranks):
    lines = [
        r"\begin{table*}[t]",
        r"\centering",
        r"\footnotesize",
        r"\setlength{\tabcolsep}{3.2pt}",
        r"\renewcommand{\arraystretch}{1.08}",
        r"\caption{Path discovery after 24 h. Values are mean $\pm$ SD over 10 runs; superscripts denote per-target ranks. Lower $\mu$Rank is better.}",
        r"\label{tab:path_main}",
        r"\begin{tabular}{@{}l" + "c" * len(fuzzers) + r"@{}}",
        r"\toprule",
        " & ".join([r"\textbf{Program}"] + [
            rf"\textbf{{{latex_escape(fuzzer)}}}"
            for fuzzer in fuzzers
        ]) + r" \\",
        r"\midrule",
    ]

    for program in programs:
        subset = data[data["Target"] == program].set_index("Fuzzer")
        best_mean = subset["Mean"].max()
        cells = [latex_escape(program)]

        for fuzzer in fuzzers:
            if fuzzer not in subset.index:
                cells.append("--")
                continue
            row = subset.loc[fuzzer]
            cell = format_mean_sd(row["Mean"], row["SD"])
            cell += rf"$^{{\scriptscriptstyle {format_rank(row['Rank'])}}}$"
            if row["Mean"] == best_mean:
                cell = r"\textbf{" + cell + "}"
            cells.append(cell)
        lines.append(" & ".join(cells) + r" \\")

    best_rank = min(mean_ranks[fuzzer] for fuzzer in fuzzers)
    cells = [r"\textbf{$\mu$Rank}"]
    for fuzzer in fuzzers:
        value = mean_ranks[fuzzer]
        cell = f"{value:.2f}"
        cells.append(r"\textbf{" + cell + "}" if value == best_rank else cell)

    lines.extend([
        r"\midrule",
        " & ".join(cells) + r" \\",
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table*}",
    ])
    return "\n".join(lines) + "\n"


def build_statistics_table(data, programs, baselines):
    lines = [
        r"\begin{table*}[t]",
        r"\centering",
        r"\footnotesize",
        r"\setlength{\tabcolsep}{4.6pt}",
        r"\renewcommand{\arraystretch}{1.08}",
        r"\caption{Statistical comparison of SEAFuzz with the baselines. Each entry is $\hat{A}_{12}/p_{\mathrm{Holm}}$; $^{*}$ denotes $p_{\mathrm{Holm}}<0.05$.}",
        r"\label{tab:path_stats}",
        r"\begin{tabular}{@{}l" + "c" * len(baselines) + r"@{}}",
        r"\toprule",
    ]

    if baselines:
        lines.extend([
            r"\textbf{Program} & "
            + rf"\multicolumn{{{len(baselines)}}}{{c}}{{\textbf{{SEAFuzz vs. baseline}}}} \\",
            rf"\cmidrule(lr){{2-{len(baselines) + 1}}}",
            " & ".join([""] + [
                rf"\textbf{{{latex_escape(fuzzer)}}}"
                for fuzzer in baselines
            ]) + r" \\",
            r"\midrule",
        ])
        for program in programs:
            subset = data[data["Target"] == program].set_index("Fuzzer")
            cells = [latex_escape(program)]
            for fuzzer in baselines:
                if fuzzer not in subset.index:
                    cells.append("--")
                    continue
                row = subset.loc[fuzzer]
                if pd.isna(row["A12"]) and pd.isna(row["Holm_p"]):
                    cells.append("--")
                else:
                    effect = "--" if pd.isna(row["A12"]) else f"{row['A12']:.2f}"
                    cells.append(f"{effect} / {format_p(row['Holm_p'])}")
            lines.append(" & ".join(cells) + r" \\")
    else:
        lines.extend([r"\textbf{Program} \\", r"\midrule"])
        for program in programs:
            lines.append(latex_escape(program) + r" \\")

    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table*}"])
    return "\n".join(lines) + "\n"


def main():
    if not ROOT_DIR.is_dir():
        raise NotADirectoryError(f"Directory not found: {ROOT_DIR}")

    records = []
    for folder in sorted(ROOT_DIR.iterdir(), key=lambda p: p.name.lower()):
        if not folder.is_dir():
            continue
        df = load_program(folder)
        if df is None:
            continue
        for row in df.itertuples(index=False):
            records.append({
                "Target": folder.name, "Fuzzer": row.name,
                "Mean": row.Mean, "SD": row.sd,
                "A12": row.A12, "Holm_p": row.Holm_p,
            })

    if not records:
        raise RuntimeError("No valid experimental data found")

    data = pd.DataFrame(records)
    available = set(data["Target"])
    programs = [program for program in PROGRAM_ORDER if program in available]
    programs += sorted(available - set(programs), key=str.casefold)
    fuzzers = [fuzzer for fuzzer in FUZZER_ORDER if fuzzer in set(data["Fuzzer"])]
    baselines = [fuzzer for fuzzer in fuzzers if fuzzer != OUR_METHOD]

    # Rank fuzzers by mean path discovery within each target.
    data["Rank"] = data.groupby("Target")["Mean"].rank(
        method="average", ascending=False
    )
    mean_ranks = data.groupby("Fuzzer")["Rank"].mean()
    counts = data.groupby("Fuzzer")["Target"].nunique()
    for fuzzer in fuzzers:
        if counts[fuzzer] < len(programs):
            print(f"Warning: {fuzzer} covers {counts[fuzzer]}/{len(programs)} programs")

    outputs = {
        "all_paths_table_data_with_rank.csv": data,
        "all_paths_rank_table.tex": build_rank_table(
            data, programs, fuzzers, mean_ranks
        ),
        "all_paths_statistics_table.tex": build_statistics_table(
            data, programs, baselines
        ),
    }
    for filename, content in outputs.items():
        path = ROOT_DIR / filename
        if isinstance(content, pd.DataFrame):
            content.to_csv(path, index=False, encoding="utf-8-sig")
        else:
            path.write_text(content, encoding="utf-8")
        print(f"Saved: {path}")

    print(f"Completed: {len(programs)} programs, {len(fuzzers)} fuzzers")


if __name__ == "__main__":
    main()
