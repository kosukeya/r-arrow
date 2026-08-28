# Stage 4 Protocol — Observation Resolution / History Depth Trade-off

## 1. Status and purpose

Stage 4 is the bounded continuation selected after Stage 3.

Stage 3 established two facts that motivate this stage:

1. one-step observed arrow visibility is exactly characterized by stationary macro-flux asymmetry;
2. one-step symmetry does not imply all-horizon reversibility, because a binary observation can first reveal an arrow at `L=3`.

Stage 4 asks:

> How does the minimum history depth required to detect trajectory-level time asymmetry change as deterministic state observations are coarsened?

The stage is deliberately finite. It does not enlarge the hidden-state count beyond four, introduce continuous time, empirical data, stochastic observation channels, quantum models, or local-arrow alignment.

## 2. Primary quantity: exact detection depth

For a stationary finite Markov chain `X` and deterministic observation `g`, define

`L_arrow(g;X) = min { L >= 1 : A_L(g;X) > 0 }`

when such a finite horizon exists.

If the observed process is exactly equivalent to its time reverse for every finite word, write

`L_arrow(g;X) = infinity`.

This stage must not infer `infinity` from a finite unsuccessful horizon scan.

## 3. Two monotonicity propositions

### 3.1 History-depth monotonicity

For a stationary observed process,

`A_{L+1}(g;X) >= A_L(g;X)`.

Reason: marginalizing a length-`L+2` trajectory to its first `L+1` symbols maps the forward and reversed path laws to the corresponding horizon-`L` laws; KL data processing cannot increase under that marginalization.

Therefore once an arrow is detected, it remains detectable at every longer horizon.

### 3.2 Observation-coarsening monotonicity

If `g_coarse = h o g_fine`, deterministic data processing gives

`A_L(g_coarse;X) <= A_L(g_fine;X)`

for every `L`.

Hence, with `infinity` ordered after every finite horizon,

`L_arrow(g_fine;X) <= L_arrow(g_coarse;X)`.

A coarser observation can preserve the same first-detection horizon, delay it, or hide the arrow at all horizons; it cannot reveal the arrow earlier than a refinement that retains more state distinctions.

## 4. Exact all-horizon equivalence certificate

Brute-force extension to larger and larger `L` is prohibited as the primary all-horizon test.

For transition matrix `P`, stationary distribution `pi`, and deterministic observed symbols, define the stationary time-reversed chain

`P_rev[i,j] = pi[j] P[j,i] / pi[i]`.

For each observed symbol `y`, let `D_y` be the diagonal selector for microstates observed as `y`.  The probability of an observed word is represented linearly by

`pi D_y0 P D_y1 P ... D_yk P 1`.

Because `P 1 = 1`, this equals the exact stationary word probability.

Stage 4 compares the forward representation with the representation built from `P_rev` in a direct-sum difference space of dimension `2n`.  Exact rational breadth-first closure keeps only linearly independent reachable row vectors.  The reachable space has dimension at most `2n`, so closure is finite.

- If the output difference is zero on the closed reachable space, every finite observed word has equal forward and reverse probability: this is the Stage 4 all-horizon reversibility certificate.
- If a difference appears, the breadth-first search returns a shortest observed word witness and `L_arrow = word_length - 1`.

This implementation is an exact finite linear-algebra equivalence test, not a claim of a new HMP-equivalence theorem.  It follows the standard finite-dimensional equivalence viewpoint used for hidden Markov processes / weighted automata (e.g. Faigle & Schoenhuth, IEEE Transactions on Information Theory 57(3), 2011).

## 5. Frozen benchmark family

Exactly three four-state models are used:

1. `biased_four_cycle` — the Stage 2 irreversible cycle;
2. `higher_order_hidden_arrow_four_state` — the Stage 3 constructive witness;
3. `reversible_four_cycle` — a four-state detailed-balance control with clockwise = counterclockwise = `3/8` and self-loop = `1/4`.

No model with more than four hidden states is admitted in Stage 4.

## 6. Frozen observation family

For every model, evaluate all 15 set partitions of `{0,1,2,3}`, including:

- the identity observation;
- all proper nontrivial deterministic coarse-grainings;
- the one-block observation as the maximally coarse endpoint.

The partition refinement relation is part of the primary result.  Macrostate count alone is only a summary variable.

## 7. Primary artifact: Arrow Detection Frontier

For each of the 45 model/partition pairs, record:

- model name;
- canonical partition label;
- macrostate count;
- exact `L_arrow` or `infinity`;
- all-horizon equivalence status;
- shortest witness word and exact forward/reverse probabilities when finite;
- reachable equivalence-space dimension.

Also record the partition-lattice cover relations and audit

`L_arrow(fine) <= L_arrow(coarse)`

on every cover edge for every model.

The result must be machine-readable and accompanied by a human-readable synthesis.  A plot may be added later but cannot be the only result artifact.

## 8. Success contract

Stage 4 succeeds when all of the following hold:

1. exact `L_arrow` / `infinity` semantics are implemented without arbitrary horizon extension;
2. the finite forward-vs-time-reverse equivalence test is independently checked against known Stage 2 / Stage 3 cases;
3. all 15 partitions of all three frozen four-state models are classified;
4. history-depth and observation-refinement monotonicity are documented and the finite frontier has no unexplained violations;
5. the final report states what the frontier actually contains, including negative/simple outcomes, without enlarging the model family to obtain a preferred pattern.

A simple frontier, many `infinity` cases, or no new detection depth beyond those already known are all valid outcomes.

## 9. Anti-regress rules

Before Stage 4 synthesis is complete:

- no hidden-state count above 4;
- no brute-force `L=10,20,100,...` search to certify non-detection;
- no stochastic observation channels;
- no continuous time;
- no empirical or quantum extension;
- no local-arrow alignment implementation;
- no change to the trajectory-level arrow definition merely to create a more interesting frontier;
- no Stage 5 selection.

## 10. Interpretation guards

`L_arrow = infinity under g != microscopic reversibility`

`later detection != arrow created by observation`

`history-depth trade-off != universal uncertainty principle`

`partition refinement monotonicity != privileged physical observer hierarchy`

`finite HMP equivalence certificate != universal theorem about time`

`observable trajectory irreversibility != ontological becoming`
