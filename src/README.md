# Source implementations

This directory contains SEAFuzz and the separate AFL-based DiPri port. The upstream AFL++ implementation of DiPri and the other comparison implementations are documented in [the baseline inventory](../baselines/README.md).

The directory names below are used by the build examples; the corresponding source snapshots must be placed under these names before running the commands.

```text
src/
├── README.md
├── SEAFuzz/
└── AFL-DiPri/
```

## SEAFuzz

SEAFuzz extends AFL with path-frequency and seed entropy feedback for fast-track seed scheduling and adaptive energy allocation.  command-line options and environment variables retain their existing names for compatibility.

### Source version and changes

- Upstream: [Google AFL](https://github.com/google/AFL).
- AFL version declared in `config.h`: **2.57b**.
- Upstream base commit: `61037103ae3722c8060ff7082994836a794f978e`.
- Files changed relative to that commit: `afl-fuzz.c`, `Makefile`, `hash.h`,and the implementation's `README.md`.

The main implementation is in `SEAFuzz/afl-fuzz.c`:

| Component | Implementation |
| --- | --- |
| Path-frequency feedback | Path-checksum frequency tracking and rarity-based seed marking. |
| Entropy feedback | Global feature-frequency tracking, a periodically refreshed rare-feature set, and per-seed entropy estimates. |
| Fast-track scheduling | Rarity and entropy checks that allow selected seeds to bypass AFL's seed-skipping checks. |
| Energy allocation | Path frequency and entropy features applied to AFL's original performance score. |
| Ablation and sensitivity controls | Separate module switches, feature switches, and runtime parameter overrides. |

`Makefile` links `afl-fuzz` with `-lm` for the added mathematical operations.

### Build and run

Run these commands from the repository root after staging the source tree:

```sh
make -C src/SEAFuzz -j2
make -C src/SEAFuzz/llvm_mode -j2 LLVM_CONFIG=llvm-config-10
```

For a target that accepts an input-file argument:

```sh
ASAN_OPTIONS_VALUE="abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1"
src/SEAFuzz/afl-fuzz \
  -i /path/to/seeds -o /path/to/results -m none -- \
  /path/to/instrumented_target @@
```

This is a command template. Use the target's actual arguments and the experiment's deterministic-stage setting. `-d`, when supplied, skips AFL's deterministic stages.

### Ablation options

Both feedback features and both added modules are enabled by default, assuming no environment overrides. Add the following options before `--`:

| Configuration | Option | Behavior |
| --- | --- | --- |
| Complete SEAFuzz | None | Both fast tracks and adaptive energy allocation. |
| Scheduler only | `-A` | Both fast tracks; original AFL energy calculation. |
| Energy allocation only | `-P` | Adaptive energy allocation; original AFL seed-skipping checks. |
| Rarity fast track only | `-RF` | Rarity fast track; entropy feedback disabled; original AFL energy calculation. |
| Entropy fast track only | `-EF` | Entropy fast track; rarity feedback disabled; original AFL energy calculation. |
| Path-frequency feedback only | `-E` | Disable entropy statistics, entropy fast track, and entropy energy factor. |
| Entropy feedback only | `-R` | Disable Path fast track and Path energy factor. |

`-A`, `-P`, `-RF`, and `-EF` are mutually exclusive and cannot be combined with
`-R` or `-E`. 

The module switches `AFL4_FAST_CHANNEL=0` and `AFL4_ENERGY_SCHEDULE=0` independently disable the added fast tracks and added energy factors. Their default is `1`. The explicit module-ablation options take precedence over these two environment variables. `AFL_ENTROPIC=0` disables entropy feedback; `-EF` explicitly enables it. Use a clean environment or record all overrides when comparing configurations.

### Parameter defaults

Parameter-sensitivity runs must record their overrides separately from the defaults.

| Environment variable | Default | Meaning |
| --- | --- | --- |
| `AFL4_RARE_RATIO` | `0.20` | Fraction used to select globally entropy rare features. |
| `AFL4_ENTROPY_REFRESH_SEC` | `60` | Entropy Rare-feature refresh interval, in seconds. |
| `AFL4_ENTROPY_QUANTILE` | `0.90` | Quantile for entropy fast-track eligibility. |
| `AFL4_ENTROPY_FAST_PROB` | `0.10` | Entropy fast-track probability. |
| `AFL4_ENTROPY_EMA` | `0.98` | Weight of the previous entropy moving average (EMA). |
| `AFL4_ENTROPY_SLOPE` | `0.20` | Entropy energy-factor slope. |
| `AFL4_ENTROPY_COOLING_OFFSET` | `4` | Offset in the logarithmic entropy-cooling function. |
| `AFL4_RARITY_FAST_BASE` | `0.10` | Base probability for the rarity fast track. |
| `AFL4_RARITY_FAST_OFFSET` | `10` | Offset in the rarity fast-track logarithmic denominator. |
| `AFL4_RARITY_ENERGY_BASE` | `0.40` | Constant term of the path frequency energy factor. |
| `AFL4_RARITY_ENERGY_NUMERATOR` | `4` | Numerator of its frequency-dependent term. |
| `AFL4_RARITY_ENERGY_SCALE` | `4` | Additive frequency denominator offset of that term. |
| `AFL4_RARITY_ENERGY_WEIGHT` | `0.50` | Rarity weight when combining both energy factors; entropy uses `1 - weight`. |
| `AFL_ENTROPIC_EVERY` | `1` | Execution interval for local entropy-statistics updates. |
| `AFL_ENTROPIC_MAX_FEATS` | `8192` | Maximum stored features per seed. |

Probabilities and ratios use decimal fractions, such as `0.20`. The entropy pseudo-count is `0.001`. The final performance score is capped at `HAVOC_MAX_MULT * 100` (`1600` in this snapshot).

## AFL-DiPri: separate AFL 2.57b port

`AFL-DiPri/` denotes the local port of DiPri to AFL 2.57b. It is a separate implementation from the AFL++-based `baselines/DiPri/` snapshot.

- AFL base: [Google AFL](https://github.com/google/AFL), commit
  `61037103ae3722c8060ff7082994836a794f978e`.
- DiPri reference implementation:
  [AFL++-DiPri](https://github.com/isefuzz/aflpp-dipri), whose checked-out upstream
  commit is `155b77c44df70c4a4f431011243454609ad4e91f`.
- Port-specific files: `afl-fuzz.c` and `Makefile` (`-lm` linkage).
- Added functionality: coverage-vector storage, distance-based seed evaluation,
  and prioritized queue traversal in the AFL workflow.

The port supports Hamming, Euclidean, and Jaccard distances and Vanilla, Periodical, and Adaptive modes. Its defaults are **Adaptive + Hamming**, whereas the AFL++ implementation defaults to **Vanilla + Hamming**. In all experiments, we used  **Adaptive + Hamming**, because in DiPri-related papers, this combination performs pretty well.

```sh
make -C src/AFL-DiPri -j2
make -C src/AFL-DiPri/llvm_mode -j2 LLVM_CONFIG=llvm-config-10

DIPRI_MODE=A DIPRI_MEASURE=H \
  src/AFL-DiPri/afl-fuzz \
  -i /path/to/seeds -o /path/to/results -m none -- \
  /path/to/instrumented_target @@
```

`DIPRI_MODE` accepts `V`, `P`, or `A`; `DIPRI_MEASURE` accepts `H`, `E`, or `J`. `DIPRI_PERIOD` controls the Periodical mode and defaults to 60 seconds. `DIPRI_EVAL_TYPE` selects distance or a supported intrinsic seed metric; `DIPRI_PLUSPLUS`, when nonempty, enables the additional bitmap-size ordering. Leave these two variables unset for the distance-only example above.

## How to use SEAFuzz(script)

ASAN_OPTIONS_VALUE="abort_on_error=1:symbolize=0:detect_leaks=0:allocator_may_return_null=1"\
SEAFuzz/AFL/afl-fuzz \
-i seeds\
-d \
-m none \
-o output \
-- TARGET

In these sets, '-d' means skip the deterministic phase, '-o' means no memory limit.
