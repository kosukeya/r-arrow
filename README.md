# r-arrow

**r-arrow — Robustness of Observable Time Asymmetry under Coarse-Graining**

`r` stands for **Robustness**.

r-arrow studies which measurable signatures of temporal direction survive loss of information under coarse-graining in finite stochastic systems.

## Current status

The first frozen research cycle is implemented through Stage 2:

- **Stage 0** — foundations / research question / success contract — complete;
- **Stage 1** — exact three-state reversible/irreversible arrow calibration — complete;
- **Stage 2** — complete four-state state-partition survival census and first Arrow Survival Map — complete;
- **Stage 3+** — intentionally not selected.

The Stage 0 Minimum Research Success contract is satisfied by the Stage 1 calibration plus the complete Stage 2 finite census. This is a deliberately small success claim: it does not require novelty and it does not establish a universal physical or ontological theorem.

## Primary question

> In finite stationary stochastic systems with measurable time-reversal asymmetry, how much of that asymmetry survives deterministic loss of state information under coarse-graining, and which coarse-grainings preserve, attenuate, or hide it at finite observation horizons?

## Frozen primary observable

At finite horizon `L`, r-arrow measures trajectory-level time asymmetry with

`A_L = D_KL(P(path) || P(reversed path))`.

For a deterministic coarse-graining `g`, observed trajectory probabilities are computed by summing all compatible microtrajectories. The observed process is **not** silently re-approximated as first-order Markov.

For irreversible references,

`r_L(g) = A_L(g) / A_L(identity)`.

The project name remains `r = Robustness`; this ratio is a first-cycle statistic, not the definition of the project.

## Stage 1 calibration

The frozen biased three-state cycle has

- `p_clockwise = 1/2`;
- `p_counterclockwise = 1/4`;
- `p_self = 1/4`;
- stationary distribution `(1/3,1/3,1/3)`;
- clockwise currents `J_01=J_12=J_20=1/12`;
- detailed balance violated;
- exact-enumeration arrow strength `A_L=(L/4) ln 2` for `L=1..4`.

The reversible control has the same stationary distribution but zero current, satisfies detailed balance, and gives `A_L=0` for `L=1..4`.

Stage 1 therefore calibrates an independently checked instrument for observable trajectory-level temporal direction.

Artifacts:

- `results/stage1_baseline.md`
- `results/stage1_baseline.json`

## Stage 2 Arrow Survival Map

Stage 2 uses the frozen four-state biased cycle with the same `p=1/2`, `q=1/4`, `s=1/4` transition rule.

All 15 set partitions of four states are enumerable exactly. The primary census contains the identity plus all 13 proper coarse-grainings, for 14 observations total, each evaluated at `L=1..4`.

Primary findings on this frozen family:

1. **Adjacent-pair three-state merges retain the arrow.** All four rotationally equivalent adjacent merges have
   `r_1=0.75`, rising to `r_4≈0.947203`.
2. **Opposite-pair three-state merges are undetected through `L=4`.** They have `A_L=0` for every frozen horizon.
3. **All seven two-macrostate observations are undetected through `L=4`.**
4. **No `memory_revealed_arrow` occurs for `L=1..4`.** No observation has `A_1=0` followed by positive `A_L` at a later frozen horizon.
5. **Non-lumpability is not sufficient for arrow visibility.** Representative adjacent and opposite three-state merges are both non-lumpable, but only the adjacent merge retains the arrow.
6. **Every declared case satisfies the KL/data-processing bounds** `0 <= r_L <= 1`.

The key finite structural contrast is therefore:

> the number of retained macro states does not by itself determine observable arrow survival; which microstates are identified matters.

Artifacts:

- `results/stage2_arrow_survival_map.md`
- `results/stage2_arrow_survival_map.csv`

## Minimum Research Success — satisfied

The first cycle succeeds because it now:

1. exactly distinguishes a reversible control from a biased irreversible cycle;
2. computes coarse-grained trajectory probabilities without an unjustified Markov approximation;
3. exhaustively evaluates all 13 proper coarse-grainings plus the identity for `L=1..4`;
4. validates the expected KL/data-processing bounds;
5. explains an exact same-resolution structural contrast: adjacent-pair merges retain the arrow while opposite-pair merges do not within the frozen horizon.

A known/replicated finite result can satisfy this contract. Novelty is not required for this first-cycle success.

## Stage 0 artifacts

- `docs/research_question.md`
- `docs/stage0_protocol.md`
- `results/stage0_freeze.md`

## Core guards

`observable irreversibility != ontological becoming`

`path-level time asymmetry != thermodynamic entropy production without additional physical assumptions`

`coarse-grained arrow loss != microscopic reversibility`

`undetected_through_L4 != absence of all higher-order time asymmetry`

`non-lumpability != observable arrow`

`non-Markov observed dynamics != fundamental memory ontology`

`finite partition census != universal coarse-graining theorem`

`exact finite-model result != empirical discovery`

`known result != meaningless result`

## Methodological rule

Do not enlarge the state space, observation horizon, or model class merely because a preferred effect is absent. Stage 3 is not selected automatically. The Stage 2 result should first be reviewed for scientific meaning and compared with relevant literature before any next research direction is frozen.
