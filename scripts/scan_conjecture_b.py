from __future__ import annotations

import argparse
import json
from pathlib import Path

from kronos.conjecture_b import scan_primes


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan Conjecture B through a finite prime bound.")
    parser.add_argument("--limit", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    report = scan_primes(args.limit)
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8", newline="\n")
    print(f"wrote {args.output} ({len(payload.encode('utf-8'))} bytes)")
    print(f"applicable primes: {report['applicable_prime_count']}")
    print(f"failures: {len(report['failures'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
