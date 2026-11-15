# Implementation and baseline map

This file maps the method names used in the paper to their implementation directories. Detailed source versions, local modifications, build and run instructions, configuration options, and other reproducibility information are maintained in two dedicated inventories:

- [Source implementations](../src/README.md): SEAFuzz and the AFL 2.57b port of DiPri, including ablation controls and parameter defaults.
- [Baseline implementations](../baselines/README.md): AFL, AFLFast, EcoFuzz, AFL++-DiPri, and Entropic, including upstream revisions, local changes, and licensing information.

## Method-to-source mapping

| Paper method | Source directory | Description |
| --- | --- | --- |
| SEAFuzz | `src/SEAFuzz/` | Proposed method (complete configuration). |
| AFL | `baselines/AFL/` | AFL 2.57b baseline. |
| AFLFast | `baselines/AFLFast/` | AFLFast baseline. |
| EcoFuzz | `baselines/EcoFuzz/EcoFuzz/` | EcoFuzz baseline. |
| AFL-DiPri | `src/AFL-DiPri/` | Local DiPri port to AFL 2.57b. |
| DiPri | `baselines/DiPri/` | AFL++-based DiPri implementation. |
| Entropic | `baselines/Entropic/` | libFuzzer with the Entropic schedule (`-entropic=1`). |

These are the method names used in the paper and explanatory tables.

## Important distinctions

- **SEAFuzz** builds on AFL 2.57b and combines path-frequency and seed-entropy feedback for fast-track seed scheduling and adaptive energy allocation. Some inherited source comments still refer to `RETAFL`.
- **AFL-DiPri and DiPri are distinct implementations.** `AFL-DiPri` is the local AFL 2.57b port; `DiPri` uses AFL++ 4.06c. Both were run with **Adaptive + Hamming** in the experiments, although the AFL++ version defaults to **Vanilla + Hamming**. 
- **Entropic is a libFuzzer baseline**, not an AFL implementation or the entropy-feedback ablation of SEAFuzz. Its local fork-mode and statistics changes are documented in the baseline inventory.
