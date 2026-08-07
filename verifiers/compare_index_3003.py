from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_cpp(path: Path) -> dict[str, object]:
    summary: dict[str, int] = {}
    records: list[dict[str, int]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        parts = raw.split()
        if not parts:
            continue
        if parts[0] == "P":
            records.append({
                "p": int(parts[1]),
                "subgroup_size": int(parts[3]),
                "order_of_2": int(parts[5]),
                "primitive_root": int(parts[7]),
                "b": int(parts[9]),
                "c": int(parts[11]),
                "subgroup_exponent": int(parts[13]),
            })
        else:
            summary[parts[0]] = int(parts[1])
    return {"summary": summary, "records": records}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_report", type=Path)
    parser.add_argument("cpp_report", type=Path)
    args = parser.parse_args()
    py = json.loads(args.json_report.read_text(encoding="utf-8"))
    cpp = parse_cpp(args.cpp_report)
    summary = cpp["summary"]
    assert summary["ELL"] == py["ell"]
    assert summary["LOWER_EXCLUSIVE"] == py["searched_prime_interval"]["lower_exclusive"]
    assert summary["UPPER_EXCLUSIVE"] == py["searched_prime_interval"]["upper_exclusive"]
    assert summary["FIRST_K"] == py["progression"]["first_k"]
    assert summary["LAST_K"] == py["progression"]["last_k"]
    assert summary["PROGRESSION_CANDIDATES"] == py["progression_candidate_count"]
    assert summary["PRIME_CANDIDATES"] == py["prime_candidate_count"]
    assert summary["INDEXED_PRIMES"] == py["indexed_prime_count"]
    projected = [
        {key: record[key] for key in ("p", "subgroup_size", "order_of_2", "primitive_root", "b", "c", "subgroup_exponent")}
        for record in py["indexed_primes"]
    ]
    assert cpp["records"] == projected
    print("CROSS-LANGUAGE MATCH")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
