# Literature Intake

This is the current primary-source intake, not a claim that the literature search is complete.

## Core sources

1. L.-C. Hsia, H.-C. Li, and W.-L. Sun, “Conflict-Avoiding Codes of Prime Lengths and Cyclotomic Numbers,” *IEEE Transactions on Information Theory* 70(10), 6834–6841 (2024). DOI: `10.1109/TIT.2024.3439714`. Preprint: `https://arxiv.org/abs/2302.01487`.
2. L.-C. Hsia, H.-C. Li, and W.-L. Sun, “Certain Diagonal Equations and Conflict-Avoiding Codes of Prime Lengths,” *Finite Fields and Their Applications* 92, article 102298 (2023). DOI: `10.1016/j.ffa.2023.102298`. Preprint: `https://arxiv.org/abs/2302.00920`.
3. H.-L. Fu, Y.-H. Lo, and K. W. Shum, “Optimal Conflict-Avoiding Codes of Odd Length and Weight Three,” *Designs, Codes and Cryptography* 72(2), 289–309 (2014). DOI: `10.1007/s10623-012-9764-5`.
4. W. Ma, C.-e. Zhao, and D. Shen, “New Optimal Constructions of Conflict-Avoiding Codes of Odd Length and Weight 3,” *Designs, Codes and Cryptography* 73(3), 791–804 (2014). DOI: `10.1007/s10623-013-9827-2`.
5. Y.-H. Lo, T.-L. Wong, K. Xu, and Y. Zhang, “Optimal Constant-Weight and Mixed-Weight Conflict-Avoiding Codes,” preprint `https://arxiv.org/abs/2407.11554`.
6. K. Xu, Y.-H. Lo, T.-L. Wong, Y. Zhang, and K. W. Shum, “Multichannel Conflict-Avoiding Codes for Expanded Scenarios,” preprint `https://arxiv.org/abs/2602.22081`.

## Reconciled statements used by the current target

The following are literature statements, not Project Kronos theorems:

- The weight-three even-length construction problem is settled, while the odd-length problem remains incomplete and prime lengths are fundamental cases.
- Conjecture B is equivalent to a twisted Fermat equation formulation called Conjecture C.
- The 2014 Ma–Zhao–Shen work is reported to have checked Conjecture B for primes `p <= 2^30`.
- The 2023 Hsia–Li–Sun theorem gives a sufficient condition at

  ```text
  p >= (2^omega(ell) * (ell - 3 - delta) + 2)^2 - 2,
  ```

  where `omega(ell)` counts distinct prime factors and `delta=1` when `4|ell`, otherwise `0`.
- The 2023 paper states unconditional coverage for every `ell <= 3000`, as well as broader ranges classified by the number of distinct prime factors.
- For `ell=3003`, the sufficient threshold evaluates to `2304192002`.

## Intake corrections made on 2026-08-06

- The earlier repository entry for the 2014 Fu–Lo–Shum paper lacked complete volume, issue, page, and DOI metadata.
- The earlier repository incorrectly attributed “New Optimal Constructions…” to Momihara, Jimbo, and Mesnager. The authors are Wenping Ma, Chun-e Zhao, and Dongsu Shen.
- The initial charter treated generic Conjecture B as the first target without accounting for the extensive 2023 coverage. The active target is now the finite `ell=3003` gap.

## Remaining literature work

- inspect the exact 2014 computational method and implementation assumptions behind the `2^30` claim;
- reconcile the notation `ell`, `ell_0`, and the role of the condition `4` not dividing `ord_p(2)` across papers;
- search citations after 2024 for an existing `ell=3003` closure or broader theorem;
- obtain external confirmation that the conditional synthesis is mathematically sound.
