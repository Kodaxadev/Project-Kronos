# Project Kronos

Project Kronos is a governed AI-assisted research program on **conflict-avoiding codes (CACs)**, deterministic schedules for asynchronous multiple access without feedback.

## Research target

The broad problem is to determine optimal weight-three CACs of odd length. The active narrow target is **Conjecture B** for prime lengths. For an odd prime `p`, let

- `H = <-1,2> <= F_p^*`, and
- `ell = [F_p^*:H]`.

Conjecture B asks whether, whenever `ell >= 3`, some primitive root `g` admits `b in gH` and `c in g^2H` with `1+b=c (mod p)`.

Primary-source reconciliation showed that the published literature already covers every `ell <= 3000` and several much larger families. The first deliberately isolated project target is therefore the composite index

```text
ell = 3003 = 3 * 7 * 11 * 13.
```

For this index, published results leave one finite interval between the historical computation through `2^30` and the published sufficient bound `2304192002`. Project Kronos has produced an internally cross-checked enumeration of that interval, but the result remains a **claim proposal**, not a registered theorem or independent reproduction.

## Research branch

Active integration branch: `research/odd-length-weight3-cac`

`main` remains the stable landing branch. Exploratory changes should branch from the research branch and return through pull requests.

## Current status

- Cruthúnas experimental adoption metadata is pinned to commit `f60d61d19254759a1c395cae52663f82212a8121`.
- The project is explicitly **non-conformant** because Cruthúnas has not released a conformant framework version.
- The canonical claim ledger remains empty.
- Proposal `K001` records a bounded computational result for the `ell=3003` finite gap.
- Python and C++ implementations agree on all five indexed primes and their witnesses.
- Neither implementation counts as independent reproduction by a separate researcher.

## Reproduce the current package

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
python scripts/close_index_3003.py --output artifacts/index-3003-generated.json
python verifiers/verify_index_3003.py artifacts/index-3003-generated.json
python scripts/negative_control_index_3003.py artifacts/index-3003-generated.json

g++ -O2 -std=c++20 -Wall -Wextra -pedantic \
  verifiers/verify_index_3003.cpp -o verify-index-3003
./verify-index-3003 > artifacts/index-3003-cpp-generated.txt
python verifiers/compare_index_3003.py \
  artifacts/index-3003-generated.json artifacts/index-3003-cpp-generated.txt
```

The finite result does not by itself prove Conjecture B even for `ell=3003`; the synthesis also depends on the correctness and applicability of the cited published results below and above the searched interval.

## Documentation

- [`RESEARCH_CHARTER.md`](RESEARCH_CHARTER.md)
- [`docs/GATE0_INTAKE.md`](docs/GATE0_INTAKE.md)
- [`docs/PROBLEM.md`](docs/PROBLEM.md)
- [`docs/STATUS.md`](docs/STATUS.md)
- [`docs/results/index-3003-gap.md`](docs/results/index-3003-gap.md)
- [`docs/AI_ACTIVITY_AUDIT.md`](docs/AI_ACTIVITY_AUDIT.md)
- [`docs/BASELINE_REPRODUCTION.md`](docs/BASELINE_REPRODUCTION.md)
- [`docs/ROADMAP.md`](docs/ROADMAP.md)
- [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md)
- [`LITERATURE.md`](LITERATURE.md)
- [`AI_USE.md`](AI_USE.md)
