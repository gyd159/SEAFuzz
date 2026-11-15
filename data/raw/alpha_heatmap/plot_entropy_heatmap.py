#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Draw a readable two-row entropy-distribution heatmap and export EPS/PDF."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap, PowerNorm


# ============================================================
# 1. 用户只需要修改这三个路径
# ============================================================

INPUT_CSV = Path(r"D:\outputx\outputx_alpha\afl4_aflpha_0.2格子\entropy_heatmap_data.csv")
OUTPUT_EPS = Path(r"D:\outputx\outputx_alpha\afl4_aflpha_0.2格子\热力图\entropy_distribution_heatmap_final_v2.eps")
OUTPUT_PDF = Path(r"D:\outputx\outputx_alpha\afl4_aflpha_0.2格子\热力图\entropy_distribution_heatmap_final_v2.pdf")


# ============================================================
# 2. 图像布局与字体设置（一般不需要修改）
# ============================================================

# 原来的 3+2 排版不变；增高画布、增大热力图和字体，热力条放下方。
FIGSIZE = (19, 22.36)  # 高度在上一版基础上增加 30%

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
        raise FileNotFoundError(f"找不到输入 CSV 文件：{INPUT_CSV}")

    data = pd.read_csv(INPUT_CSV)

    required = {"program", "alpha", "entropy_bin", "percentage"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"CSV 缺少必要列：{sorted(missing)}")

    programs = sorted(data["program"].dropna().unique())
    alphas = sorted(data["alpha"].dropna().unique(), key=float)
    bins = list(dict.fromkeys(data["entropy_bin"]))
    bin_width = float(data["bin_width"].iloc[0]) if "bin_width" in data else 1.0

    if len(alphas) > 5:
        raise ValueError(
            f"当前脚本的两行布局最多支持 5 个 alpha，实际检测到 {len(alphas)} 个。"
        )

    # 所有子图共用颜色范围，确保不同 alpha 之间可以直接比较。
    max_percentage = float(data["percentage"].max())
    vmax = max(10.0, (max_percentage // 10 + 1) * 10)

    # 颜色调整：不改变原始数据，只调整颜色显示。
    # 0% 格子显示为浅灰；大于 0% 的格子使用蓝色渐变。
    # 截掉 Blues 里最浅的、接近白色的部分，以提高低占比可见性。
    blue_colors = plt.get_cmap("Blues")(np.linspace(0.25, 1.0, 256))
    cmap = LinearSegmentedColormap.from_list("VisibleBlues", blue_colors)
    cmap.set_bad("#F0F0F0")

    # gamma < 1 放大低比例区间的视觉差异；所有子图共用相同归一化。
    norm = PowerNorm(gamma=0.4, vmin=0, vmax=vmax)

    # 仍是原来的 3+2 两行布局；扩展绘图区，同时留足大字体的空间。
    # 坐标为整张画布的相对位置 (left, bottom, width, height)。
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

        # 只遮罩占比恰好为 0 的格子（不影响 H=0 这一熵区间的正常统计）。
        values = matrix.to_numpy(dtype=float)
        masked_values = np.ma.masked_where(values == 0, values)
        image = ax.imshow(
            masked_values,
            aspect="auto",
            cmap=cmap,
            norm=norm,
            interpolation="nearest",
            origin="lower",  # 熵值从下往上递增
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

        # 纵坐标使用简洁的整数刻度：0、1、2、...、10。
        # 每 1 个熵单位对应 1 / bin_width 个分箱；不显示区间括号。
        rows_per_unit = max(1, round(1.0 / bin_width))
        tick_positions = list(range(0, len(bins), rows_per_unit))
        tick_labels = [str(i) for i in range(len(tick_positions))]
        ax.set_yticks(tick_positions)
        ax.set_yticklabels(tick_labels, fontsize=FONT_Y_TICK)

        # 不添加额外的纵轴标题；熵值从底部 0 向顶部递增。

        ax.tick_params(axis="both", which="major", length=3.5, width=0.8)
        for spine in ax.spines.values():
            spine.set_linewidth(0.8)

    # 底部公共水平热力条，释放原来右侧占用的绘图空间。
    cax = fig.add_axes([0.24, 0.052, 0.52, 0.018])
    colorbar = fig.colorbar(image, cax=cax, orientation="horizontal")
    colorbar.set_label(
        "Seed Proportion (%)",
        fontsize=FONT_COLORBAR,
        labelpad=10,
    )
    # PowerNorm 为非线性映射；用较疏的真实百分比刻度避免标签拥挤。
    colorbar_ticks = sorted(set(v for v in [0, 1, 5, 10, 20, 40, 60, vmax] if v <= vmax))
    colorbar.set_ticks(colorbar_ticks)
    colorbar.ax.tick_params(labelsize=FONT_COLORBAR - 1, length=3)

    # 自动创建输出目录，并分别保存 EPS、PDF。
    # EPS 使用 Type 3 字体以提高 PostScript/LaTeX 工具链兼容性；PDF 仍使用 Type 42。
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

    print("\n生成完成：")
    print(f"  输入 CSV：{INPUT_CSV}")
    print(f"  EPS：{OUTPUT_EPS}")
    print(f"  PDF：{OUTPUT_PDF}")

    plt.close(fig)


if __name__ == "__main__":
    main()
