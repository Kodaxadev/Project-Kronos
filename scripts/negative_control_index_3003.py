from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    data = json.loads(args.report.read_text(encoding="utf-8"))
    data["indexed_primes"][0]["c"] += 1
    with tempfile.TemporaryDirectory() as directory:
        corrupted = Path(directory) / "corrupted.json"
        corrupted.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        verifier = Path(__file__).resolve().parents[1] / "verifiers" / "verify_index_3003.py"
        result = subprocess.run(
            [sys.executable, str(verifier), str(corrupted)],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            raise SystemExit("negative control failed: corrupted witness was accepted")
    print("NEGATIVE CONTROL PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
