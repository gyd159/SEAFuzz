"""Core deduplication for magma.tsv; process CRASH records and count reached/triggered separately."""

from collections import defaultdict


def deduplicate(records):
    groups = defaultdict(lambda: defaultdict(
        lambda: {"reached": set(), "triggered": set()}
    ))
    for row in records:
        if row.get("record_type") != "CRASH":
            continue
        runs = groups[row["root"], row["program"], row["fuzzer"]]
        bugs = runs[row["out"]]
        for kind in ("reached", "triggered"):
            bugs[kind].update(
                bug.strip() for bug in row[f"{kind}_bugs"].split(",")
                if bug.strip() not in ("", "-")
            )  # Count each bug ID once; reached and triggered remain separate.

    result = {}
    for group, runs in groups.items():
        result[group] = {}
        for kind in ("reached", "triggered"):
            union = set().union(*(bugs[kind] for bugs in runs.values()))
            result[group][kind] = {
                "tot": sum(len(bugs[kind]) for bugs in runs.values()),
                "uni": len(union),
                "bug_ids": union,
            }
    return result
