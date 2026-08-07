# Reproducibility

## Environment

The starter tools use only the Python standard library and require Python 3.11 or newer.

## Commands

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python scripts/scan_conjecture_b.py --limit 5000 --output artifacts/baseline.json
python verifiers/verify_conjecture_b.py artifacts/baseline.json
python scripts/negative_control.py artifacts/baseline.json
```

Run the scanner twice and compare bytes to test deterministic serialization.

## Independence statement

`verifiers/verify_conjecture_b.py` is structurally separated and does not import the scanner package. It independently recomputes primality, the subgroup, quotient order, report completeness, and every witness condition. Because it was created in the same initialization workflow, it is not recorded as `INDEPENDENT_REPRODUCTION`.

## Artifact policy

Generated scans go under `artifacts/` or `results/`. A result becomes governed evidence only after its exact command, environment, source revision, hash, scope, and negative-control outcome are registered under `audit/evidence/`.
