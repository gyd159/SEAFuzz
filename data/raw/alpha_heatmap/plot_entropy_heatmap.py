
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Draw a readable two-row entropy-distribution heatmap and export EPS/PDF."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap, PowerNorm


# ============================================================
# 1. Users only need to modify these three paths
# ============================================================

INPUT_CSV = Path(r"D:\outputx\outputx_alpha\afl4_aflpha_0.2_grid\entropy_heatmap_data.csv")
OUTPUT_EPS = Path(r"D:\outputx\outputx_alpha\afl4_aflpha_0.2_grid\heatmap\entropy_distribution_heatmap_final_v2.eps")
OUTPUT_PDF = Path(r"D:\outputx\outputx_alpha\afl4_aflpha_0.2_grid\heatmap\entropy_distribution_heatmap_final_v2.pdf")


# ============================================================
# 2. Figure layout and font settings (usually no changes needed)
# ============================================================

# Keep the original 3+2 layout unchanged.
# Increase the figure height, enlarge the heatmaps and fonts,
# and place the colorbar at the bottom.
FIGSIZE = (19, 22.36)  # Height increased by 30% compared with the previous version

FONT_SUPTITLE = 19
FONT_PANEL_TITLE = 24
FONT_AXIS_LABEL = 20
FONT_X_TICK = 18
FONT_Y_TICK = 17
FONT_COLORBAR = 19

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 3  # EPS: Type 3 glyphs, broadly compatible with PostScript viewers


def main():
    if not INPUT_CSV.is_file():
        raise FileNotFoundError(f"Input CSV file not found: {INPUT_CSV}")

    data = pd.read_csv(INPUT_CSV)

    required = {"program", "alpha", "entropy_bin", "percentage"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Missing required columns in CSV: {sorted(missing)}")

    programs = sorted(data["program"].dropna().unique())
    alphas = sorted(data["alpha"].dropna().unique(), key=float)
    bins = list(dict.fromkeys(data["entropy_bin"]))
    bin_width = float(data["bin_width"].iloc[0]) if "bin_width" in data else 1.0

    if len(alphas) > 5:
        raise ValueError(
            f"The current two-row layout supports at most 5 alpha values, "
            f"but {len(alphas)} were detected."
        )

    # Use a shared color range for all subplots to ensure
    # direct comparability across different alpha values.
    max_percentage = float(data["percentage"].max())
    vmax = max(10.0, (max_percentage // 10 + 1) * 10)

    # Color adjustments:
    # Do not modify the original data; only adjust the color representation.
    # Cells with 0% are displayed in light gray.
    # Cells with values greater than 0% use a blue gradient.
    # Remove the lightest, nearly white portion of the Blues colormap
    # to improve the visibility of low-percentage values.
    blue_colors = plt.get_cmap("Blues")(np.linspace(0.25, 1.0, 256))
    cmap = LinearSegmentedColormap.from_list("VisibleBlues", blue_colors)
    cmap.set_bad("#F0F0F0")

    # gamma < 1 enhances visual differences in the low-percentage range.
    # All subplots use the same normalization.
    norm = PowerNorm(gamma=0.4, vmin=0, vmax=vmax)

    # Maintain the original 3+2 two-row layout.
    # Expand the plotting area while leaving sufficient space
    # for larger fonts and axis labels.
    # Coordinates are relative to the entire figure:
    # (left, bottom, width, height).
    fig = plt.figure(figsize=FIGSIZE)
    panel_width = 0.25
    panel_height = 0.31
    positions = [
        (0.040, 0.642, panel_width, panel_height),
        (0.375, 0.642, panel_width, panel_height),
        (0.710, 0.642, panel_width, panel_height),
        (0.2075, 0.192, panel_width, panel_height),
        (0.5425, 0.192, panel_width, panel_height),
    ]

    axes = []
    image = None

    for index, alpha in enumerate(alphas):
        ax = fig.add_axes(positions[index])
        axes.append(ax)

        sub = data[data["alpha"] == alpha]
        matrix = sub.pivot(
            index="entropy_bin",
            columns="program",
            values="percentage",
        )
        matrix = matrix.reindex(index=bins, columns=programs, fill_value=0)

        # Mask only cells with an exact percentage of 0.
        # This does not affect the statistics of the H=0 entropy bin.
        values = matrix.to_numpy(dtype=float)
        masked_values = np.ma.masked_where(values == 0, values)

        image = ax.imshow(
            masked_values,
            aspect="auto",
            cmap=cmap,
            norm=norm,
            interpolation="nearest",
            origin="lower",  # Entropy values increase from bottom to top
        )

        ax.set_title(f"α = {float(alpha):g}", fontsize=FONT_PANEL_TITLE, pad=11)

        ax.set_xticks(range(len(programs)))
        ax.set_xticklabels(
            programs,
            rotation=65,
            ha="right",
            rotation_mode="anchor",
            fontsize=FONT_X_TICK,
        )
        ax.set_xlabel("Program", fontsize=FONT_AXIS_LABEL, labelpad=9)

        # Use simple integer tick labels on the y-axis:
        # 0, 1, 2, ..., 10.
        # Each entropy unit corresponds to 1 / bin_width bins.
        # Do not display interval brackets.
        rows_per_unit = max(1, round(1.0 / bin_width))
        tick_positions = list(range(0, len(bins), rows_per_unit))
        tick_labels = [str(i) for i in range(len(tick_positions))]

        ax.set_yticks(tick_positions)
        ax.set_yticklabels(tick_labels, fontsize=FONT_Y_TICK)

        # Do not add an extra y-axis title.
        # Entropy values increase upward, starting from 0 at the bottom.

        ax.tick_params(
            axis="both",
            which="major",
            length=3.5,
            width=0.8,
        )

        for spine in ax.spines.values():
            spine.set_linewidth(0.8)

    # Place a shared horizontal colorbar at the bottom.
    # This frees up the space previously occupied by
    # the vertical colorbar on the right.
    cax = fig.add_axes([0.24, 0.052, 0.52, 0.018])

    colorbar = fig.colorbar(
        image,
        cax=cax,
        orientation="horizontal",
    )

    colorbar.set_label(
        "Seed Proportion (%)",
        fontsize=FONT_COLORBAR,
        labelpad=10,
    )

    # PowerNorm uses nonlinear color mapping.
    # Use relatively sparse ticks representing actual percentages
    # to prevent the colorbar labels from overlapping.
    colorbar_ticks = sorted(
        set(
            v for v in [0, 1, 5, 10, 20, 40, 60, vmax]
            if v <= vmax
        )
    )

    colorbar.set_ticks(colorbar_ticks)
    colorbar.ax.tick_params(
        labelsize=FONT_COLORBAR - 1,
        length=3,
    )

    # Automatically create the output directories
    # and save the figure in both EPS and PDF formats.
    #
    # EPS uses Type 3 fonts for improved compatibility
    # with PostScript/LaTeX toolchains.
    # PDF continues to use Type 42 fonts.
    OUTPUT_EPS.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(
        OUTPUT_EPS,
        format="eps",
        bbox_inches="tight",
        pad_inches=0.15,
    )

    fig.savefig(
        OUTPUT_PDF,
        format="pdf",
        bbox_inches="tight",
        pad_inches=0.15,
    )

    print("\nGeneration completed successfully:")
    print(f"  Input CSV: {INPUT_CSV}")
    print(f"  EPS output: {OUTPUT_EPS}")
    print(f"  PDF output: {OUTPUT_PDF}")

    plt.close(fig)


if __name__ == "__main__":
    main()
