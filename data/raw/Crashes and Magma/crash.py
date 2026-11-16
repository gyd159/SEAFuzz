"""Core deduplication for crash.txt; input selection, replay, parsing, and I/O omitted."""

from collections import defaultdict


def bug_key(asan_error=None, asan_frames=(), gdb_signal=None, gdb_frames=()):
    """Build a key from function names after addresses, paths, and line numbers are removed."""
    if asan_error and asan_error != "-":
        source, error, frames = "ASAN", asan_error, asan_frames
    elif gdb_signal and gdb_signal != "-":
        source, error, frames = "GDB", gdb_signal, gdb_frames
    else:
        return None  # Unclassified samples are excluded from deduplication.
    frames = list(frames)[:3]
    frames += ["<missing>"] * (3 - len(frames))
    return "|".join([source, error, *frames])


def deduplicate(records):
    """Deduplicate records containing experiment IDs and parsed crash fields."""
    groups = defaultdict(lambda: defaultdict(set))
    for row in records:
        runs = groups[row["program"], row["fuzzer"]]
        bugs = runs[row["root"], row["out"]]
        key = bug_key(
            row.get("asan_error"), row.get("asan_frames", ()),
            row.get("gdb_signal"), row.get("gdb_frames", ()),
        )
        if key is not None:
            bugs.add(key)  # Deduplicate within each independent out first.

    result = {}
    for group, runs in groups.items():
        union = set().union(*runs.values())
        result[group] = {
            "tot": sum(map(len, runs.values())),  # Sum of per-out unique counts.
            "uni": len(union),                   # Size of the cross-out union.
            "unique_bug_keys": union,
        }
    return result
