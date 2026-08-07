# Project Kronos

Project Kronos is a governed AI-assisted research program on **conflict-avoiding codes (CACs)**, deterministic schedules for asynchronous multiple access without feedback.

## Candidate target

The broad problem is to determine optimal weight-three CACs of odd length. The first narrow target is the prime-length coset statement called **Conjecture B** in the literature:

> For an odd prime `p`, set `H = <-1,2> <= F_p^*` and `ell = [F_p^*:H]`. If `ell >= 3`, there should be a generator `tH` of the quotient and `b in tH`, `c in t^2H` with `1+b=c (mod p)`.

The conjecture and the broader odd-length problem remain open. This repository currently contains initialization structure and baseline verification tooling, not a new theorem.

## Research branch

Active integration branch: `research/odd-length-weight3-cac`

`main` remains the stable landing branch. Exploratory changes should branch from the research branch and return through pull requests.

## Current status

- Cruthúnas experimental adoption metadata is pinned to commit `f60d61d19254759a1c395cae52663f82212a8121`.
- The project is explicitly **non-conformant** because Cruthúnas has not released a conformant framework version.
- The claim ledger is empty until intake and baseline reproduction are complete.
- A deterministic finite scanner and a separately implemented report verifier are included.
- The separate verifier is not yet an independent reproduction by a different researcher.

## Run the baseline

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python scripts/scan_conjecture_b.py --limit 5000 --output artifacts/baseline.json
python verifiers/verify_conjecture_b.py artifacts/baseline.json
python scripts/negative_control.py artifacts/baseline.json
```

An empty finite failure list is computational evidence only and does not prove the conjecture.

## Documentation

- [`RESEARCH_CHARTER.md`](RESEARCH_CHARTER.md)
- [`docs/PROBLEM.md`](docs/PROBLEM.md)
- [`docs/STATUS.md`](docs/STATUS.md)
- [`docs/ROADMAP.md`](docs/ROADMAP.md)
- [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md)
- [`LITERATURE.md`](LITERATURE.md)
- [`AI_USE.md`](AI_USE.md)
