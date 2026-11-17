# SEAFuzz Analysis: Modules and Workflows

Nine Python scripts support comparisons of **SEAFuzz, AFL, AFLFast, EcoFuzz, DiPri, AFL-DiPri, and Entropic**. Fuzzer names are used directly, without mapping.

## Modules

| Module | Scripts | Purpose |
| --- | --- | --- |
| **M1 — Path time series** | `fuzzer_plot_data_preprocessor.py`, `fuzzer_path_timeseries.py` | Extract per-run minute-level data or calculate mean path counts. Run either script independently. |
| **M2 — 24-hour paths** | `extract_24h_path_counts.py` | Extract a 24-hour path count for each run. |
| **M3 — Statistics** | `fuzzer_standard_deviation.py`, `fuzzer_statistical_analysis.py`, `seafuzz_baseline_comparison.py` | Calculate SD, Mann–Whitney U, A12, Holm-adjusted p-values, and paper tables. |
| **M4 — Boxplots** | `prepare_boxplot_data.py`, `plot_fuzzer_boxplots.py` | Prepare Excel data and export boxplot figures. |
| **M5 — Seed counts** | `seed_count_analysis.py` | Analyze seed counts independently of M1–M4. |

## Which Scripts Should I Run?

| Goal | Workflow | Output |
| --- | --- | --- |
| Per-run minute-level paths | M1: `fuzzer_plot_data_preprocessor.py` | `xinjia/<fuzzer>.csv` |
| Mean path growth curves | M1: `fuzzer_path_timeseries.py` | `<program>.csv` |
| 24-hour results | M2 | `<program>1.csv` |
| Standard deviations | M2 → `fuzzer_standard_deviation.py` | `<program>_sd.csv` |
| Statistical comparisons | M2 → `fuzzer_statistical_analysis.py` | `<program>_statistics.csv` |
| Paper tables | M2 → standard deviation + statistical tests → `seafuzz_baseline_comparison.py` | `all_paths_rank_table.tex`, `all_paths_statistics_table.tex` |
| Boxplot figures | M2 → `prepare_boxplot_data.py` → `plot_fuzzer_boxplots.py` | `boxplots/*.pdf`, `boxplots/*.eps` |
| Seed-count time series and 24-hour summary | M5 | `all.csv`, `mean.csv`, `final.csv` |

## Setup

```bash
pip install numpy pandas scipy statsmodels matplotlib openpyxl
```

Set `ROOT_DIR`, `BASE_ROOT`, or `INPUT_ROOT` in each script to your experiment directory. Path workflows read `plot_data`; the seed-count workflow reads `seed_count.csv`.

**Notes:** Path scripts use the first `plot_data` column as time and the fourth as the metric. The 24-hour path count defaults to the latest recorded value at or before 24 hours (or the last value of a shorter run). Seed-count minute values use linear interpolation, while its 24-hour final value requires an actual record **at or after 86,400 seconds**. In `fuzzer_statistical_analysis.py`, set `OUR_METHOD = "seafuzz"`; the table-generation script uses `"SEAFuzz"`.
