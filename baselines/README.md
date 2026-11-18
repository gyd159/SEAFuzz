# Baseline implementations

This file records the source versions and local modifications of AFL, AFLFast, EcoFuzz, AFL++-DiPri, and Entropic. SEAFuzz and the separate AFL 2.57b DiPri port are documented in [the source inventory](../src/README.md).

## Directory layout

```text
baselines/
├── README.md
├── AFL/
├── AFLFast/
├── EcoFuzz/
│   └── EcoFuzz/
├── DiPri/
└── Entropic/
```

`EcoFuzz/` preserves the upstream repository layout, including its inner `EcoFuzz/` implementation directory. `DiPri/` contains the AFL++-based `aflpp-dipri` source tree. `Entropic/` contains the `compiler-rt/lib/fuzzer` subtree of the LLVM checkout, together with the applicable upstream license files. Build examples below assume these source snapshots have been placed in the indicated directories and are run from the artifact repository root.

## Source versions

| Baseline | Upstream repository | Declared framework version | Upstream base commit |
| --- | --- | --- | --- |
| AFL | [google/AFL](https://github.com/google/AFL) | AFL 2.57b | `61037103ae3722c8060ff7082994836a794f978e` |
| AFLFast | [mboehme/aflfast](https://github.com/mboehme/aflfast) | AFL 2.51b | `d1d54caf9850ca4afe2ac634a2a212aa6bb40032` |
| EcoFuzz | [MoonLight-SteinsGate/EcoFuzz](https://github.com/MoonLight-SteinsGate/EcoFuzz) | AFL 2.52b | `1fd94608291b708e9c97240780aea16349c688b8` |
| DiPri | [isefuzz/aflpp-dipri](https://github.com/isefuzz/aflpp-dipri) | AFL++ 4.06c (`++4.06c` in `include/config.h`) | `155b77c44df70c4a4f431011243454609ad4e91f` |
| Entropic | [llvm/llvm-project](https://github.com/llvm/llvm-project) | libFuzzer from an LLVM development checkout | `dc9be4ee30d07060a21273bdf8c64e4f34165562` |

The LLVM source commit identifies the libFuzzer source.

## AFL

```sh
make -C baselines/AFL -j2

ASAN_OPTIONS_VALUE="abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1"
baselines/AFLFast/afl-fuzz -p fast \
  -i /path/to/seeds -o /path/to/results -m none -d \
  -- /path/to/instrumented_target @@
```

When LLVM instrumentation is needed, build `baselines/AFL/llvm_mode` with the LLVM toolchain specified by the target's build configuration.

## AFLFast

```sh
make -C baselines/AFLFast -j2

ASAN_OPTIONS_VALUE="abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1"
baselines/AFLFast/afl-fuzz \
  -i /path/to/seeds -o /path/to/results -m none -d \
  -- /path/to/instrumented_target @@
```

`fast` is the default power schedule in this snapshot.

## EcoFuzz

```sh
make -C baselines/EcoFuzz/EcoFuzz -j2

ASAN_OPTIONS_VALUE="abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1"
baselines/EcoFuzz/EcoFuzz/afl-fuzz \
  -i /path/to/seeds -o /path/to/results -m none -d\
  -- /path/to/instrumented_target @@
```

## DiPri: AFL++ implementation

### Build and configuration

```sh
make -C baselines/DiPri source-only

ASAN_OPTIONS_VALUE="abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1"
DIPRI_MODE=A DIPRI_MEASURE=H \
  baselines/DiPri/afl-fuzz \
  -i /path/to/seeds -o /path/to/results -m none -d \
  -- /path/to/instrumented_target @@
```

The command explicitly selects **Adaptive + Hamming**. Without these overrides, this AFL++ implementation defaults to **Vanilla + Hamming**. `DIPRI_MODE=P` selects Periodical mode; `DIPRI_MEASURE=E` or `J` selects Euclidean or Jaccard distance. Distance evaluation is the default when `DIPRI_EVAL_TYPE` is unset. Leave `DIPRI_PLUSPLUS` unset for the distance-only example.

## Entropic: libFuzzer with the Entropic schedule

Entropic is evaluated through libFuzzer's existing Entropic power schedule.
It is enabled explicitly with **`-entropic=1`**. It is not an AFL port, and it
is separate from SEAFuzz's entropy-feedback ablation.

### Source and local modifications

The source subtree is `compiler-rt/lib/fuzzer` at the LLVM commit recorded above.
Four files have local changes related to fork-mode execution and statistics:

| File | Local changes |
| --- | --- |
| `FuzzerFlags.def` | Adds `-fork_job_duration` and `-fork_stats_file`. |
| `FuzzerOptions.h` | Stores the corresponding runtime options. |
| `FuzzerDriver.cpp` | Validates and passes the added options to fork mode. |
| `FuzzerFork.cpp` | Configurable child-job duration cap, per-job CSV statistics, and tracking of distinct crash-artifact names. |

The Entropic energy implementation in `FuzzerCorpus.h` matches the recorded upstream revision. The fork-mode changes still form part of the experimental implementation and must accompany the source snapshot. The local `-fork_job_duration=N` implementation caps child jobs at `N` seconds; the initial duration still increases with the job index. Zero retains the upstream 300-second cap. `-fork_stats_file` writes:

```text
unix_time,elapsed_seconds,job_id,new_seeds,total_seeds,total_execs,execs_per_sec,new_crashes,total_crashes
```

Here `total_seeds` counts the main corpus files and `total_crashes` counts distinct `crash-*` artifact names observed in child logs. They are native libFuzzer counters, with different definitions from AFL's path and crash counters. 

### Build and invocation

The provided `build.sh` compiles the local runtime sources into `libFuzzer.a`:

```sh
cd baselines/Entropic
CXX=clang++ ./build.sh
```

The build requires a C++17-capable compiler. Target compilation must link this runtime snapshot explicitly. Using only `-fsanitize=fuzzer` can instead select the compiler installation's bundled runtime. A target-specific build should  compile its sources with the required coverage instrumentation, such as `-fsanitize=fuzzer-no-link`, and link the resulting objects with this `libFuzzer.a`, together with the target's dependencies and sanitizer settings.

For a linked target exposing `LLVMFuzzerTestOneInput`, the basic invocation is:

```sh
/path/to/libfuzzer_target -entropic=1 /path/to/corpus
```

libFuzzer mutates inputs through the callback; it does not use AFL's `@@`
file-argument substitution. A fork-mode command template for the locally added
statistics is:

```sh
ASAN_OPTIONS_VALUE="abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1"
LSAN_OPTIONS_VALUE="detect_leaks=0:symbolize=0"
taskset -c 0 \
/path/to/libfuzzer_target \
  -entropic=1 -fork=1 -max_total_time=86400 \
  -fork_stats_file=/path/to/results/fork_stats.csv \
  -artifact_prefix=/path/to/results/artifacts/ \
  /path/to/corpus
```
taskset -c 0 binds to CPU core 0
Create the results, artifacts, and corpus directories first. This template illustrates the interface; the experiment configuration must record the actual fork settings, seed, limits, harness, and sanitizer options.

The source defaults for the Entropic options are:

| Option | Default |
| --- | --- |
| `-entropic` | `1` |
| `-entropic_feature_frequency_threshold` | `255` |
| `-entropic_number_of_rarest_features` | `100` |
| `-entropic_scale_per_exec_time` | `0` |

A nonempty `-focus_function` disables Entropic scheduling in this snapshot.
The startup message `INFO: Running with entropic power schedule` confirms that
the schedule is enabled.

## Fingerprints of modified baseline files

Paths are relative to the baseline directories above.

| File | SHA-256 |
| --- | --- |
| `DiPri/include/afl-fuzz.h` | `d8a168dfe56d1970b43aec5983da4f7545f088ec00dddcbc069712815be61bf9` |
| `DiPri/include/config.h` | `c561bc96fe69e3bc96ea51481e17c70292d859e5d8281014a162357085fc75f4` |
| `DiPri/src/afl-fuzz-init.c` | `25748d53913f350e8c42ba94e879f2184949c6493f1a6fa0ca641a86004f74ef` |
| `DiPri/src/afl-fuzz-queue.c` | `4b2a8b656c040d03c66ff8cc1b8ac03703ba8b44f830fe9894b783178a3463d2` |
| `DiPri/src/afl-fuzz-run.c` | `fba9b57860a73cf20217fd56bbc6453886bac7263fce8f052f24219efb031b76` |
| `Entropic/FuzzerDriver.cpp` | `dab37a1107adb09fd21be1ed1c9074abfb39e0ef016a8dd9c74555b1f250b17e` |
| `Entropic/FuzzerFlags.def` | `127ba60274a1c42b4d32ea5c42f850cdd594dba7d4246026370996451ed1cd26` |
| `Entropic/FuzzerFork.cpp` | `6d3bfa82c3153073dcbfb64a717d0fdb16e9b8514e938a8d49be993602002db9` |
| `Entropic/FuzzerOptions.h` | `33bbc8305c85f1d5c3cb05f8c2bc6b4247c5974eb6c1cfd2015247e140e7177b` |

Preserve each upstream project's license files and copyright notices. The AFL-derived source files carry Apache 2.0 notices. The LLVM compiler-rt license declares Apache 2.0 with LLVM Exceptions; retain its `LICENSE.TXT` and the applicable notices when packaging the libFuzzer subtree.
