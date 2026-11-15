# UniFuzz — Unique Crash Signature Results

> SEAFuzz evaluation data · 16 programs · 13 fuzzers · 10 out directories per fuzzer

## Overview

| Item | Value |
| --- | --- |
| Programs | **16** |
| Fuzzers per program | **13** |
| Out directories per program/fuzzer | **10** |
| Distinct program × fuzzer × out combinations | **2,080** |
| Program summary rows | **16** |
| Fuzzer summary rows | **208** |
| Additional libpng variant | Excluded |

**Metric notation:** `tot` is the sum of per-run unique crash signature counts; `uni` is the number of distinct crash signatures across runs. BugKey definition: `ASAN|error_type|frame0|frame1|frame2`; fallback: `GDB|signal|frame0|frame1|frame2`. These are **crash signature keys**, not independently verified distinct vulnerabilities.

**Data integrity note:** The source reports **11** runs for `strip / SEAFuzz`, but the out manifest lists **10** out directories. The source run count was kept unchanged, and the out list preserves the 10 provided directory names.

## Per-program summary

| Program | Fuzzers | Reported runs | Selected crashes | Classified | ASAN | GDB | Unclassified | Total (tot) | Unique (uni) | Consistency |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `bloaty` | 13 | 130 | 149 | 149 | 149 | 0 | 0 | 83 | **1** | 0.638462 |
| `cxxfilt` | 13 | 130 | 5374 | 93 | 93 | 0 | 5281 | 44 | **2** | 0.169231 |
| as-new (`gas`) | 13 | 130 | 1562 | 238 | 0 | 238 | 1324 | 152 | **5** | 0.233846 |
| `libpng` | 13 | 130 | 178 | 178 | 178 | 0 | 0 | 41 | **1** | 0.315385 |
| `libsndfile` | 13 | 130 | 7297 | 6956 | 6770 | 186 | 341 | 945 | **9** | 0.807692 |
| `lua` | 13 | 130 | 293 | 217 | 217 | 0 | 76 | 73 | **1** | 0.561538 |
| `nm` | 13 | 130 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | 0.000000 |
| `objcopy` | 13 | 130 | 1405 | 0 | 0 | 0 | 1405 | 0 | **0** | 0.000000 |
| `objdump` | 13 | 130 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | 0.000000 |
| `php` | 13 | 130 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | 0.000000 |
| `poppler` | 13 | 130 | 5 | 5 | 5 | 0 | 0 | 4 | **1** | 0.030769 |
| `re2` | 13 | 130 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | 0.000000 |
| `readelf` | 13 | 130 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | 0.000000 |
| `size` | 13 | 130 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | 0.000000 |
| `sqlite` | 13 | 130 | 0 | 0 | 0 | 0 | 0 | 0 | **0** | 0.000000 |
| `strip` | 13 | 131 | 1214 | 0 | 0 | 0 | 1214 | 0 | **0** | 0.000000 |

## Unique crash signatures by fuzzer and program

Each cell is the `uni` value from the corresponding `FUZZER_SUMMARY`. It is intentionally **not** the number of raw crash files.

| Program | AFL | AFLFast | EcoFuzz | DiPri | AFL-DiPri | Entropic | P-FE | E-FE | P-F | E-F | PE-F | PE-E | SEAFuzz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `bloaty` | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `cxxfilt` | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| as-new (`gas`) | 4 | 0 | 3 | 0 | 4 | 1 | 4 | 4 | 4 | 4 | 3 | 4 | 4 |
| `libpng` | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `libsndfile` | 8 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| `lua` | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `nm` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `objcopy` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `objdump` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `php` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `poppler` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| `re2` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `readelf` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `size` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `sqlite` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `strip` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Detailed fuzzer statistics and out directory mapping

Expand a program to see the original source counters and the exact ten out directory names. The complete crash signature keys are listed in the collapsed signature section for each program and preserved in the lossless archive below.

<details>
<summary><strong>bloaty</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 9 | 9 | 9 | 0 | 0 | 7 | 1 | 0.700000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out5`, `out6`, `out7`, `out8`, `out9`, `out11` |
| AFLFast | 10 | 5 | 5 | 5 | 0 | 0 | 4 | 1 | 0.400000 | 1.000000 | `out0`, `out1`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| EcoFuzz | 10 | 3 | 3 | 3 | 0 | 0 | 3 | 1 | 0.300000 | 1.000000 | `out0`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| DiPri | 10 | 8 | 8 | 8 | 0 | 0 | 6 | 1 | 0.600000 | 1.000000 | `out0`, `out1`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| AFL-DiPri | 10 | 18 | 18 | 18 | 0 | 0 | 9 | 1 | 0.900000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10` |
| Entropic | 10 | 9 | 9 | 9 | 0 | 0 | 3 | 1 | 0.300000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 10 | 10 | 10 | 0 | 0 | 5 | 1 | 0.500000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| E-FE | 10 | 14 | 14 | 14 | 0 | 0 | 8 | 1 | 0.800000 | 1.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 21 | 21 | 21 | 0 | 0 | 10 | 1 | 1.000000 | 1.000000 | `out0`, `out1`, `out6`, `out8`, `out9`, `out10`, `out12`, `out13`, `out14`, `out17` |
| E-F | 10 | 13 | 13 | 13 | 0 | 0 | 9 | 1 | 0.900000 | 1.000000 | `out0`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out12`, `out15`, `out16` |
| PE-F | 10 | 10 | 10 | 10 | 0 | 0 | 5 | 1 | 0.500000 | 1.000000 | `out0`, `out1`, `out6`, `out8`, `out11`, `out12`, `out17`, `out18`, `out22`, `out23` |
| PE-E | 10 | 13 | 13 | 13 | 0 | 0 | 7 | 1 | 0.700000 | 1.000000 | `out6`, `out7`, `out8`, `out9`, `out12`, `out13`, `out15`, `out20`, `out22`, `out23` |
| SEAFuzz | 10 | 16 | 16 | 16 | 0 | 0 | 7 | 1 | 0.700000 | 1.000000 | `out1`, `out3`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11`, `out12`, `out13` |

<details>
<summary>View program-wide unique BugKey signatures</summary>

```text
ASAN|SEGV|__gnu_cxx::__normal_iterator<bloaty::dwarf::AbbrevTable::Attribute const*, std::vector<bloaty::dwarf::AbbrevTable::Attribute, std::allocator<bloaty::dwarf::AbbrevTable::Attribute> > >::__normal_iterator(bloaty::dwarf::AbbrevTable::Attribute const* const&)|pthread_create|std::thread::_M_start_thread(std::unique_ptr<std::thread::_State, std::default_delete<std::thread::_State> >, void
```

</details>

</details>

<details>
<summary><strong>cxxfilt</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 2 | 2 | 2 | 0 | 0 | 2 | 1 | 0.200000 | 1.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out11` |
| AFLFast | 10 | 9 | 9 | 9 | 0 | 0 | 6 | 1 | 0.600000 | 1.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10`, `out11` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out11` |
| AFL-DiPri | 10 | 3 | 3 | 3 | 0 | 0 | 3 | 1 | 0.300000 | 1.000000 | `out0`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| Entropic | 10 | 5281 | 0 | 0 | 0 | 5281 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 8 | 8 | 8 | 0 | 0 | 6 | 1 | 0.600000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10` |
| E-FE | 10 | 10 | 10 | 10 | 0 | 0 | 4 | 1 | 0.400000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out8`, `out9`, `out10` |
| P-F | 10 | 13 | 13 | 13 | 0 | 0 | 6 | 2 | 0.300000 | 1.000000 | `out0`, `out3`, `out4`, `out5`, `out6`, `out9`, `out10`, `out11`, `out15`, `out17` |
| E-F | 10 | 8 | 8 | 8 | 0 | 0 | 4 | 1 | 0.400000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out8`, `out10`, `out13`, `out14`, `out15` |
| PE-F | 10 | 17 | 17 | 17 | 0 | 0 | 5 | 1 | 0.500000 | 1.000000 | `out0`, `out3`, `out4`, `out5`, `out7`, `out11`, `out13`, `out18`, `out20`, `out22` |
| PE-E | 10 | 7 | 7 | 7 | 0 | 0 | 3 | 1 | 0.300000 | 1.000000 | `out3`, `out4`, `out5`, `out8`, `out9`, `out13`, `out17`, `out18`, `out20`, `out21` |
| SEAFuzz | 10 | 16 | 16 | 16 | 0 | 0 | 5 | 1 | 0.500000 | 1.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out8`, `out9`, `out10`, `out13`, `out14` |

<details>
<summary>View program-wide unique BugKey signatures</summary>

```text
ASAN|SEGV|d_lookup_template_argument|d_find_pack|d_args_length
ASAN|SEGV|d_lookup_template_argument|d_find_pack|d_print_comp_inner
```

</details>

</details>

<details>
<summary><strong>gas (as-new)</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 35 | 35 | 0 | 35 | 0 | 21 | 4 | 0.525000 | 1.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out9`, `out10`, `out11` |
| AFLFast | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10`, `out11` |
| EcoFuzz | 10 | 4 | 4 | 0 | 4 | 0 | 3 | 3 | 0.100000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out5`, `out7`, `out8`, `out9`, `out10`, `out11` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out11` |
| AFL-DiPri | 10 | 38 | 38 | 0 | 38 | 0 | 20 | 4 | 0.500000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out7`, `out8`, `out9`, `out10`, `out11` |
| Entropic | 10 | 1330 | 6 | 0 | 6 | 1324 | 2 | 1 | 0.200000 | 0.004511 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 9 | 9 | 0 | 9 | 0 | 9 | 4 | 0.225000 | 1.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| E-FE | 10 | 20 | 20 | 0 | 20 | 0 | 17 | 4 | 0.425000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 15 | 15 | 0 | 15 | 0 | 12 | 4 | 0.300000 | 1.000000 | `out0`, `out1`, `out3`, `out6`, `out7`, `out8`, `out10`, `out11`, `out16`, `out17` |
| E-F | 10 | 26 | 26 | 0 | 26 | 0 | 17 | 4 | 0.425000 | 1.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out9`, `out11`, `out12`, `out15` |
| PE-F | 10 | 23 | 23 | 0 | 23 | 0 | 15 | 3 | 0.500000 | 1.000000 | `out3`, `out4`, `out5`, `out6`, `out11`, `out14`, `out20`, `out21`, `out22`, `out23` |
| PE-E | 10 | 23 | 23 | 0 | 23 | 0 | 16 | 4 | 0.400000 | 1.000000 | `out1`, `out2`, `out6`, `out15`, `out16`, `out17`, `out18`, `out19`, `out22`, `out23` |
| SEAFuzz | 10 | 39 | 39 | 0 | 39 | 0 | 20 | 4 | 0.500000 | 1.000000 | `out0`, `out3`, `out5`, `out8`, `out9`, `out10`, `out11`, `out12`, `out13`, `out14` |

<details>
<summary>View program-wide unique BugKey signatures</summary>

```text
GDB|SIGSEGV|__asan_memcpy|snapshot_symbol|resolve_expression
GDB|SIGSEGV|expr|operand|expr
GDB|SIGSEGV|operand|expr|operand
GDB|SIGSEGV|operand|operand|operand
GDB|SIGSEGV|resolve_symbol_value|resolve_symbol_value|sframe_estimate_size_before_relax
```

</details>

</details>

<details>
<summary><strong>libpng</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 4 | 4 | 4 | 0 | 0 | 4 | 1 | 0.400000 | 1.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| AFLFast | 10 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0.100000 | 1.000000 | `out0`, `out1`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| DiPri | 10 | 27 | 27 | 27 | 0 | 0 | 5 | 1 | 0.500000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| AFL-DiPri | 10 | 3 | 3 | 3 | 0 | 0 | 3 | 1 | 0.300000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| Entropic | 10 | 105 | 105 | 105 | 0 | 0 | 9 | 1 | 0.900000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0.100000 | 1.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| E-FE | 10 | 9 | 9 | 9 | 0 | 0 | 4 | 1 | 0.400000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 4 | 4 | 4 | 0 | 0 | 3 | 1 | 0.300000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out5`, `out6`, `out7`, `out8`, `out9`, `out11` |
| E-F | 10 | 2 | 2 | 2 | 0 | 0 | 2 | 1 | 0.200000 | 1.000000 | `out0`, `out1`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| PE-F | 10 | 5 | 5 | 5 | 0 | 0 | 3 | 1 | 0.300000 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out6`, `out8`, `out14`, `out16`, `out17`, `out23` |
| PE-E | 10 | 7 | 7 | 7 | 0 | 0 | 5 | 1 | 0.500000 | 1.000000 | `out0`, `out5`, `out10`, `out13`, `out15`, `out16`, `out18`, `out20`, `out22`, `out23` |
| SEAFuzz | 10 | 10 | 10 | 10 | 0 | 0 | 1 | 1 | 0.100000 | 1.000000 | `out0`, `out2`, `out4`, `out6`, `out7`, `out8`, `out9`, `out11`, `out12`, `out13` |

<details>
<summary>View program-wide unique BugKey signatures</summary>

```text
ASAN|SEGV|png_do_expand_palette|png_do_read_transformations|png_read_row
```

</details>

</details>

<details>
<summary><strong>libsndfile</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 492 | 460 | 454 | 6 | 32 | 68 | 8 | 0.850000 | 0.934959 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out8`, `out9`, `out10` |
| AFLFast | 10 | 470 | 428 | 424 | 4 | 42 | 67 | 8 | 0.837500 | 0.910638 | `out0`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out9`, `out10`, `out11` |
| EcoFuzz | 10 | 391 | 352 | 342 | 10 | 39 | 75 | 9 | 0.833333 | 0.900256 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out8`, `out9`, `out10` |
| DiPri | 10 | 427 | 427 | 415 | 12 | 0 | 69 | 9 | 0.766667 | 1.000000 | `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| AFL-DiPri | 10 | 420 | 420 | 408 | 12 | 0 | 73 | 9 | 0.811111 | 1.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| Entropic | 10 | 1649 | 1421 | 1379 | 42 | 228 | 66 | 9 | 0.733333 | 0.861734 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 523 | 523 | 509 | 14 | 0 | 77 | 9 | 0.855556 | 1.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out8`, `out9`, `out10` |
| E-FE | 10 | 465 | 465 | 449 | 16 | 0 | 75 | 9 | 0.833333 | 1.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 521 | 521 | 502 | 19 | 0 | 77 | 9 | 0.855556 | 1.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10`, `out11` |
| E-F | 10 | 488 | 488 | 472 | 16 | 0 | 72 | 9 | 0.800000 | 1.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10`, `out11` |
| PE-F | 10 | 481 | 481 | 466 | 15 | 0 | 75 | 9 | 0.833333 | 1.000000 | `out1`, `out2`, `out3`, `out8`, `out11`, `out12`, `out14`, `out16`, `out18`, `out22` |
| PE-E | 10 | 465 | 465 | 453 | 12 | 0 | 73 | 9 | 0.811111 | 1.000000 | `out2`, `out3`, `out4`, `out6`, `out12`, `out15`, `out16`, `out18`, `out19`, `out21` |
| SEAFuzz | 10 | 505 | 505 | 497 | 8 | 0 | 78 | 9 | 0.866667 | 1.000000 | `out0`, `out1`, `out3`, `out4`, `out6`, `out7`, `out9`, `out11`, `out12`, `out14` |

<details>
<summary>View program-wide unique BugKey signatures</summary>

```text
ASAN|FPE|paf_read_header|paf_open|psf_open_file
ASAN|SEGV|wavlike_read_fmt_chunk|rf64_read_header|rf64_open
ASAN|SEGV|wavlike_read_fmt_chunk|wav_read_header|wav_open
ASAN|global-buffer-overflow|__asan_memcpy|memcpy|aiff_read_chanmap
ASAN|heap-buffer-overflow|__asan_memset|calloc|memset
ASAN|heap-buffer-overflow|calloc|wavlike_read_fmt_chunk|rf64_read_header
ASAN|heap-buffer-overflow|calloc|wavlike_read_fmt_chunk|wav_read_header
ASAN|negative-size-param|__asan_memset|calloc|memset
GDB|SIGABRT|__asan::AsanCheckFailed(char const*, int, char const*, unsigned long long, unsigned long long)|__sanitizer::CheckFailed(char const*, int, char const*, unsigned long long, unsigned long long)|__asan::GetShadowAddressInformation(unsigned long, __asan::ShadowAddressDescription*)
```

</details>

</details>

<details>
<summary><strong>lua</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 13 | 8 | 8 | 0 | 5 | 5 | 1 | 0.500000 | 0.615385 | `out0`, `out1`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10`, `out11` |
| AFLFast | 10 | 15 | 9 | 9 | 0 | 6 | 5 | 1 | 0.500000 | 0.600000 | `out0`, `out1`, `out2`, `out3`, `out5`, `out6`, `out7`, `out9`, `out10`, `out11` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out9`, `out10`, `out11` |
| DiPri | 10 | 4 | 4 | 4 | 0 | 0 | 3 | 1 | 0.300000 | 1.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out11` |
| AFL-DiPri | 10 | 58 | 48 | 48 | 0 | 10 | 10 | 1 | 1.000000 | 0.827586 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10` |
| Entropic | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| P-FE | 10 | 33 | 24 | 24 | 0 | 9 | 5 | 1 | 0.500000 | 0.727273 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| E-FE | 10 | 26 | 15 | 15 | 0 | 11 | 7 | 1 | 0.700000 | 0.576923 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10` |
| P-F | 10 | 26 | 21 | 21 | 0 | 5 | 6 | 1 | 0.600000 | 0.807692 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out9`, `out11` |
| E-F | 10 | 14 | 9 | 9 | 0 | 5 | 5 | 1 | 0.500000 | 0.642857 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out9`, `out10`, `out11` |
| PE-F | 10 | 21 | 16 | 16 | 0 | 5 | 7 | 1 | 0.700000 | 0.761905 | `out5`, `out8`, `out10`, `out12`, `out14`, `out15`, `out16`, `out20`, `out21`, `out23` |
| PE-E | 10 | 33 | 29 | 29 | 0 | 4 | 10 | 1 | 1.000000 | 0.878788 | `out0`, `out1`, `out2`, `out6`, `out7`, `out12`, `out14`, `out15`, `out17`, `out18` |
| SEAFuzz | 10 | 50 | 34 | 34 | 0 | 16 | 10 | 1 | 1.000000 | 0.680000 | `out2`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11`, `out13`, `out14` |

<details>
<summary>View program-wide unique BugKey signatures</summary>

```text
ASAN|SEGV|changedline|luaG_traceexec|luaV_execute
```

</details>

</details>

<details>
<summary><strong>nm</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out11` |
| AFLFast | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out8`, `out9`, `out10`, `out11` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| AFL-DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10` |
| Entropic | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| E-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out3`, `out5`, `out6`, `out8`, `out9`, `out10`, `out13`, `out15`, `out16` |
| E-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out3`, `out4`, `out5`, `out8`, `out10`, `out11`, `out13`, `out15`, `out17` |
| PE-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out4`, `out9`, `out11`, `out15`, `out17`, `out20`, `out21` |
| PE-E | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out2`, `out3`, `out5`, `out6`, `out11`, `out12`, `out13`, `out14`, `out15`, `out16` |
| SEAFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out9`, `out10`, `out14` |

</details>

<details>
<summary><strong>objcopy</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 538 | 0 | 0 | 0 | 538 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10`, `out11` |
| AFLFast | 10 | 527 | 0 | 0 | 0 | 527 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out11` |
| EcoFuzz | 10 | 340 | 0 | 0 | 0 | 340 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out11` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10`, `out11` |
| AFL-DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10`, `out11` |
| Entropic | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out9`, `out10` |
| E-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out9`, `out10` |
| P-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out8`, `out9`, `out11`, `out14`, `out15`, `out16`, `out17` |
| E-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out2`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10`, `out12`, `out13`, `out17` |
| PE-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out5`, `out12`, `out14`, `out15`, `out17`, `out18`, `out19`, `out20` |
| PE-E | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out5`, `out6`, `out7`, `out9`, `out10`, `out15`, `out17`, `out19`, `out22`, `out23` |
| SEAFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out9`, `out10`, `out11` |

</details>

<details>
<summary><strong>objdump</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10` |
| AFLFast | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out11` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10` |
| AFL-DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out8`, `out9`, `out10`, `out11` |
| Entropic | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out9`, `out10` |
| E-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out4`, `out5`, `out6`, `out8`, `out10`, `out11`, `out12`, `out13`, `out14` |
| E-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out3`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11`, `out14`, `out17` |
| PE-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out5`, `out6`, `out9`, `out10`, `out14`, `out15`, `out17` |
| PE-E | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out4`, `out6`, `out11`, `out13`, `out14`, `out16`, `out17`, `out22`, `out23` |
| SEAFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out8`, `out9`, `out10`, `out12`, `out13`, `out14` |

</details>

<details>
<summary><strong>php</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out5`, `out6`, `out7`, `out9`, `out10`, `out11` |
| AFLFast | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out11` |
| AFL-DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10` |
| Entropic | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| E-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out11` |
| E-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| PE-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out3`, `out9`, `out11`, `out12`, `out14`, `out16`, `out17`, `out20`, `out21` |
| PE-E | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out3`, `out4`, `out6`, `out8`, `out11`, `out19`, `out20`, `out21` |
| SEAFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out4`, `out6`, `out7`, `out9`, `out10`, `out11`, `out12`, `out13`, `out14` |

</details>

<details>
<summary><strong>poppler</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| AFLFast | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out10`, `out11` |
| AFL-DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| Entropic | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out9`, `out10` |
| E-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out9`, `out10`, `out11` |
| E-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out9`, `out10`, `out11` |
| PE-F | 10 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0.100000 | 1.000000 | `out0`, `out3`, `out4`, `out5`, `out6`, `out8`, `out11`, `out17`, `out18`, `out19` |
| PE-E | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out3`, `out4`, `out8`, `out9`, `out11`, `out13`, `out16`, `out18`, `out21`, `out23` |
| SEAFuzz | 10 | 4 | 4 | 4 | 0 | 0 | 3 | 1 | 0.300000 | 1.000000 | `out0`, `out1`, `out2`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10`, `out13` |

<details>
<summary>View program-wide unique BugKey signatures</summary>

```text
ASAN|SEGV|SplashOutputDev::type3D1(GfxState*, double, double, double, double, double, double)|Gfx::execOp(Object*, Object*, int)|Gfx::go(bool)
```

</details>

</details>

<details>
<summary><strong>re2</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out10`, `out11` |
| AFLFast | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10`, `out11` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out11` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| AFL-DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| Entropic | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out8`, `out9`, `out10` |
| E-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out6`, `out7`, `out9`, `out10`, `out11`, `out12`, `out13` |
| E-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out7`, `out8`, `out9`, `out11`, `out12`, `out15`, `out16` |
| PE-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out6`, `out7`, `out13`, `out14`, `out15`, `out19`, `out23` |
| PE-E | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out4`, `out9`, `out14`, `out15`, `out18`, `out20`, `out22`, `out23` |
| SEAFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out10`, `out12` |

</details>

<details>
<summary><strong>readelf</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out9`, `out10`, `out11` |
| AFLFast | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out8`, `out9`, `out11` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out8`, `out9`, `out10`, `out11` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out10`, `out11` |
| AFL-DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10`, `out11` |
| Entropic | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| E-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out4`, `out6`, `out10`, `out11`, `out13`, `out14`, `out15`, `out17` |
| E-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out7`, `out10`, `out11`, `out13`, `out15`, `out16` |
| PE-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out7`, `out11`, `out12`, `out13`, `out18`, `out19`, `out21`, `out22`, `out23` |
| PE-E | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out3`, `out4`, `out6`, `out12`, `out14`, `out19`, `out20`, `out22`, `out23` |
| SEAFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out10`, `out11`, `out13`, `out14` |

</details>

<details>
<summary><strong>size</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| AFLFast | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10`, `out11` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out11` |
| AFL-DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| Entropic | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| P-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| E-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out7`, `out9`, `out10`, `out11`, `out12`, `out14` |
| E-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out4`, `out6`, `out8`, `out10`, `out11`, `out12`, `out14`, `out17` |
| PE-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out3`, `out4`, `out6`, `out9`, `out10`, `out13`, `out18`, `out20`, `out21`, `out22` |
| PE-E | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out7`, `out10`, `out13`, `out15`, `out16`, `out20`, `out22` |
| SEAFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out6`, `out8`, `out9`, `out11`, `out12`, `out14` |

</details>

<details>
<summary><strong>sqlite</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out5`, `out6`, `out8`, `out9`, `out10`, `out11` |
| AFLFast | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10`, `out11` |
| EcoFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out6`, `out7`, `out8`, `out10`, `out11` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out8`, `out10`, `out11` |
| AFL-DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| Entropic | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10` |
| E-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10` |
| P-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out5`, `out6`, `out7`, `out9`, `out10`, `out11` |
| E-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| PE-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out8`, `out9`, `out10`, `out13`, `out14`, `out17`, `out18` |
| PE-E | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out3`, `out6`, `out12`, `out14`, `out15`, `out16`, `out18`, `out19`, `out22`, `out23` |
| SEAFuzz | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out4`, `out6`, `out9`, `out10`, `out11`, `out13`, `out14` |

</details>

<details>
<summary><strong>strip</strong> — 13 fuzzers and their out directories</summary>

| Fuzzer | Runs | Selected | Classified | ASAN | GDB | Unclassified | tot | uni | Consistency | Classification rate | Out directory names |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | 10 | 422 | 0 | 0 | 0 | 422 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10`, `out11` |
| AFLFast | 10 | 453 | 0 | 0 | 0 | 453 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out3`, `out5`, `out6`, `out7`, `out8`, `out9`, `out10`, `out11` |
| EcoFuzz | 10 | 333 | 0 | 0 | 0 | 333 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out9`, `out11` |
| DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10`, `out11` |
| AFL-DiPri | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out2`, `out3`, `out4`, `out5`, `out6`, `out8`, `out9`, `out10`, `out11` |
| Entropic | 10 | 6 | 0 | 0 | 0 | 6 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out9` |
| P-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out7`, `out8`, `out9`, `out10` |
| E-FE | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out0`, `out1`, `out2`, `out3`, `out4`, `out5`, `out6`, `out7`, `out8`, `out10` |
| P-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out3`, `out4`, `out6`, `out7`, `out9`, `out12`, `out13`, `out14`, `out15`, `out17` |
| E-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out2`, `out5`, `out6`, `out7`, `out10`, `out13`, `out14`, `out16`, `out17` |
| PE-F | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out4`, `out6`, `out7`, `out13`, `out14`, `out16`, `out17`, `out21`, `out22` |
| PE-E | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out4`, `out7`, `out10`, `out12`, `out13`, `out14`, `out17`, `out18`, `out19`, `out21` |
| SEAFuzz | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | 0.000000 | `out1`, `out3`, `out4`, `out5`, `out8`, `out9`, `out10`, `out11`, `out12`, `out13` |

</details>

## Reproducibility notes

- All 16 original program directories are retained; `gas` is also labeled as **as-new** for the paper.
- All 13 fuzzer display names use the final agreed mapping, including **PE-F** and **PE-E**.
- Empty or unclassified crash signatures remain recorded as in the source; they were not converted to confirmed bugs.
- The extra libpng variant was excluded and the libpng `PROGRAM_SUMMARY` was already recomputed consistently in the verified source.
- `out_list` values retain the exact original 10 directory identifiers per program/fuzzer, including gaps.
- All source numeric values and BugKey strings remain available in the recoverable TSV below.

## Complete data archive (lossless)

The readable tables above are designed for GitHub. The complete normalized TSV 
is also embedded below as an XZ-compressed Base64 payload. **No CRASH, BUG,
RUN_SUMMARY, or FUZZER_SUMMARY source records are omitted from the recoverable dataset.**
This preserves reproducibility without adding more files to the repository.

- Restored filename: `crash.tsv`
- SHA-256 of recovered file: `65551a855466451624065b431d288cbd254d761252976d4d1befc295b6c44dfd`
- Original TSV bytes: 50,125; compressed payload: 4,444 bytes

To reconstruct the machine-readable file (Linux / macOS with `xz` installed):

```bash
sed -n '/^CRASH_FULL_TSV_XZ_BASE64_BEGIN$/,/^CRASH_FULL_TSV_XZ_BASE64_END$/p' crash.md | sed '1d;$d' | base64 -d | xz -dc > crash.tsv
sha256sum crash.tsv
```

<details>
<summary>Show complete crash data payload (XZ + Base64)</summary>

```text
CRASH_FULL_TSV_XZ_BASE64_BEGIN
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
CRASH_FULL_TSV_XZ_BASE64_END
```

</details>
