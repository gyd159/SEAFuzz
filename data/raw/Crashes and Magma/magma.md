# Magma — Bug Reaching and Triggering Results

> SEAFuzz evaluation · 16 programs · 13 fuzzers · run IDs 0–9

## Overview

| Item | Value |
| --- | --- |
| Programs in run inventory | **16** |
| Fuzzers per program | **13** |
| Run IDs per program and fuzzer | **0–9** |
| Program × fuzzer × run records | **2,080** |
| Programs with actual Magma results | **6** (`libpng`, `libsndfile`, `lua`, `php`, `poppler`, `sqlite`) |
| Magma fuzzer summaries | **78** |
| Magma per-run summaries | **780** |
| Recorded bug observations | **9,212** |
| Recorded crash observations | **7,773** |

**Coverage:** Magma measurements are available for six targets. The other ten programs are included in the run inventory without Magma measurements.

**Metrics:** `Reached (tot/uni)` and `Triggered (tot/uni)` use `tot` for the sum of per-run bug counts and `uni` for distinct bug IDs across runs. Consistency and run-level fields are reported alongside the results.

## Magma results — overall across six targets

| Fuzzer | Reached (tot/uni) | Triggered (tot/uni) |
| --- | --- | --- |
| AFL | **69/11** | **50/6** |
| AFLFast | **56/10** | **47/6** |
| EcoFuzz | **40/4** | **40/4** |
| DiPri | **66/10** | **47/6** |
| AFL-DiPri | **74/12** | **53/6** |
| Entropic | **71/9** | **42/5** |
| P-FE | **54/10** | **46/6** |
| E-FE | **71/11** | **51/6** |
| P-F | **66/10** | **50/6** |
| E-F | **59/10** | **48/6** |
| PE-F | **70/15** | **51/7** |
| PE-E | **83/12** | **55/6** |
| SEAFuzz | **78/16** | **54/7** |

*Totals are calculated across the six measured Magma targets.*

## Magma results — per target

### `libpng` — 7 known bugs

| Fuzzer | Reached (tot/uni) | Triggered (tot/uni) | Reached consistency | Triggered consistency | Unreached | Untriggered |
| --- | --- | --- | --- | --- | --- | --- |
| AFL | 16/4 | 4/1 | 0.400000 | 0.400000 | 3 | 6 |
| AFLFast | 4/4 | 1/1 | 0.100000 | 0.100000 | 3 | 6 |
| EcoFuzz | 0/0 | 0/0 | 0.000000 | 0.000000 | 7 | 7 |
| DiPri | 20/4 | 5/1 | 0.500000 | 0.500000 | 3 | 6 |
| AFL-DiPri | 13/5 | 3/1 | 0.260000 | 0.300000 | 2 | 6 |
| Entropic | 38/5 | 9/1 | 0.760000 | 0.900000 | 2 | 6 |
| P-FE | 4/4 | 1/1 | 0.100000 | 0.100000 | 3 | 6 |
| E-FE | 16/4 | 4/1 | 0.400000 | 0.400000 | 3 | 6 |
| P-F | 12/4 | 3/1 | 0.300000 | 0.300000 | 3 | 6 |
| E-F | 8/4 | 2/1 | 0.200000 | 0.200000 | 3 | 6 |
| PE-F | 13/5 | 3/1 | 0.260000 | 0.300000 | 2 | 6 |
| PE-E | 21/5 | 5/1 | 0.420000 | 0.500000 | 2 | 6 |
| SEAFuzz | 4/4 | 1/1 | 0.100000 | 0.100000 | 3 | 6 |

### `libsndfile` — 18 known bugs

| Fuzzer | Reached (tot/uni) | Triggered (tot/uni) | Reached consistency | Triggered consistency | Unreached | Untriggered |
| --- | --- | --- | --- | --- | --- | --- |
| AFL | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |
| AFLFast | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |
| EcoFuzz | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |
| DiPri | 40/4 | 39/4 | 1.000000 | 0.975000 | 14 | 14 |
| AFL-DiPri | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |
| Entropic | 33/4 | 33/4 | 0.825000 | 0.825000 | 14 | 14 |
| P-FE | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |
| E-FE | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |
| P-F | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |
| E-F | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |
| PE-F | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |
| PE-E | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |
| SEAFuzz | 40/4 | 40/4 | 1.000000 | 1.000000 | 14 | 14 |

### `lua` — 4 known bugs

| Fuzzer | Reached (tot/uni) | Triggered (tot/uni) | Reached consistency | Triggered consistency | Unreached | Untriggered |
| --- | --- | --- | --- | --- | --- | --- |
| AFL | 13/3 | 6/1 | 0.433333 | 0.600000 | 1 | 3 |
| AFLFast | 12/2 | 6/1 | 0.600000 | 0.600000 | 2 | 3 |
| EcoFuzz | 0/0 | 0/0 | 0.000000 | 0.000000 | 4 | 4 |
| DiPri | 6/2 | 3/1 | 0.300000 | 0.300000 | 2 | 3 |
| AFL-DiPri | 21/3 | 10/1 | 0.700000 | 1.000000 | 1 | 3 |
| Entropic | 0/0 | 0/0 | 0.000000 | 0.000000 | 4 | 4 |
| P-FE | 10/2 | 5/1 | 0.500000 | 0.500000 | 2 | 3 |
| E-FE | 15/3 | 7/1 | 0.500000 | 0.700000 | 1 | 3 |
| P-F | 14/2 | 7/1 | 0.700000 | 0.700000 | 2 | 3 |
| E-F | 11/2 | 6/1 | 0.550000 | 0.600000 | 2 | 3 |
| PE-F | 13/2 | 7/1 | 0.650000 | 0.700000 | 2 | 3 |
| PE-E | 22/3 | 10/1 | 0.733333 | 1.000000 | 1 | 3 |
| SEAFuzz | 21/3 | 10/1 | 0.700000 | 1.000000 | 1 | 3 |

### `php` — 16 known bugs

| Fuzzer | Reached (tot/uni) | Triggered (tot/uni) | Reached consistency | Triggered consistency | Unreached | Untriggered |
| --- | --- | --- | --- | --- | --- | --- |
| AFL | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| AFLFast | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| EcoFuzz | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| DiPri | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| AFL-DiPri | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| Entropic | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| P-FE | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| E-FE | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| P-F | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| E-F | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| PE-F | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| PE-E | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |
| SEAFuzz | 0/0 | 0/0 | 0.000000 | 0.000000 | 16 | 16 |

### `poppler` — 22 known bugs

| Fuzzer | Reached (tot/uni) | Triggered (tot/uni) | Reached consistency | Triggered consistency | Unreached | Untriggered |
| --- | --- | --- | --- | --- | --- | --- |
| AFL | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| AFLFast | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| EcoFuzz | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| DiPri | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| AFL-DiPri | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| Entropic | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| P-FE | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| E-FE | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| P-F | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| E-F | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| PE-F | 4/4 | 1/1 | 0.100000 | 0.100000 | 18 | 21 |
| PE-E | 0/0 | 0/0 | 0.000000 | 0.000000 | 22 | 22 |
| SEAFuzz | 13/5 | 3/1 | 0.260000 | 0.300000 | 17 | 21 |

### `sqlite` — 19 known bugs

| Fuzzer | Reached (tot/uni) | Triggered (tot/uni) | Reached consistency | Triggered consistency | Unreached | Untriggered |
| --- | --- | --- | --- | --- | --- | --- |
| AFL | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| AFLFast | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| EcoFuzz | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| DiPri | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| AFL-DiPri | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| Entropic | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| P-FE | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| E-FE | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| P-F | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| E-F | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| PE-F | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| PE-E | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |
| SEAFuzz | 0/0 | 0/0 | 0.000000 | 0.000000 | 19 | 19 |

## Run inventory — 16 programs

Each program is represented by 13 fuzzers and ten run IDs (`0`–`9`).

<details>
<summary><strong>bloaty</strong> — 13 fuzzers × run IDs 0–9 (run inventory only)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>cxxfilt</strong> — 13 fuzzers × run IDs 0–9 (run inventory only)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>as-new</strong> — 13 fuzzers × run IDs 0–9 (run inventory only)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>libpng</strong> — 13 fuzzers × run IDs 0–9 (Magma measured)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>libsndfile</strong> — 13 fuzzers × run IDs 0–9 (Magma measured)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>lua</strong> — 13 fuzzers × run IDs 0–9 (Magma measured)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>nm</strong> — 13 fuzzers × run IDs 0–9 (run inventory only)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>objcopy</strong> — 13 fuzzers × run IDs 0–9 (run inventory only)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>objdump</strong> — 13 fuzzers × run IDs 0–9 (run inventory only)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>php</strong> — 13 fuzzers × run IDs 0–9 (Magma measured)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>poppler</strong> — 13 fuzzers × run IDs 0–9 (Magma measured)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>re2</strong> — 13 fuzzers × run IDs 0–9 (run inventory only)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>readelf</strong> — 13 fuzzers × run IDs 0–9 (run inventory only)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>size</strong> — 13 fuzzers × run IDs 0–9 (run inventory only)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>sqlite</strong> — 13 fuzzers × run IDs 0–9 (Magma measured)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

<details>
<summary><strong>strip</strong> — 13 fuzzers × run IDs 0–9 (run inventory only)</summary>

| Fuzzer | Run IDs (0–9) |
| --- | --- |
| AFL | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFLFast | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| EcoFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| AFL-DiPri | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| Entropic | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-FE | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| P-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| E-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-F | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| PE-E | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |
| SEAFuzz | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` |

</details>

## Per-run Magma metrics (780 runs)

Each target contains 130 recorded runs (13 fuzzers × 10 run IDs). The full dataset includes bug IDs, crash IDs, timing information, and artifact references.

<details>
<summary><strong>libpng</strong> — 130 runs (13 fuzzers × 10 runs)</summary>

| Fuzzer | Run ID | Selected crashes | Actual crashes | Reached (tot/uni) | Triggered (tot/uni) | Time mode | Source root |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `3` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| AFL | `4` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| AFL | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `6` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| AFL | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `8` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| AFL | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `8` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| AFLFast | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| DiPri | `0` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `1` | 1 | 1 | 4/4 | 1/1 | relative_time | outputx_xinjia |
| DiPri | `2` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `3` | 8 | 8 | 4/4 | 1/1 | relative_time | outputx_xinjia |
| DiPri | `4` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `5` | 3 | 3 | 4/4 | 1/1 | relative_time | outputx_xinjia |
| DiPri | `6` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `7` | 14 | 14 | 4/4 | 1/1 | relative_time | outputx_xinjia |
| DiPri | `8` | 1 | 1 | 4/4 | 1/1 | relative_time | outputx_xinjia |
| DiPri | `9` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| AFL-DiPri | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `2` | 1 | 1 | 5/5 | 1/1 | unix_time | outputy |
| AFL-DiPri | `3` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| AFL-DiPri | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `7` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| AFL-DiPri | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| Entropic | `0` | 4 | 4 | 4/4 | 1/1 | unix_time | entropic |
| Entropic | `1` | 54 | 54 | 4/4 | 1/1 | unix_time | entropic |
| Entropic | `2` | 14 | 14 | 4/4 | 1/1 | unix_time | entropic |
| Entropic | `3` | 2 | 2 | 4/4 | 1/1 | unix_time | entropic |
| Entropic | `4` | 1 | 1 | 5/5 | 1/1 | unix_time | entropic |
| Entropic | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `6` | 17 | 17 | 4/4 | 1/1 | unix_time | entropic |
| Entropic | `7` | 1 | 1 | 4/4 | 1/1 | unix_time | entropic |
| Entropic | `8` | 4 | 4 | 5/5 | 1/1 | unix_time | entropic |
| Entropic | `9` | 8 | 8 | 4/4 | 1/1 | unix_time | entropic |
| P-FE | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `5` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| P-FE | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `0` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| E-FE | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `3` | 4 | 4 | 4/4 | 1/1 | unix_time | outputy |
| E-FE | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `6` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| E-FE | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `9` | 3 | 3 | 4/4 | 1/1 | unix_time | outputy |
| P-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `1` | 1 | 1 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| P-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `6` | 1 | 1 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| P-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `9` | 2 | 2 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| E-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `6` | 1 | 1 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| E-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `8` | 1 | 1 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| E-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `2` | 1 | 1 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `3` | 1 | 1 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `7` | 3 | 3 | 5/5 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `1` | 1 | 1 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `2` | 2 | 2 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `7` | 1 | 1 | 5/5 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `8` | 2 | 2 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `9` | 1 | 1 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| SEAFuzz | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `3` | 10 | 10 | 4/4 | 1/1 | unix_time | outputy |
| SEAFuzz | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |

</details>

<details>
<summary><strong>libsndfile</strong> — 130 runs (13 fuzzers × 10 runs)</summary>

| Fuzzer | Run ID | Selected crashes | Actual crashes | Reached (tot/uni) | Triggered (tot/uni) | Time mode | Source root |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | `0` | 53 | 53 | 4/4 | 4/4 | unix_time | outputy |
| AFL | `1` | 44 | 44 | 4/4 | 4/4 | unix_time | outputy |
| AFL | `2` | 45 | 45 | 4/4 | 4/4 | unix_time | outputy |
| AFL | `3` | 57 | 57 | 4/4 | 4/4 | unix_time | outputy |
| AFL | `4` | 48 | 48 | 4/4 | 4/4 | unix_time | outputy |
| AFL | `5` | 51 | 51 | 4/4 | 4/4 | unix_time | outputy |
| AFL | `6` | 51 | 51 | 4/4 | 4/4 | unix_time | outputy |
| AFL | `7` | 49 | 49 | 4/4 | 4/4 | unix_time | outputy |
| AFL | `8` | 45 | 45 | 4/4 | 4/4 | unix_time | outputy |
| AFL | `9` | 49 | 49 | 4/4 | 4/4 | unix_time | outputy |
| AFLFast | `0` | 53 | 53 | 4/4 | 4/4 | unix_time | outputy |
| AFLFast | `1` | 46 | 46 | 4/4 | 4/4 | unix_time | outputy |
| AFLFast | `2` | 51 | 51 | 4/4 | 4/4 | unix_time | outputy |
| AFLFast | `3` | 48 | 48 | 4/4 | 4/4 | unix_time | outputy |
| AFLFast | `4` | 41 | 41 | 4/4 | 4/4 | unix_time | outputy |
| AFLFast | `5` | 48 | 48 | 4/4 | 4/4 | unix_time | outputy |
| AFLFast | `6` | 51 | 51 | 4/4 | 4/4 | unix_time | outputy |
| AFLFast | `7` | 44 | 44 | 4/4 | 4/4 | unix_time | outputy |
| AFLFast | `8` | 40 | 40 | 4/4 | 4/4 | unix_time | outputy |
| AFLFast | `9` | 48 | 48 | 4/4 | 4/4 | unix_time | outputy |
| EcoFuzz | `0` | 33 | 33 | 4/4 | 4/4 | unix_time | outputy |
| EcoFuzz | `1` | 38 | 38 | 4/4 | 4/4 | unix_time | outputy |
| EcoFuzz | `2` | 34 | 34 | 4/4 | 4/4 | unix_time | outputy |
| EcoFuzz | `3` | 42 | 42 | 4/4 | 4/4 | unix_time | outputy |
| EcoFuzz | `4` | 31 | 31 | 4/4 | 4/4 | unix_time | outputy |
| EcoFuzz | `5` | 43 | 43 | 4/4 | 4/4 | unix_time | outputy |
| EcoFuzz | `6` | 41 | 41 | 4/4 | 4/4 | unix_time | outputy |
| EcoFuzz | `7` | 38 | 38 | 4/4 | 4/4 | unix_time | outputy |
| EcoFuzz | `8` | 51 | 51 | 4/4 | 4/4 | unix_time | outputy |
| EcoFuzz | `9` | 40 | 40 | 4/4 | 4/4 | unix_time | outputy |
| DiPri | `0` | 45 | 45 | 4/4 | 4/4 | relative_time | outputx_xinjia |
| DiPri | `1` | 46 | 46 | 4/4 | 4/4 | relative_time | outputx_xinjia |
| DiPri | `2` | 42 | 42 | 4/4 | 4/4 | relative_time | outputx_xinjia |
| DiPri | `3` | 42 | 42 | 4/4 | 4/4 | relative_time | outputx_xinjia |
| DiPri | `4` | 43 | 43 | 4/4 | 3/3 | relative_time | outputx_xinjia |
| DiPri | `5` | 39 | 39 | 4/4 | 4/4 | relative_time | outputx_xinjia |
| DiPri | `6` | 43 | 43 | 4/4 | 4/4 | relative_time | outputx_xinjia |
| DiPri | `7` | 46 | 46 | 4/4 | 4/4 | relative_time | outputx_xinjia |
| DiPri | `8` | 40 | 41 | 4/4 | 4/4 | relative_time | outputx_xinjia |
| DiPri | `9` | 41 | 41 | 4/4 | 4/4 | relative_time | outputx_xinjia |
| AFL-DiPri | `0` | 37 | 37 | 4/4 | 4/4 | unix_time | outputy |
| AFL-DiPri | `1` | 37 | 37 | 4/4 | 4/4 | unix_time | outputy |
| AFL-DiPri | `2` | 42 | 42 | 4/4 | 4/4 | unix_time | outputy |
| AFL-DiPri | `3` | 42 | 43 | 4/4 | 4/4 | unix_time | outputy |
| AFL-DiPri | `4` | 50 | 50 | 4/4 | 4/4 | unix_time | outputy |
| AFL-DiPri | `5` | 44 | 44 | 4/4 | 4/4 | unix_time | outputy |
| AFL-DiPri | `6` | 43 | 43 | 4/4 | 4/4 | unix_time | outputy |
| AFL-DiPri | `7` | 35 | 35 | 4/4 | 4/4 | unix_time | outputy |
| AFL-DiPri | `8` | 44 | 45 | 4/4 | 4/4 | unix_time | outputy |
| AFL-DiPri | `9` | 46 | 46 | 4/4 | 4/4 | unix_time | outputy |
| Entropic | `0` | 104 | 104 | 3/3 | 3/3 | unix_time | entropic |
| Entropic | `1` | 167 | 167 | 3/3 | 3/3 | unix_time | entropic |
| Entropic | `2` | 121 | 121 | 3/3 | 3/3 | unix_time | entropic |
| Entropic | `3` | 332 | 332 | 4/4 | 4/4 | unix_time | entropic |
| Entropic | `4` | 87 | 87 | 3/3 | 3/3 | unix_time | entropic |
| Entropic | `5` | 169 | 169 | 4/4 | 4/4 | unix_time | entropic |
| Entropic | `6` | 258 | 258 | 4/4 | 4/4 | unix_time | entropic |
| Entropic | `7` | 137 | 137 | 3/3 | 3/3 | unix_time | entropic |
| Entropic | `8` | 139 | 139 | 3/3 | 3/3 | unix_time | entropic |
| Entropic | `9` | 135 | 135 | 3/3 | 3/3 | unix_time | entropic |
| P-FE | `0` | 53 | 53 | 4/4 | 4/4 | unix_time | outputy |
| P-FE | `1` | 59 | 61 | 4/4 | 4/4 | unix_time | outputy |
| P-FE | `2` | 50 | 50 | 4/4 | 4/4 | unix_time | outputy |
| P-FE | `3` | 60 | 60 | 4/4 | 4/4 | unix_time | outputy |
| P-FE | `4` | 49 | 49 | 4/4 | 4/4 | unix_time | outputy |
| P-FE | `5` | 47 | 48 | 4/4 | 4/4 | unix_time | outputy |
| P-FE | `6` | 50 | 50 | 4/4 | 4/4 | unix_time | outputy |
| P-FE | `7` | 60 | 60 | 4/4 | 4/4 | unix_time | outputy |
| P-FE | `8` | 49 | 49 | 4/4 | 4/4 | unix_time | outputy |
| P-FE | `9` | 46 | 46 | 4/4 | 4/4 | unix_time | outputy |
| E-FE | `0` | 47 | 47 | 4/4 | 4/4 | unix_time | outputy |
| E-FE | `1` | 45 | 45 | 4/4 | 4/4 | unix_time | outputy |
| E-FE | `2` | 51 | 51 | 4/4 | 4/4 | unix_time | outputy |
| E-FE | `3` | 47 | 47 | 4/4 | 4/4 | unix_time | outputy |
| E-FE | `4` | 46 | 46 | 4/4 | 4/4 | unix_time | outputy |
| E-FE | `5` | 47 | 47 | 4/4 | 4/4 | unix_time | outputy |
| E-FE | `6` | 49 | 49 | 4/4 | 4/4 | unix_time | outputy |
| E-FE | `7` | 42 | 42 | 4/4 | 4/4 | unix_time | outputy |
| E-FE | `8` | 46 | 46 | 4/4 | 4/4 | unix_time | outputy |
| E-FE | `9` | 45 | 45 | 4/4 | 4/4 | unix_time | outputy |
| P-F | `0` | 55 | 55 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| P-F | `1` | 50 | 50 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| P-F | `2` | 55 | 55 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| P-F | `3` | 46 | 46 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| P-F | `4` | 50 | 50 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| P-F | `5` | 57 | 57 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| P-F | `6` | 67 | 67 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| P-F | `7` | 44 | 44 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| P-F | `8` | 47 | 47 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| P-F | `9` | 50 | 50 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| E-F | `0` | 52 | 52 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| E-F | `1` | 51 | 51 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| E-F | `2` | 51 | 51 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| E-F | `3` | 49 | 49 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| E-F | `4` | 56 | 56 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| E-F | `5` | 45 | 45 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| E-F | `6` | 43 | 43 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| E-F | `7` | 53 | 53 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| E-F | `8` | 37 | 37 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| E-F | `9` | 51 | 51 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-F | `0` | 47 | 47 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-F | `1` | 51 | 51 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-F | `2` | 55 | 55 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-F | `3` | 44 | 44 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-F | `4` | 38 | 38 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-F | `5` | 39 | 39 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-F | `6` | 48 | 48 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-F | `7` | 47 | 47 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-F | `8` | 56 | 56 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-F | `9` | 56 | 56 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-E | `0` | 46 | 46 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-E | `1` | 54 | 54 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-E | `2` | 40 | 40 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-E | `3` | 53 | 53 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-E | `4` | 42 | 42 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-E | `5` | 48 | 48 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-E | `6` | 43 | 43 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-E | `7` | 48 | 48 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-E | `8` | 40 | 40 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| PE-E | `9` | 51 | 51 | 4/4 | 4/4 | unix_time | outputx_xinjia |
| SEAFuzz | `0` | 48 | 48 | 4/4 | 4/4 | unix_time | outputy |
| SEAFuzz | `1` | 49 | 49 | 4/4 | 4/4 | unix_time | outputy |
| SEAFuzz | `2` | 53 | 54 | 4/4 | 4/4 | unix_time | outputy |
| SEAFuzz | `3` | 54 | 54 | 4/4 | 4/4 | unix_time | outputy |
| SEAFuzz | `4` | 57 | 57 | 4/4 | 4/4 | unix_time | outputy |
| SEAFuzz | `5` | 43 | 43 | 4/4 | 4/4 | unix_time | outputy |
| SEAFuzz | `6` | 52 | 52 | 4/4 | 4/4 | unix_time | outputy |
| SEAFuzz | `7` | 51 | 51 | 4/4 | 4/4 | unix_time | outputy |
| SEAFuzz | `8` | 50 | 50 | 4/4 | 4/4 | unix_time | outputy |
| SEAFuzz | `9` | 48 | 48 | 4/4 | 4/4 | unix_time | outputy |

</details>

<details>
<summary><strong>lua</strong> — 130 runs (13 fuzzers × 10 runs)</summary>

| Fuzzer | Run ID | Selected crashes | Actual crashes | Reached (tot/uni) | Triggered (tot/uni) | Time mode | Source root |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | `0` | 2 | 2 | 2/2 | 1/1 | unix_time | outputy |
| AFL | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `3` | 4 | 4 | 3/3 | 1/1 | unix_time | outputy |
| AFL | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `5` | 2 | 2 | 2/2 | 1/1 | unix_time | outputy |
| AFL | `6` | 2 | 2 | 2/2 | 1/1 | unix_time | outputy |
| AFL | `7` | 2 | 2 | 2/2 | 1/1 | unix_time | outputy |
| AFL | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `9` | 1 | 1 | 2/2 | 1/1 | unix_time | outputy |
| AFLFast | `0` | 2 | 2 | 2/2 | 1/1 | unix_time | outputy |
| AFLFast | `1` | 2 | 2 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `2` | 1 | 1 | 2/2 | 1/1 | unix_time | outputy |
| AFLFast | `3` | 5 | 5 | 2/2 | 1/1 | unix_time | outputy |
| AFLFast | `4` | 1 | 1 | 2/2 | 1/1 | unix_time | outputy |
| AFLFast | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `6` | 2 | 2 | 2/2 | 1/1 | unix_time | outputy |
| AFLFast | `7` | 2 | 2 | 2/2 | 1/1 | unix_time | outputy |
| AFLFast | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| DiPri | `0` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `1` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `2` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `3` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `4` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `5` | 1 | 1 | 2/2 | 1/1 | relative_time | outputx_xinjia |
| DiPri | `6` | 2 | 2 | 2/2 | 1/1 | relative_time | outputx_xinjia |
| DiPri | `7` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `8` | 1 | 1 | 2/2 | 1/1 | relative_time | outputx_xinjia |
| DiPri | `9` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| AFL-DiPri | `0` | 2 | 2 | 2/2 | 1/1 | unix_time | outputy |
| AFL-DiPri | `1` | 9 | 9 | 2/2 | 1/1 | unix_time | outputy |
| AFL-DiPri | `2` | 5 | 5 | 2/2 | 1/1 | unix_time | outputy |
| AFL-DiPri | `3` | 5 | 5 | 2/2 | 1/1 | unix_time | outputy |
| AFL-DiPri | `4` | 9 | 9 | 2/2 | 1/1 | unix_time | outputy |
| AFL-DiPri | `5` | 5 | 5 | 2/2 | 1/1 | unix_time | outputy |
| AFL-DiPri | `6` | 6 | 6 | 2/2 | 1/1 | unix_time | outputy |
| AFL-DiPri | `7` | 3 | 3 | 2/2 | 1/1 | unix_time | outputy |
| AFL-DiPri | `8` | 1 | 1 | 2/2 | 1/1 | unix_time | outputy |
| AFL-DiPri | `9` | 13 | 13 | 3/3 | 1/1 | unix_time | outputy |
| Entropic | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| P-FE | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `1` | 4 | 4 | 2/2 | 1/1 | unix_time | outputy |
| P-FE | `2` | 1 | 1 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `4` | 7 | 8 | 2/2 | 1/1 | unix_time | outputy |
| P-FE | `5` | 4 | 4 | 2/2 | 1/1 | unix_time | outputy |
| P-FE | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `7` | 6 | 6 | 2/2 | 1/1 | unix_time | outputy |
| P-FE | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `9` | 11 | 12 | 2/2 | 1/1 | unix_time | outputy |
| E-FE | `0` | 0 | 1 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `1` | 1 | 1 | 2/2 | 1/1 | unix_time | outputy |
| E-FE | `2` | 3 | 3 | 2/2 | 1/1 | unix_time | outputy |
| E-FE | `3` | 3 | 3 | 3/3 | 1/1 | unix_time | outputy |
| E-FE | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `5` | 5 | 5 | 2/2 | 1/1 | unix_time | outputy |
| E-FE | `6` | 1 | 2 | 2/2 | 1/1 | unix_time | outputy |
| E-FE | `7` | 3 | 3 | 2/2 | 1/1 | unix_time | outputy |
| E-FE | `8` | 10 | 10 | 2/2 | 1/1 | unix_time | outputy |
| E-FE | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `1` | 5 | 5 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| P-F | `2` | 2 | 2 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| P-F | `3` | 5 | 5 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| P-F | `4` | 10 | 10 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| P-F | `5` | 1 | 1 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| P-F | `6` | 2 | 2 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| P-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `9` | 1 | 1 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| E-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `1` | 1 | 1 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| E-F | `2` | 4 | 4 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| E-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `4` | 2 | 2 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| E-F | `5` | 1 | 1 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| E-F | `6` | 4 | 4 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| E-F | `7` | 1 | 1 | 1/1 | 1/1 | unix_time | outputx_xinjia |
| E-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `9` | 1 | 1 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `0` | 1 | 1 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `1` | 1 | 2 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `3` | 4 | 4 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `4` | 3 | 3 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `5` | 1 | 1 | 1/1 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `7` | 5 | 7 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `8` | 6 | 6 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `0` | 1 | 1 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `1` | 9 | 9 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `2` | 1 | 1 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `3` | 2 | 2 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `4` | 4 | 4 | 3/3 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `5` | 8 | 8 | 3/3 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `6` | 3 | 3 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `7` | 2 | 2 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `8` | 2 | 2 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| PE-E | `9` | 1 | 1 | 2/2 | 1/1 | unix_time | outputx_xinjia |
| SEAFuzz | `0` | 3 | 4 | 2/2 | 1/1 | unix_time | outputy |
| SEAFuzz | `1` | 2 | 2 | 2/2 | 1/1 | unix_time | outputy |
| SEAFuzz | `2` | 1 | 1 | 2/2 | 1/1 | unix_time | outputy |
| SEAFuzz | `3` | 10 | 10 | 2/2 | 1/1 | unix_time | outputy |
| SEAFuzz | `4` | 3 | 3 | 1/1 | 1/1 | unix_time | outputy |
| SEAFuzz | `5` | 3 | 3 | 2/2 | 1/1 | unix_time | outputy |
| SEAFuzz | `6` | 4 | 4 | 3/3 | 1/1 | unix_time | outputy |
| SEAFuzz | `7` | 11 | 11 | 3/3 | 1/1 | unix_time | outputy |
| SEAFuzz | `8` | 11 | 11 | 2/2 | 1/1 | unix_time | outputy |
| SEAFuzz | `9` | 2 | 2 | 2/2 | 1/1 | unix_time | outputy |

</details>

<details>
<summary><strong>php</strong> — 130 runs (13 fuzzers × 10 runs)</summary>

| Fuzzer | Run ID | Selected crashes | Actual crashes | Reached (tot/uni) | Triggered (tot/uni) | Time mode | Source root |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| DiPri | `0` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `1` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `2` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `3` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `4` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `5` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `6` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `7` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `8` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `9` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| AFL-DiPri | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| Entropic | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| P-FE | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| SEAFuzz | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |

</details>

<details>
<summary><strong>poppler</strong> — 130 runs (13 fuzzers × 10 runs)</summary>

| Fuzzer | Run ID | Selected crashes | Actual crashes | Reached (tot/uni) | Triggered (tot/uni) | Time mode | Source root |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| DiPri | `0` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `1` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `2` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `3` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `4` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `5` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `6` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `7` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `8` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `9` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| AFL-DiPri | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| Entropic | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| P-FE | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `3` | 1 | 1 | 4/4 | 1/1 | unix_time | outputx_xinjia |
| PE-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| SEAFuzz | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `2` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| SEAFuzz | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `4` | 1 | 1 | 4/4 | 1/1 | unix_time | outputy |
| SEAFuzz | `5` | 2 | 2 | 5/5 | 1/1 | unix_time | outputy |
| SEAFuzz | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |

</details>

<details>
<summary><strong>sqlite</strong> — 130 runs (13 fuzzers × 10 runs)</summary>

| Fuzzer | Run ID | Selected crashes | Actual crashes | Reached (tot/uni) | Triggered (tot/uni) | Time mode | Source root |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFLFast | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| EcoFuzz | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| DiPri | `0` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `1` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `2` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `3` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `4` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `5` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `6` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `7` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `8` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| DiPri | `9` | 0 | 0 | 0/0 | 0/0 | relative_time | outputx_xinjia |
| AFL-DiPri | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| AFL-DiPri | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| Entropic | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| Entropic | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | entropic |
| P-FE | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-FE | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| E-FE | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| P-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| P-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| E-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-F | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| PE-E | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputx_xinjia |
| SEAFuzz | `0` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `1` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `2` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `3` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `4` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `5` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `6` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `7` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `8` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
| SEAFuzz | `9` | 0 | 0 | 0/0 | 0/0 | unix_time | outputy |
