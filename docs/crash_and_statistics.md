# Unique crashes and Magma bugs

This document shows a reproducible procedure. It covers ordinary AFL output, Entropic output, UniFuzz deduplication with ASan/GDB, and Magma Canary builds, reachability checks, and trigger decisions.

## 1. Analysis Scope and Directory Layout

Ordinary AFL/UniFuzz data are stored in:

``` text
/home/gg/outputxxx/outputy/<program>/<fuzzer>/outN/
```

Entropic data are stored in:

``` text
/home/gg/outputxxx/entropic/entropic/<program>/outN/       # contains seed_count.csv and artifacts/
```

The current Magma Canary target mapping is:

| program    | target binary                      | monitor                  |
|------------|------------------------------------|--------------------------|
| libpng     | fuzzing_libpng/libpng_read_fuzzer  | build/libpng/monitor     |
| libsndfile | fuzzing_libsndfile/sndfile_fuzzer  | build/libsndfile/monitor |
| lua        | fuzzing_lua/lua/lua                | build/lua/monitor        |
| php        | fuzzing_php/parser                 | build/php/monitor        |
| poppler    | fuzzing_poppler/poppler_pdf_fuzzer | build/poppler/monitor    |
| sqlite     | fuzzing_sqlite3/sqlite3_fuzz       | build/sqlite3/monitor    |

`crash.txt` covers all 16 programs; the monitor is run for only the six
Canary targets listed above when generating `magma.tsv`.

## 2. Selecting Ordinary AFL Crashes

Selection is based on each `out` directory’s own `plot_data`, not on crash-file creation or modification times. The algorithm is implemented in `/home/gg/magma_canary/crash_analyse/unifuzz_batch.py`.

### 2.1 Reading the Time Series

The script checks these locations in order:

``` text
<out>/plot_data
<out>/default/plot_data       # used if the first path does not exist
```

The file must have a header and parseable data rows. The count column is `unique_crashes` when available; otherwise, `saved_crashes` is used. If neither column exists, the `out` cannot be selected using this rule.

The time window spans 86,400 seconds from the first valid record in `plot_data`:

- If the first column is headed `unix_time`, set `start = first_unix_time` and retain rows where `time <= start + 86400`.
- Otherwise, treat the first column as relative time in seconds and retain rows where `relative_time <= 86400`.

The count value on the last row within the window is `crash_limit`. It is a cumulative upper bound; it is not obtained by rescanning the crash directory.

### 2.2 Selecting Files by Crash ID

Scan `<out>/crashes` and:

1.  Skip `README.txt` and accept regular files only.
2.  Require the filename to contain `id:<number>`.
3.  Sort files in ascending order by the extracted numeric ID.
4.  Select the first `crash_limit` files in that order.

Directory order and `mtime` are not used. If `crash_limit=7` but only four parseable files exist, only four are selected. `selected_crashes` counts the inputs actually executed.

For the n-th selected input (`selected_index=n-1`), the script finds the first time on the cumulative-count curve at which `crash_count >= n` and records it as `plot_time`. `plot_time` is a curve-mapped time, not a file timestamp.

For example, if the final `unique_crashes` value in the window is 7 and the directory contains 10 files sorted by ID, only the first seven are executed; files with the eighth and later IDs are excluded from this analysis.

### 2.3 Replaying Inputs

Ordinary ASan replay uses a 20-second timeout and the following options:

``` sh
ASAN_OPTIONS=abort_on_error=1:symbolize=1:detect_leaks=0:allocator_may_return_null=1
```

GDB fallback is run only when ASan produces no valid report; the GDB timeout is 12 seconds. 

## 3. Selecting Entropic Crashes

We used all the crash seeds that Entropic recorded during testing.

## 4. UniFuzz Crash Deduplication

### 4.1 ASan First, GDB as Fallback

Each selected input is classified in the following order:

1.  Run the target and parse `AddressSanitizer: <error_type>`.
2.  Extract the first three function names from stack frames marked with `#N`; pad with `<missing>` if fewer than three frames are available.
3.  If no valid ASan error line is found, run the input under GDB and parse `Program received signal SIG...` and the first three stack frames.
4.  If ASan succeeds, do not run GDB; therefore, one input is not counted in both classification paths.

The ASan BugKey is:

``` text
ASAN|error_type|frame0|frame1|frame2
```

The GDB BugKey is:

``` text
GDB|signal|frame0|frame1|frame2
```

Inputs with the same error type/signal and the same first three function names are assigned to the same candidate category. File paths, AFL crash IDs, file hashes, `mtime`, and later stack frames are not used for deduplication. If neither ASan nor GDB yields a valid key, the input is marked `unclassified`.

### 4.2 Fields and Statistics in `crash.txt`

The file is a tab-separated TSV with two main record types:
`FUZZER_SUMMARY` and `PROGRAM_SUMMARY`. The core fields mean:

| Field                          | Meaning                                                                      |
|--------------------------------|------------------------------------------------------------------------------|
| `runs`                         | Number of independent `out` runs included; not the number of crashes         |
| `selected_crashes`             | Number of inputs actually selected and replayed                              |
| `classified_crashes`           | Number of inputs assigned a valid ASan or GDB key                            |
| `asan_crashes` / `gdb_crashes` | Counts for the two classification paths                                      |
| `unclassified_crashes`         | Number of inputs without a key                                               |
| `tot`                          | Deduplicate within each `out`, then sum the number of keys across `out` runs |
| `uni`                          | Size of the union of BugKeys across all `out` runs                           |
| `classification_rate`          | Classification rate                                                          |
| `unique_bug_keys`              | Actual keys, separated by semicolons                                         |

For the set `S(out_i)` associated with a program/fuzzer pair, the statistics are:

``` text
tot = Σ |S(out_i)|
uni = |S(out_1) ∪ S(out_2) ∪ ...|
consistency = tot / (uni × runs)       # when uni and runs are nonzero
classification_rate = classified_crashes / selected_crashes
```

`tot` reflects how often candidate categories recur across independent `out` runs; `uni` is the number of distinct candidate categories. Neither is the number of actual Magma vulnerabilities. `PROGRAM_SUMMARY` adds the counts from all fuzzers and computes a cross-fuzzer union of `unique_bug_keys`.

## 5. Building Magma

### 5.1 Official Captain/Docker Workflow

Magma’s official entry point is `magma/tools/captain/build.sh`. It requires `FUZZER` and `TARGET` to be set and builds a Docker image from the Magma root directory:

``` sh
cd magma
export MAGMA=magma
export FUZZER=afl_asan             # another directory under magma/fuzzers/ may also be selected
export TARGET=libpng               # e.g., libpng, libsndfile, lua, php, poppler, or sqlite3
export CANARY_MODE=1               # 1: enable Canary; do not enable fixes
magma/tools/captain/build.sh
```

The command requires Docker and the target’s build dependencies. `build.sh` converts `CANARY_MODE=1` into `--build-arg canaries=1`. Do not use `CANARY_MODE=3` as a Canary vulnerability-detection build: that mode enables fixes rather than canaries.

### 5.2 Stages in the Dockerfile

The key stages in `magma/docker/Dockerfile` are:

1.  Install Magma, fuzzer, and target dependencies.
2.  Run Magma’s `prebuild.sh` to compile `canary.c` and `storage.c` into `magma.o`.
3.  Run the fuzzer’s `fetch.sh` and `build.sh`.
4.  Run the target’s `fetch.sh` and `magma/apply_patches.sh` to apply setup and bug patches in sequence.
5.  Compile the target with options such as `-include <magma>/src/canary.h`, `-DMAGMA_ENABLE_CANARIES`, and `-g -O0`.
6.  Run the fuzzer’s `instrument.sh` to link the fuzzer driver, target, and `magma.o`.

Inside the container, `SHARED` defaults to `/magma_shared`, so the
shared storage object is `$SHARED/canaries.raw`. The monitor is also
built by `magma/prebuild.sh` and reads the same shared object at
runtime.

Optional build switches:

| Switch          | Effect                                                                                           |
|-----------------|--------------------------------------------------------------------------------------------------|
| `CANARY_MODE=1` | Defines `MAGMA_ENABLE_CANARIES`, retains vulnerable code, and enables checkpoints                |
| `ISAN=1`        | Defines `MAGMA_FATAL_CANARIES`; when a Canary is triggered, the target terminates with `SIGSEGV` |
| `HARDEN=1`      | Defines `MAGMA_HARDEN_CANARIES` and protects shared-memory pages                                 |
| `CANARY_MODE=3` | Defines fixes; used for fixed-version comparisons, not vulnerability discovery                   |

This crash analysis uses Canary builds. Results from fixes builds must not be mixed with `magma.tsv`.

### 5.3 Target-Specific Builds

The actual build details for each target are determined by
`magma/targets/*/build.sh`:

- libpng: run `autoreconf`/`configure`, then statically build `libpng16.a` and `libpng_read_fuzzer`.
- libsndfile: use `--enable-ossfuzzers` to generate `sndfile_fuzzer`.
- Lua: build `liblua.a` and `lua`.
- PHP: build the fuzzer-enabled PHP version and generate drivers such as `parser`.
- Poppler: build FreeType first, then use CMake to build static Poppler and `pdf_fuzzer`.
- SQLite: enable options such as debug/rtree, then build the amalgamation and `sqlite3_fuzz`.

## 6. Determining Whether a Canary Was Reached or Triggered

For each input, the analysis script runs:

``` sh
/home/gg/magma_canary/build/libpng/monitor --fetch watch --dump human \
  /home/gg/magma_canary/fuzzing_libpng/libpng_read_fuzzer /path/to/crash
```

For another target, replace only the monitor and target paths. The analysis script uses a 20-second monitor timeout; a timeout is recorded as `rc=124`, while a script execution error is usually recorded as `rc=125`. `run_canary.sh` is a convenience script for manual batch testing and uses a 15-second timeout; do not confuse its timeout with the analysis timeout used for `magma.tsv`.

The monitor output is parsed with this regular expression:

``` text
<BUG_ID> reached <integer> triggered <integer>
```

The `MAGMA_LOG`/`MAGMA_LOG_V` macros in the source define these labels and conditions, such as `PNG007`, `SND017`, and `LUA004`. A label identifies a known Magma vulnerability checkpoint; when its condition is true, Canary increments the `triggered` count.

The decision rules are:

- `reached > 0`: execution reached the checkpoint, but the condition was not necessarily satisfied.
- `triggered > 0`: the vulnerability condition at that checkpoint was satisfied.
- If one crash has multiple labels, record each label separately.
- The status of a `CRASH` row prioritizes `triggered`, then `reached`; if neither is present, use `none`.

To manually verify a single input:

``` sh
cd /home/gg/magma_canary
build/libpng/monitor --rm
build/libpng/monitor --fetch watch --dump human \
  fuzzing_libpng/libpng_read_fuzzer /path/to/crash
```

The monitor for each target is located at `build/<program>/monitor`;
replace the paths above for the target being tested.

## 7. Fields and Statistics in `magma.tsv`

`magma.tsv` contains four sections.

### CRASH

Each row corresponds to a crash/artifact that was actually executed. It records the root, program, fuzzer, `out`, crash ID, input path, plot time, monitor return code, status, reached labels, triggered labels, and error information. `crash_id` comes from the filename; it is not a Magma bug ID.

### BUG

Each row represents an association between one crash and one Magma `bug_id`:

``` text
BUG  root  program  fuzzer  out  crash_id  bug_id  reached  triggered
```

The same bug appearing in many crashes produces many `BUG` rows. The number of `BUG` rows is the number of associations, not the number of distinct vulnerabilities.

### FUZZER_SUMMARY

Multiple `out` runs are aggregated by root, program, and fuzzer. For `X`, where `X` is either reached or triggered, the formulas are:

``` text
X_tot = Σ |X_set(out_i)|
X_uni = |X_set(out_1) ∪ ... ∪ X_set(out_runs)|
X_missed = known_bugs - X_uni
X_consistency = X_tot / (X_uni × runs)
```

## 8. Keep the Two Deduplication Schemes Separate

| Statistics location            | Deduplication key                                    | Question answered                                    |
|--------------------------------|------------------------------------------------------|------------------------------------------------------|
| `uni` in `crash.txt`           | ASan/GDB + error/signal + first three stack frames   | How many candidate crash categories are present?     |
| `BUG` in `magma.tsv`           | Association between one crash and one Magma `bug_id` | Which inputs reached or triggered which labels?      |
| `triggered_uni` in `magma.tsv` | Set of Magma `bug_id` labels                         | How many distinct known Magma labels were triggered? |

The `uni` value in `crash.txt` is not the number of real vulnerabilities and must not be added to or substituted for `triggered_uni`. One Magma bug can produce multiple ASan stack categories, and one ASan category may correspond to different Magma labels.

## 8.1 Regenerating the Analysis Results

The analysis scripts perform ordinary AFL/UniFuzz scanning, replay, and
`crash.txt` aggregation:

``` sh
cd /home/gg/magma_canary
python3 crash_analyse/unifuzz_batch.py
```

The script scans `output`, then writes `unifuzz_manifest.tsv`, `unifuzz_results.tsv`, and logs. A subsequent aggregation step computes `tot`, `uni`, `consistency`, and the classification rate for each program/fuzzer/`out`, then updates `crash_analyse/1/crash.txt`. Do not mistake the per-input TSV files for the final summary file. Back up existing results before rerunning; the script skips tasks already completed according to the existing per-input results.

Entropic processing has two steps:

``` sh
cd /home/gg/magma_canary
python3 crash_analyse/add_entropic.py
python3 crash_analyse/merge_entropic.py
```

`add_entropic.py` replays all `artifacts/crash-*` files and runs Magma for the six programs with Canary monitors. `merge_entropic.py` then merges the intermediate TSV files into `crash_analyse/1/crash.txt` and `crash_analyse/1/magma.tsv`. These scripts may launch many target processes; use `UNIFUZZ_WORKERS` or `ENTROPIC_WORKERS` to limit concurrency.

## 9. Keep the Three Meanings of “Unique” Separate

The experiment uses at least three distinct meanings of “unique”; they must not be conflated:

| Name                           | Source                  | Actual meaning                                                                                      |
|--------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| `plot_data.unique_crashes`     | AFL `plot_data`         | Cumulative count used to determine the maximum number of inputs to select within the 24-hour window |
| `uni` in `crash.txt`           | ASan/GDB replay results | Union of BugKeys (error type/signal + first three stack frames)                                     |
| `triggered_uni` in `magma.tsv` | Magma monitor           | Union of Magma `bug_id` labels                                                                      |

## 10. Meaning of Unclassified Crashes

`unclassified_crashes` means that the current replay produced neither a parseable ASan BugKey nor a parseable GDB BugKey. It does not mean that the input is bug-free or that the original AFL record is invalid.

Common causes include:

- The `sig:06` marker in the original AFL filename cannot be reproduced in the current environment.
- The target exits normally or returns because the input format is
  invalid.
- ASan emits only a warning and no standard AddressSanitizer error line.
- GDB receives no recognizable signal or no valid stack trace is available.
- Execution times out, the command fails, or the target arguments differ from those used in the original run.
- Inputs for binutils targets such as `objcopy` or `strip` produce only `memory exhausted` or exit code 1.

## 11. Extracting and Aggregating Path Coverage

AFL `plot_data` headers commonly include:

``` text
unix_time, cycles_done, cur_path, paths_total, pending_total,
pending_favs, map_size, unique_crashes, unique_hangs, max_depth,
execs_per_sec
```

For each data row, `paths_total` is the cumulative number of paths discovered up to that time. **The uploaded path-statistics scripts actually read the first column as time and the fourth column as the metric; they do not search for a column named `paths_total`.** This interpretation is valid only if the fourth column in the input file is in fact `paths_total`. For each independent `out` run, the first valid record is treated as time zero, and the last record no later than the 24-hour target is selected:

``` text
paths_total_24h(out_i) = the last valid fourth-column value with elapsed_time <= 86400 seconds
```

The scripts default to `TIME_ZERO_MODE="first_row"`, `SAMPLE_METHOD="previous"`, and `FILL_AFTER_LAST=True`. If a run is shorter than 24 hours, its last observed value is carried forward rather than treating the run as missing.
