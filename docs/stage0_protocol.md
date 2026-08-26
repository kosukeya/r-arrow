# Stage 0 Protocol — Foundations and Success Contract

## 0. Status and authority

This document freezes the executable conceptual contract for the first r-arrow research cycle.

Stages 1–2 may implement this contract, but they must not silently redefine its primary observable, benchmark family, finite observation family, or minimum-success rule. Any necessary change must be documented explicitly as a protocol revision before interpreting new results.

Stage 3 and beyond are intentionally **not frozen**.

## 1. Project name

**r-arrow — Robustness of Observable Time Asymmetry under Coarse-Graining**

Officially:

`r = Robustness`.

## 2. Primary object

Let `X_t` be a stationary discrete-time Markov chain on a finite state space `X={0,...,n-1}` with transition matrix `P` and stationary distribution `pi`.

For a path

`gamma=(x_0,...,x_L)`,

define its stationary forward probability

`Pr_X(gamma)=pi[x_0] * product_{t=0}^{L-1} P[x_t,x_{t+1}]`.

Define the reversed path

`gamma^R=(x_L,...,x_0)`.

The frozen finite-horizon arrow strength is

`A_L(X) = D_KL(Pr_X(gamma) || Pr_X(gamma^R))`

or explicitly

`A_L(X)=sum_gamma Pr_X(gamma) log(Pr_X(gamma)/Pr_X(gamma^R))`.

Conventions:

- logarithms are natural;
- `0 log(0/q)=0`;
- if a forward-positive path has zero reverse probability, the contribution is `+infinity`;
- primary Stage 1–2 benchmarks are chosen with bidirectional cycle support so the intended arrow strengths remain finite.

`A_L >= 0` by KL non-negativity.

For a stationary reversible process, `A_L=0` for every finite `L`.

## 3. Auxiliary diagnostics

For stationary Markov chains, define the edge probability current

`J_ij = pi_i P_ij - pi_j P_ji`.

Detailed balance holds when all declared edge currents vanish:

`pi_i P_ij = pi_j P_ji`.

Stage 1 uses current/detailed-balance diagnostics as independent checks of the path-KL result. They are not substitutes for the frozen path observable.

## 4. Frozen coarse-graining semantics

A deterministic observation / coarse-graining is a surjective map

`g : X -> Y`,

equivalently a set partition of the microstate space.

The observed process is

`Y_t = g(X_t)`.

### Critical rule: do not silently re-Markovize

The coarse-grained process `Y_t` need not be first-order Markov even when `X_t` is Markov.

Therefore the primary observed path law must be computed directly:

`Pr_g(y_0,...,y_L) = sum_{x_0,...,x_L : g(x_t)=y_t for all t} Pr_X(x_0,...,x_L)`.

The frozen observed arrow strength is

`A_L(g;X) = D_KL(Pr_g(y_0,...,y_L) || Pr_g(y_L,...,y_0))`.

A fitted or aggregated one-step transition matrix may be reported later as an auxiliary diagnostic, but **must not replace this exact observed trajectory law** in Stages 1–2.

## 5. Robustness ratio

For an irreversible reference process with `A_L(id;X)>0`, define

`r_L(g;X) = A_L(g;X) / A_L(id;X)`.

Here `id` is the full-state observation.

The ratio is dimensionless.

Because deterministic observation is a data-processing map applied to trajectories, the expected invariant is

`0 <= r_L(g;X) <= 1`.

Stage 1–2 implementations must test this numerically/exactly for every declared case.

For reversible controls, `A_L(id;X)=0`, so `r_L` is **not applicable**, not zero.

The project name does not depend on this exact ratio remaining the best summary statistic. `r` officially continues to mean Robustness even if later stages refine the statistic.

## 6. Frozen finite-horizon vocabulary

At a fixed horizon `L`:

- `preserved_at_L`: `r_L = 1`;
- `retained_at_L`: `0 < r_L < 1`;
- `undetected_at_L`: `r_L = 0`.

Use `erased_at_L` only as an informal synonym for `undetected_at_L`.

Never infer

`undetected_at_L => no time asymmetry at larger horizons`.

For the frozen horizon set `H={1,2,3,4}`, define

`L_star(g) = min {L in H : A_L(g;X)>0}`

when such an `L` exists.

If `A_1=0` but `A_L>0` for some later frozen horizon, classify the observation as

`memory_revealed_arrow`.

If no asymmetry is detected for `L<=4`, classify it only as

`undetected_through_L4`.

This is not a proof of all-horizon reversibility.

## 7. Stage 1 frozen benchmark family

Stage 1 uses a three-state cyclic chain with states `{0,1,2}`.

### 7.1 Irreversible benchmark

For indices modulo 3:

- clockwise: `P[i,i+1]=p=1/2`;
- counterclockwise: `P[i,i-1]=q=1/4`;
- self-loop: `P[i,i]=s=1/4`.

This circulant chain has the uniform stationary distribution.

Expected analytical checks:

- nonzero cycle current;
- detailed balance violated;
- `A_L > 0`;
- with the frozen parameters, the expected path-KL growth is linear in `L` and should agree with the direct enumeration oracle.

### 7.2 Reversible control

Use the same three-state topology with

- `p=q=3/8`;
- `s=1/4`.

Expected checks:

- zero edge current;
- detailed balance satisfied;
- `A_L=0` for every tested `L`.

### 7.3 Stage 1 horizon

Validate `L in {1,2,3,4}` by exact path enumeration.

No Monte Carlo estimator is needed for the Stage 1 primary result.

## 8. Stage 2 frozen benchmark and observation family

Stage 2 uses a four-state cyclic chain `{0,1,2,3}` with the same biased-cycle parameters:

- `P[i,i+1]=1/2`;
- `P[i,i-1]=1/4`;
- `P[i,i]=1/4`;
- indices modulo 4.

The full-state observation is the reference.

### 8.1 Observation family

Enumerate **all set partitions of the four microstates with at least two blocks**.

There are 15 set partitions in total for four elements; excluding the one-block observation leaves 14 declared observations:

- 1 identity/full-state observation;
- 13 proper nontrivial coarse-grainings.

The one-block map may be evaluated as a sanity control but is not part of the primary 14-observation survival census.

### 8.2 Frozen horizons

For every declared observation, compute exact observed path distributions and

`A_L(g;X), r_L(g;X)`

for

`L in {1,2,3,4}`.

### 8.3 Stage 2 primary artifact

Produce one **Arrow Survival Map** containing, for every declared partition:

- canonical partition label;
- number of macro states;
- `A_1, A_2, A_3, A_4`;
- `r_1, r_2, r_3, r_4` when applicable;
- frozen-horizon classification;
- `L_star` when detected;
- whether the observed process is lumpable / first-order Markov, if that diagnostic is implemented reliably;
- a short structural note.

The first result must not depend on a plot alone; machine-readable/tabular output is required.

## 9. Minimum Research Success contract

The first r-arrow research cycle is declared **successful** once all of the following are satisfied:

1. **Benchmark discrimination** — the Stage 1 reversible control gives zero path-level arrow strength while the biased cycle gives a positive value, with independent current/detailed-balance checks.
2. **Exact observed-path computation** — coarse-grained path probabilities are computed by summing compatible microtrajectories, without assuming the observed process is Markov.
3. **Complete finite census** — all 13 proper coarse-grainings of the frozen four-state Stage 2 benchmark are evaluated, together with the identity reference, for `L=1..4`.
4. **Validated robustness bounds** — every finite result satisfies the expected KL/data-processing inequalities within exact arithmetic or a declared numerical tolerance.
5. **At least one structural explanation** — the final Stage 2 report explains at least one nontrivial contrast between two coarse-grainings that lose the same nominal number of states but retain different amounts/orders of time-asymmetry information, **or** reports clearly that no such contrast occurs in the frozen benchmark.

Passing these five conditions is a meaningful first-cycle result even if every phenomenon observed is already known in prior literature.

`replication / finite classification can satisfy Minimum Research Success`.

`novelty is not required for Minimum Research Success`.

## 10. Success is outcome-neutral

The project must count the following as valid outcomes:

- some partitions retain the arrow and some hide it;
- every proper partition attenuates it;
- all partitions with a given macrostate count behave identically;
- higher-order histories reveal asymmetry hidden at `L=1`;
- no higher-order recovery occurs through `L=4`;
- a simple structural rule explains the census;
- no simple structural rule explains the census.

A result is not judged unsuccessful because it is less surprising than hoped.

## 11. Stop / anti-regress rules

To prevent the first cycle from turning into an open-ended search:

1. Do not increase state count beyond 4 before the Stage 2 report is complete.
2. Do not extend `L>4` merely because a preferred effect was not found.
3. Do not add continuous time, stochastic observation channels, temporal coarse-graining, or empirical data before the Stage 2 report.
4. Do not redefine the arrow metric merely to obtain a positive or novel-looking result.
5. Do not treat a literature finding that the phenomenon is known as a reason to abandon the first cycle; record it as replication/context and finish the finite census.
6. Do not select Stage 3 until Stage 2 is complete and the first-cycle success contract has been evaluated.
7. If a primary implementation path fails, simplify the implementation while preserving the frozen mathematical question rather than expanding model complexity.

## 12. Interpretation guards

`observable irreversibility != ontological becoming`

`path-level time asymmetry != thermodynamic entropy production without additional physical assumptions`

`coarse-grained arrow loss != microscopic reversibility`

`undetected_at_L != absent_at_all_horizons`

`non-Markov observed dynamics != fundamental memory ontology`

`finite partition census != universal coarse-graining theorem`

`r_L over declared partitions != representation-independent physical constant`

`exact finite-model result != empirical discovery`

`known phenomenon != meaningless result`

## 13. Evidence hierarchy for the first cycle

When claims conflict, prefer:

1. exact mathematical definitions and executable enumeration;
2. independent analytical oracle / identities;
3. tests and machine-readable result tables;
4. result reports;
5. interpretive prose.

## 14. Stage boundaries

### Stage 0 — Foundations and success contract

Complete when this protocol, the research-question document, and the freeze record agree.

### Stage 1 — Exact three-state arrow benchmark

Goal: establish trusted reversible/irreversible path-level diagnostics.

### Stage 2 — Four-state coarse-graining survival census

Goal: produce the complete frozen Arrow Survival Map and evaluate the Minimum Research Success contract.

### Stage 3+

**Not selected.**

Possible later directions are hypotheses, not roadmap commitments.
