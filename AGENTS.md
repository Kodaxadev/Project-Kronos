# Agent Operating Rules

Read `RESEARCH_CHARTER.md`, `docs/STATUS.md`, and `claims/claims.yaml` before changing research content.

## Mandatory boundaries

- Do not describe the candidate conjecture as solved.
- Do not register a new claim without an exact quantified statement and explicit limitations.
- Do not promote a finite scan to a universal result.
- Do not call same-workflow implementations independent.
- Preserve failed routes and counterexamples under `docs/refutations/` when they arise.
- Generated reports belong in `artifacts/` or `results/`; large outputs are not committed without a manifest decision.
- Every verifier must reject at least one material corruption.
- Keep workflow actions pinned by full commit SHA.

## Research sequence

1. Reproduce definitions and published examples.
2. Register a bounded claim proposal.
3. Run a fresh hostile audit.
4. Build computation with an explicit domain and deterministic output.
5. Add a structurally separate verifier and meaningful negative control.
6. Seek genuinely independent reproduction or formalization.
7. Update the claim ledger only through evidence-backed transitions.
