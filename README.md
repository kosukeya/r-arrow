# r-arrow

**r-arrow — Robustness of Observable Time Asymmetry under Coarse-Graining**

`r` stands for **Robustness**.

r-arrow studies which measurable signatures of temporal direction survive loss of information under coarse-graining in finite stochastic systems.

## Current status

The project is implemented through bounded Stage 6:

- **Stage 0** — foundations / research question / success contract — complete;
- **Stage 1** — exact three-state reversible/irreversible arrow calibration — complete;
- **Stage 2** — complete four-state state-partition survival census and first Arrow Survival Map — complete;
- **Stage 3** — one-step structural criterion plus bounded higher-order separation — complete;
- **Stage 4** — exact observation-resolution / history-depth Arrow Detection Frontier — complete;
- **Stage 5** — exact temporal-order reversal-odd hierarchy and micro-to-macro cancellation analysis — complete;
- **Stage 6** — exact recursive arrow filtering and Memory–Depth linear-realization census — implemented;
- **Stage 7+** — intentionally not selected.

The first-cycle Minimum Research Success contract was satisfied by Stages 1–2. Stages 3–6 are bounded theoretical continuations: Stage 3 separates one-step from higher-order arrow structure, Stage 4 classifies exact first-detection depth across a fixed observation lattice, Stage 5 explains those depth classes as the first surviving time-reversal-odd temporal order, and Stage 6 separates raw detection depth from exact recursive representation complexity.

## Primary observable

At finite horizon `L`, r-arrow measures trajectory-level time asymmetry with

`A_L = D_KL(P(path) || P(reversed path))`.

For deterministic coarse-graining `g`, observed trajectory probabilities are exact sums over compatible microtrajectories; the observed process is not silently re-Markovized.

## Stage 1 calibration

The biased three-state cycle has `A_L=(L/4) ln 2` for `L=1..4`, nonzero current, and violated detailed balance. The reversible control has zero current and `A_L=0`.

Artifacts:

- `results/stage1_baseline.md`
- `results/stage1_baseline.json`

## Stage 2 Arrow Survival Map

The frozen biased four-state cycle was evaluated under all 13 proper deterministic coarse-grainings plus the identity for `L=1..4`.

Key result:

> the number of retained macro states does not determine arrow survival; which microstates are identified matters.

Adjacent-pair three-state merges retain the arrow, opposite-pair three-state merges are undetected through `L=4`, and all seven two-state observations are undetected through `L=4`.

Artifacts:

- `results/stage2_arrow_survival_map.md`
- `results/stage2_arrow_survival_map.csv`

## Stage 3 structural criteria

For exact stationary macro flux `F`,

`A_1(g) = D_KL(F || F^T)`.

Hence `A_1=0` iff the macro-flux matrix is symmetric. The criterion reproduces every Stage 2 one-step classification.

For any stationary binary process, `A_1=A_2=0`, so `L=3` is the earliest possible binary detection horizon. Stage 3 constructs a strictly positive four-state witness with partition `01|23` for which `A_1=A_2=0` but `A_3>0`.

Artifacts:

- `docs/stage3_protocol.md`
- `docs/stage3_proofs.md`
- `results/stage3_structural_criteria.md`
- `results/stage3_structural_criteria.json`

## Stage 4 Arrow Detection Frontier

Stage 4 defines

`L_arrow(g;X) = min {L>=1 : A_L(g;X)>0}`,

and uses `L_arrow=infinity` only when exact finite linear-algebra equivalence certifies that the observed process equals its time reverse for every finite word.

The frozen family is deliberately small:

- Stage 2 biased four-cycle;
- Stage 3 higher-order witness;
- reversible four-cycle control;
- all 15 partitions of four states for each model (45 cases).

Primary findings:

1. **Stage 2 finite non-detections close exactly.** The nine primary observations previously `undetected_through_L4` are all certified all-horizon reversible under those observation maps.
2. **The Stage 3 witness realizes four detection classes.** Across its partitions: 4 have `L_arrow=1`, 2 have `L_arrow=2`, 2 have `L_arrow=3`, and 7 have `L_arrow=infinity`.
3. **Macrostate count is insufficient.** Among its six three-state observations, `L_arrow` can be `1`, `2`, or `infinity`; among its seven binary observations, two have `L_arrow=3` and five have `infinity`.
4. **Refinement monotonicity holds throughout.** Across the 31 partition-lattice cover edges and all three models (93 checks), there are zero violations of `L_arrow(fine) <= L_arrow(coarse)`.
5. **The reversible control remains all-horizon reversible under all 15 observations.**

Artifacts:

- `docs/stage4_protocol.md`
- `docs/stage4_proofs.md`
- `results/stage4_detection_frontier.md`
- `results/stage4_detection_frontier.csv`

## Stage 5 temporal-order hierarchy

Stage 5 defines the exact reversal-odd component of the observed horizon-`L` path law by

`O_L(w) = [P_L(w)-P_L(reverse(w))]/2`.

Then

`O_L=0 <=> A_L=0`,

so `L_arrow` is exactly the lowest temporal order whose observed reversal-odd component is nonzero.

For stationary path laws,

`marginalize(O_L)=O_(L-1)`.

Thus the order-2 and order-3 frozen representatives are genuinely higher-order: their first nonzero odd component disappears exactly when one temporal step is marginalized away.

The same frozen Stage 3/4 witness still has detection classes `1,2,3,infinity` with counts `4,2,2,7`. Exact first-detection odd masses show that temporal order is distinct from magnitude: the two `L_arrow=3` binary observations have masses `27/2048` and `27/4096`.

For selected shortest witnesses, Stage 5 decomposes each macro word/reverse difference into signed microtrajectory reversal differences. Representative results are:

- order 1 `0|12|3`, witness `01`: no positive/negative cancellation; macro residual `3/64`;
- order 2 `0|1|23`, witness `021`: partial cancellation; macro residual `9/1024`;
- order 3 `01|23`, witness `0010`: multiple positive/negative micro contributions; macro residual `-27/8192`;
- all-horizon hidden `02|1|3`: no finite odd motif exists because Stage 4 already certifies complete observed reversal equivalence.

The bounded conclusion is explanatory, not universal: no partition-only formula or universal motif taxonomy predicting arbitrary `L_arrow` is claimed.

Artifacts:

- `docs/stage5_protocol.md`
- `docs/stage5_proofs.md`
- `results/stage5_temporal_order_hierarchy.md`
- `results/stage5_temporal_order_hierarchy.json`

## Stage 6 Memory–Depth Map

Stage 6 asks a different question from Stage 4–5:

> once arrow-relevant information is distributed across history, how much exact internal state is needed to update forward-versus-reverse evidence without retaining the raw prefix?

It implements an exact recursive filter containing forward and time-reversed hidden-state predictive rows. Their sums reproduce exact observed word likelihoods, so arbitrarily long raw prefixes can be compressed into a fixed finite-dimensional state for the frozen finite hidden-state family.

The current scalar likelihood ratio alone is **not** recursively sufficient in the finite-arrow cases. All eight finite-arrow partitions have an exact prefix-length-`<=3` counterexample: two prefixes have the same current ratio but update to different ratios after the same next symbol. Representative examples include:

- order 1 `0|12|3`: `Lambda(1)=Lambda(0)=1`, but `Lambda(10)=8/11` while `Lambda(00)=1`;
- order 2 `0|1|23`: `Lambda(02)=Lambda(0)=1`, but `Lambda(021)=32/23` while `Lambda(01)=1`;
- order 3 `01|23`: `Lambda(001)=Lambda(0)=1`, but `Lambda(0010)=440/467` while `Lambda(00)=1`.

Stage 6 then computes exact weighted-linear minimal realization ranks. The same joint forward/reverse rank `6` occurs at three different detection depths:

- `0|12|3`: `L_arrow=1`, joint rank `6`;
- `0|1|23`: `L_arrow=2`, joint rank `6`;
- `01|23`: `L_arrow=3`, joint rank `6`.

Even within `L_arrow=1`, `0|13|2` has joint rank `4` while the other order-1 observations have rank `6`. Therefore raw temporal depth and exact linear representation dimension are distinct axes.

A separate reversal-contrast rank is computed for the signed series `P_forward-P_reverse`. Every all-horizon-hidden observation has contrast rank `0`, while its joint observed-process rank can remain `1` or `2`. Thus process representation complexity and directional contrast complexity also separate.

The reversible four-cycle control has contrast rank `0` under all 15 partitions.

Stage 6 does **not** interpret these ranks as physical memory bits or a unique nonlinear minimal discriminator memory. Computational-mechanics causal-state complexity is also not inferred: no open-ended or approximate mixed-state closure search is performed.

Artifacts:

- `docs/stage6_protocol.md`
- `docs/stage6_proofs.md`
- `results/stage6_memory_depth_map.md`
- `results/stage6_memory_depth_map.json`

## First-cycle Minimum Research Success — satisfied

The first cycle succeeded because it:

1. exactly distinguished reversible and irreversible benchmarks;
2. computed coarse-grained path laws without unjustified Markov approximation;
3. completed the frozen Stage 2 partition census;
4. validated KL/data-processing bounds;
5. explained a same-resolution structural contrast.

Novelty was not required for this finite success contract.

## Core guards

`observable irreversibility != ontological becoming`

`path-level time asymmetry != thermodynamic entropy production without additional physical assumptions`

`coarse-grained arrow loss != microscopic reversibility`

`one-step macro-flux symmetry != all-horizon reversibility`

`A_1=0 != no hidden arrow`

`L_arrow=infinity under g != microscopic reversibility`

`later detection != arrow created by observation`

`same macrostate count != same detection depth`

`temporal order != arrow strength`

`history depth != internal memory complexity`

`linear realization rank != physical memory bits`

`joint likelihood rank != uniquely defined nonlinear minimal discriminator memory`

`contrast rank != predictive complexity`

`likelihood ratio at one instant != sufficient recursive state in the frozen finite-arrow family`

`higher-order odd component != newly created physical arrow`

`microtrajectory cancellation != destruction of microscopic irreversibility`

`representative motif != universal motif taxonomy`

`finite equivalence certificate != universal theorem about time`

`exact finite-model result != empirical discovery`

## Methodological rule

Do not enlarge the state space, horizon, or model family merely because a preferred effect is absent. Stage 6 stops after the exact four-state Memory–Depth census, recursive-filter sufficiency audit, and reversible controls. It does not start open-ended causal-state reconstruction, approximate memory inference, larger hidden-state families, or Stage 7 selection.
