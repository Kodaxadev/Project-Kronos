from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


def load_verifier():
    path = Path(__file__).resolve().parents[1] / "verifiers" / "verify_conjecture_b.py"
    spec = importlib.util.spec_from_file_location("kronos_standalone_verifier", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load standalone verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser(description="Ensure a material witness corruption is rejected.")
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    report = json.loads(args.report.read_text(encoding="utf-8"))
    if not report["records"]:
        raise RuntimeError("negative control requires at least one witness record")
    report["records"][0]["c"] = (report["records"][0]["c"] + 1) % report["records"][0]["p"]
    verifier = load_verifier()
    ok, _message = verifier.verify_report(report)
    if ok:
        print("negative control failed: corrupted witness was accepted")
        return 1
    print("negative control passed: corrupted witness was rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
