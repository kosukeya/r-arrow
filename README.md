# r-arrow

**r-arrow — Robustness of Observable Time Asymmetry under Coarse-Graining**

`r` stands for **Robustness**.

r-arrow studies which measurable signatures of temporal direction survive loss of information under coarse-graining in finite stochastic systems.

## Current status

The project is implemented through bounded Stage 4:

- **Stage 0** — foundations / research question / success contract — complete;
- **Stage 1** — exact three-state reversible/irreversible arrow calibration — complete;
- **Stage 2** — complete four-state state-partition survival census and first Arrow Survival Map — complete;
- **Stage 3** — one-step structural criterion plus bounded higher-order separation — complete;
- **Stage 4** — exact observation-resolution / history-depth Arrow Detection Frontier — implemented;
- **Stage 5+** — intentionally not selected.

The first-cycle Minimum Research Success contract was satisfied by Stages 1–2. Stages 3–4 are bounded theoretical continuations: Stage 3 separates one-step from higher-order arrow structure, and Stage 4 classifies exact first-detection depth across a fixed observation lattice without arbitrary horizon extension.

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

`history-depth trade-off != universal uncertainty principle`

`finite equivalence certificate != universal theorem about time`

`exact finite-model result != empirical discovery`

## Methodological rule

Do not enlarge the state space, horizon, or model family merely because a preferred effect is absent. Stage 4 replaces open-ended horizon scans with a finite all-horizon equivalence certificate and stops after the fixed 45-case Detection Frontier. Stage 5 is not selected on this branch.
