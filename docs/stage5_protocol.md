# Stage 5 Protocol — Temporal-Order Hierarchy of Observable Irreversibility

## 1. Status and purpose

Stage 5 is the bounded continuation selected after merged Stage 4.

Stage 4 classified exact first-detection depth `L_arrow` across a fixed four-state observation lattice, but it did not explain why the same micro process can yield `L_arrow=1`, `2`, `3`, or `infinity` under different deterministic observations.

Stage 5 asks:

> What exact time-reversal-odd trajectory structure first survives at each finite detection depth, and how does deterministic coarse-graining cancel or retain the microtrajectory contributions that produce it?

The stage does **not** enlarge the hidden-state count, search beyond the already frozen Stage 4 detection depths, introduce new benchmark families, or claim an arbitrary-order structural theorem.

## 2. Frozen model and observation family

The primary model is only the existing Stage 3/4 witness:

`higher_order_hidden_arrow_four_state()`.

All 15 deterministic set partitions of its four microstates are retained for the detection-class census. Stage 4 already certified their exact classes:

- four observations with `L_arrow=1`;
- two with `L_arrow=2`;
- two with `L_arrow=3`;
- seven with `L_arrow=infinity`.

No new state count or preferred-effect search is allowed.

## 3. Exact reversal-odd hierarchy

For the exact observed path law `P_L` on words of length `L+1`, let `R` reverse a word and define

`O_L(w) = (P_L(w) - P_L(Rw)) / 2`.

`O_L` is the exact time-reversal-odd component of the path law.

Then

`O_L = 0 <=> P_L = R P_L <=> A_L = 0`.

Therefore Stage 4 detection depth can be rewritten exactly as

`L_arrow = min { L>=1 : O_L != 0 }`,

with `L_arrow=infinity` iff every finite-order odd component vanishes.

For compact reporting, one representative is retained from each non-palindromic reversal pair. Its signed difference is

`Delta_L(w) = P_L(w) - P_L(Rw) = 2 O_L(w)`.

The exact odd mass reported at horizon `L` is

`M_L = sum_{unordered reversal pairs {w,Rw}} |Delta_L(w)|`.

This equals the total-variation distance between `P_L` and its reversal.

## 4. Temporal marginalization

Dropping the last symbol maps an `(L+1)`-symbol stationary path law to the horizon-`L-1` law. For stationary path distributions, this marginalization commutes with the reversal-odd construction:

`marginalize(O_L) = O_{L-1}`.

Hence if `L_arrow=k>1`, then the first nonzero odd component satisfies

`O_k != 0` but `marginalize(O_k)=O_{k-1}=0`.

Stage 5 calls this a **first-detection odd component in the kernel of temporal marginalization**. This is a precise statement about finite path laws; it is not an ontological claim about time.

## 5. Micro-to-macro cancellation identity

For deterministic observation `g` and an observed word `w`,

`P_g(w) = sum_{x:g(x_t)=w_t} P_X(x)`.

Therefore

`Delta_g(w) = P_g(w)-P_g(Rw)`

can be decomposed exactly as

`Delta_g(w) = sum_{x:g(x_t)=w_t} [P_X(x)-P_X(Rx)]`.

Stage 5 records every compatible microtrajectory contribution for selected shortest witnesses, separating:

- positive contributions;
- negative contributions;
- exactly cancelling/zero contributions;
- the signed residual after cancellation.

This makes the coarse-graining mechanism inspectable rather than treating `L_arrow` as a black-box label.

## 6. Frozen representative observations

Exactly four representative partitions are used for detailed comparison:

- order 1: `0|12|3`;
- order 2: `0|1|23`;
- order 3: `01|23`;
- all-horizon hidden: `02|1|3`.

The finite representatives use the shortest mismatch word returned by the Stage 4 exact equivalence machinery. The `infinity` representative is not assigned a finite motif; its all-horizon vanishing is inherited from the exact equivalence certificate, not from a finite scan.

## 7. Stage 5 outputs

The executable synthesis must report:

1. the 15-partition detection-class census from the frozen witness;
2. for every finite class, exact first-detection odd-pair count and odd mass;
3. horizon `1..3` odd profiles for the four frozen representatives;
4. exact temporal-marginalization checks;
5. microtrajectory cancellation summaries for the three finite representatives;
6. a clear separation between finite representative structure and any general statement.

Primary artifacts:

- `docs/stage5_protocol.md`;
- `docs/stage5_proofs.md`;
- `src/r_arrow/temporal_order.py`;
- `src/r_arrow/stage5.py`;
- `results/stage5_temporal_order_hierarchy.md`;
- `results/stage5_temporal_order_hierarchy.json`.

## 8. Success contract

Stage 5 succeeds if all of the following hold:

1. the exact reversal-odd hierarchy is implemented and `O_L=0 <=> A_L=0` is regression-tested on the frozen observations;
2. Stage 4 classes `1,2,3,infinity` are reproduced without enlarging the horizon search;
3. first-detection odd components marginalize to zero at the preceding horizon for the order-2 and order-3 representatives;
4. exact micro-to-macro contribution sums reproduce the selected macro reversal differences;
5. the result states honestly whether a compact motif/partition criterion beyond this exact decomposition was or was not established.

A negative result on a compact criterion still satisfies the contract.

## 9. Guards

`temporal order != arrow strength`

`higher-order odd component != newly created physical arrow`

`microtrajectory cancellation != destruction of microscopic irreversibility`

`kernel of temporal marginalization != hidden ontological time`

`L_arrow=infinity under g != microscopic reversibility`

`representative motif != universal motif taxonomy`

`finite four-state hierarchy != arbitrary-order theorem`

`observable trajectory irreversibility != ontological becoming`

## 10. Stop rule

Stage 5 stops after explaining the already frozen `L_arrow=1,2,3,infinity` classes of the existing four-state witness with exact odd components and representative cancellation decompositions.

Do not add five-state models, extend to larger detection depths, introduce computational mechanics/minimal-memory machinery, or select Stage 6 on this branch.