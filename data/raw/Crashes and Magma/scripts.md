# Deduplication Script Notes

## `crash.py`

For UniFuzz results in the `crash.txt` format.

- Grouping key: `program + fuzzer`.
- Each group combines results from all roots and outs.
- ASan uses `ASAN|error type|first 3 stack frames` as the BugKey.
- If no valid ASan result exists, it uses `GDB|signal|first 3 stack frames`.
- Deduplicate within each out first; `tot` is the sum of per-out unique counts, and `uni` is the size of the union across all outs.

## `magma.py`

For `CRASH` records in `magma.tsv`.

- Grouping key: `root + program + fuzzer`.
- Collect `reached_bugs` and `triggered_bugs` separately for each out.
- Keep each Magma bug ID only once.
- `tot` is the sum of per-out unique counts, and `uni` is the size of the union across all outs.
- `reached` and `triggered` are counted separately and are not merged.

The scripts contain only the deduplication functions; the caller handles input/output and writing results.
