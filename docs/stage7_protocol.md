# Stage 7 — Structural Certificates for All-Horizon Arrow Hiding

## Status

Protocol frozen after merged Stage 6.

## Research question

For the frozen four-state irreversible witness and deterministic state partitions, what exact hidden-state or representation-level structure explains observations for which

`P_forward(w) = P_reverse(w)`

for every finite observed word `w`?

Stage 7 turns the Stage 4 yes/no all-horizon equivalence certificate into an explicit structural certificate where possible.

## Frozen family

Primary:

- `higher_order_hidden_arrow_four_state()`;
- all 15 deterministic partitions of its four microstates;
- the 7 Stage 4–6 all-horizon-hidden partitions are the positive target set;
- the 8 finite-arrow partitions are negative controls.

Positive control:

- `reversible_four_cycle()` under the same partitions.

No larger state space, new benchmark family, stochastic observation channel, or higher-horizon search is introduced.

## Stage 7A — observation-preserving permutation certificate

For a permutation `sigma` of microstates require all of:

1. observation preservation: `g(sigma(x)) = g(x)` for every state;
2. stationary preservation: `pi(sigma(x)) = pi(x)`;
3. reversal conjugacy:

   `P_rev[i,j] = P[sigma(i), sigma(j)]`.

If these hold, `sigma` is an explicit sufficient certificate that the observed forward and reverse word processes are equal at every finite length.

All `n!` permutations are enumerated exactly. For `n=4`, this is only 24 candidates.

The permutation condition is treated as sufficient, not necessary.

## Stage 7B — minimal linear intertwiner certificate

If an all-horizon-hidden observation has no permutation certificate, reduce the forward and reverse observed scalar word processes to exact minimal weighted-linear realizations.

For reduced row-state realizations

`(alpha_+, {A_y^+}, beta_+)`

and

`(alpha_-, {A_y^-}, beta_-)`,

seek an invertible rational matrix `T` satisfying

- `alpha_+ T = alpha_-`;
- `A_y^+ T = T A_y^-` for every observation symbol `y`;
- `T beta_- = beta_+`.

A verified `T` is a representation-level structural certificate of equality of the complete observed word series.

The reduced dimension is obtained from exact reachable/observable Hankel pairing rank. No numerical tolerance is used.

## Certificate taxonomy

Each primary partition is classified as:

- `permutation` — at least one observation-preserving reversal-conjugating state permutation exists;
- `linear_only` — no such permutation exists, but an exact minimal linear intertwiner exists;
- `finite_arrow` — Stage 4 already supplies a distinguishing word, so no all-horizon equality certificate may be issued;
- `unresolved` — reserved only if Stage 4 says all-horizon equivalent but neither frozen certificate class is constructed.

Stage 7 succeeds even if `unresolved` occurs; the model family must not be enlarged merely to eliminate it.

## Representative explanation

If a permutation certificate exists, record a microtrajectory pairing example.

If no permutation certificate exists but a linear certificate does, record instead:

- a prefix whose forward and reverse hidden predictive rows differ;
- the corresponding reduced minimal states;
- the exact intertwiner showing that the observable predictive coordinates coincide.

This prevents pretending that a one-to-one microtrajectory pairing exists when only representation-level equivalence has been established.

## Success contract

Stage 7 succeeds when it:

1. proves and implements the exact permutation sufficient criterion;
2. completes the 7-target permutation census and the 8 finite-arrow negative-control census;
3. constructs exact minimal linear intertwiners for every positive target not permutation-certified, or records a bounded unresolved class;
4. confirms the reversible control admits the identity permutation certificate;
5. freezes a complete certificate taxonomy for all 15 primary partitions;
6. records one exact human-readable representative structural explanation.

## Anti-regress / stop rules

- no state count above 4;
- no arbitrary-horizon path search;
- no approximate symmetry search;
- no stochastic observation channels;
- no continuous time;
- no empirical data;
- no neural or quantum extension;
- no causal-state reconstruction;
- no entropy-production interpretation;
- no local-arrow alignment;
- no Stage 8 selection in this stage.

## Guards

`permutation certificate => all-horizon observed reversibility` does not imply the converse.

`linear intertwiner != literal hidden-state relabeling`.

`all-horizon observed reversibility != microscopic reversibility`.

`hidden symmetry under an observation != privileged physical observer`.

`representation equivalence != ontological equivalence`.

`observable arrow hiding != ontological blockness`.
