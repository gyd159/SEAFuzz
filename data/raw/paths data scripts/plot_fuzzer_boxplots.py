"""Plot 4x4 boxplots comparing the seven fuzzers on benchmark programs."""

from pathlib import Path
import math
import string

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import FixedLocator, FuncFormatter


# Configuration
ROOT_DIR = Path("path/to/experiment/results")
INPUT_XLSX = ROOT_DIR / "boxplot_data.xlsx"
OUTPUT_DIR = ROOT_DIR / "boxplots"

FUZZER_ORDER = (
    "SEAFuzz", "AFL", "AFLFast", "EcoFuzz",
    "DiPri", "AFL-DiPri", "Entropic",
)
FUZZER_COLORS = {
    "SEAFuzz": "#C62828",
    "AFL": "#1565C0",
    "AFLFast": "#2E7D32",
    "EcoFuzz": "#EF6C00",
    "DiPri": "#0097A7",
    "AFL-DiPri": "#6A1B9A",
    "Entropic": "#5D4037",
}

PROGRAM_GRID = [
    ["libpng", "libsndfile", "lua", "php"],
    ["poppler", "sqlite", "bloaty", "re2"],
    ["cxxfilt", "gas", "nm", "objcopy"],
    ["objdump", "readelf", "size", "strip"],
]

# These aliases apply to benchmark program names, not fuzzer names.
PROGRAM_ALIASES = {"as-new": "gas", "sqlite3": "sqlite", "strip-new": "strip"}
PROGRAM_DISPLAY_NAMES = {"gas": "as-new", "sqlite": "sqlite3", "strip": "strip-new"}

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "DejaVu Sans"],
    "axes.unicode_minus": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 3,
})

FIGSIZE = (9.1, 8.2)
FONT_Y_LABEL = 9.5
FONT_Y_TICK = 8.8
FONT_PANEL_TITLE = 9.5
FONT_LEGEND = 9.0
BOX_STEP = 0.72
BOX_WIDTH = 0.46


def load_data(path):
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
    df = pd.read_excel(path)
    required = {"Program", "Fuzzer", "Paths"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing columns: {sorted(required - set(df.columns))}")

    df = df.dropna(subset=["Program", "Fuzzer"]).copy()
    df["Program"] = df["Program"].astype(str).str.strip().str.casefold()
    df["Program"] = df["Program"].replace(PROGRAM_ALIASES)
    df["Fuzzer"] = df["Fuzzer"].astype(str).str.strip().str.casefold()
    df["Paths"] = pd.to_numeric(df["Paths"], errors="coerce")
    df = df[df["Fuzzer"].isin({fuzzer.casefold() for fuzzer in FUZZER_ORDER})]
    if not df["Paths"].notna().any():
        raise RuntimeError("No valid path count data found.")
    return df


def set_clean_y_axis(ax, values):
    minimum, maximum = float(np.min(values)), float(np.max(values))
    span = maximum - minimum
    if span <= 0:
        span = max(abs(maximum) * 0.08, 1.0)
        minimum -= span / 2
        maximum += span / 2

    margin = 0.035 * span
    low, high = minimum - margin, maximum + margin
    target_step = (high - low) / 4
    exponent = math.floor(math.log10(target_step)) if target_step > 0 else 0
    candidates = sorted({
        multiplier * 10.0 ** power
        for power in range(exponent - 2, exponent + 4)
        for multiplier in (1, 2, 5, 10)
    })

    choices = []
    for step in candidates:
        first = math.floor(low / step) * step
        last = math.ceil(high / step) * step
        count = int(round((last - first) / step)) + 1
        if 4 <= count <= 5:
            unused = ((last - first) - (high - low)) / (high - low)
            choices.append((unused + (0.07 if count == 4 else 0), step, first, count))

    if choices:
        _, step, first, count = min(choices)
    else:
        step = next(s for s in candidates if s * 4 >= high - low)
        first = math.floor(low / step) * step
        count = int(math.ceil((high - first) / step)) + 1

    ticks = np.round(first + np.arange(count) * step, 9)
    ax.set_ylim(float(ticks[0]), float(ticks[-1]))
    ax.yaxis.set_major_locator(FixedLocator(ticks))
    ax.yaxis.set_major_formatter(FuncFormatter(
        lambda value, _: str(int(round(value)))
        if abs(value - round(value)) < 1e-7
        else f"{value:.2f}".rstrip("0").rstrip(".")
    ))
    ax.yaxis.get_offset_text().set_visible(False)


def main():
    df = load_data(INPUT_XLSX)
    programs = [program for row in PROGRAM_GRID for program in row]
    fig, axes = plt.subplots(4, 4, figsize=FIGSIZE, sharex=False, sharey=False)
    fig.patch.set_facecolor("white")

    for index, program in enumerate(programs):
        ax = axes.flat[index]
        data = df[df["Program"] == program]
        samples, positions, present = [], [], []
        for fuzzer_index, fuzzer in enumerate(FUZZER_ORDER):
            values = data.loc[data["Fuzzer"] == fuzzer.casefold(), "Paths"]
            values = values.dropna().to_numpy(dtype=float)
            if len(values):
                if len(values) != 10:
                    print(f"  {program} / {fuzzer}: {len(values)} valid runs")
                samples.append(values)
                positions.append(1 + fuzzer_index * BOX_STEP)
                present.append(fuzzer)

        ax.set_facecolor("white")
        ax.grid(False)
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("black")
            spine.set_linewidth(0.8)

        if samples:
            boxes = ax.boxplot(
                samples,
                positions=positions,
                widths=BOX_WIDTH,
                patch_artist=True,
                whis=1.5,
                showfliers=True,
                boxprops={"edgecolor": "black", "linewidth": 0.8},
                medianprops={"color": "black", "linewidth": 1.0},
                whiskerprops={"color": "black", "linewidth": 0.8},
                capprops={"color": "black", "linewidth": 0.8},
                flierprops={"marker": "o", "markerfacecolor": "white",
                            "markeredgecolor": "black", "markeredgewidth": 0.7,
                            "markersize": 2.8, "linestyle": "none"},
            )
            for patch, fuzzer in zip(boxes["boxes"], present):
                patch.set_facecolor(FUZZER_COLORS[fuzzer])
            set_clean_y_axis(ax, np.concatenate(samples))
        else:
            ax.text(0.5, 0.5, "No data", transform=ax.transAxes,
                    ha="center", va="center", fontsize=FONT_Y_TICK)
            ax.set_yticks([])

        ticks = np.arange(len(FUZZER_ORDER)) * BOX_STEP + 1
        ax.set_xlim(ticks[0] - 0.42, ticks[-1] + 0.42)
        ax.set_xticks(ticks)
        ax.set_xticklabels([])
        ax.tick_params(axis="x", bottom=False, top=False, labelbottom=False)
        ax.set_ylabel("Paths", fontsize=FONT_Y_LABEL, labelpad=2)
        ax.yaxis.set_label_coords(-0.32, 0.5)
        ax.tick_params(axis="y", labelsize=FONT_Y_TICK,
                       width=0.7, length=2.5, pad=2, direction="out")
        label = PROGRAM_DISPLAY_NAMES.get(program, program)
        ax.text(0.5, -0.17, f"({string.ascii_lowercase[index]}) {label}",
                transform=ax.transAxes, ha="center", va="top",
                fontsize=FONT_PANEL_TITLE, clip_on=False)

    fig.subplots_adjust(left=0.095, right=0.995, top=0.985,
                        bottom=0.115, wspace=0.49, hspace=0.56)
    fig.legend(
        handles=[Patch(facecolor=FUZZER_COLORS[fuzzer], edgecolor="none", label=fuzzer)
                 for fuzzer in FUZZER_ORDER],
        ncol=7, loc="lower center", bbox_to_anchor=(0.5, 0.008),
        frameon=False, handlelength=1.85, handleheight=0.85,
        handletextpad=0.42, columnspacing=1.25,
        borderaxespad=0, prop={"size": FONT_LEGEND},
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for extension in ("pdf", "eps"):
        output = OUTPUT_DIR / f"all_fuzzer_boxplots.{extension}"
        fig.savefig(output, format=extension, bbox_inches="tight", pad_inches=0.03)
        print(f"Saved: {output}")
    plt.close(fig)


if __name__ == "__main__":
    main()
