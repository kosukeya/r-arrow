# r-arrow

**r-arrow — Robustness of Observable Time Asymmetry under Coarse-Graining**

`r` stands for **Robustness**.

r-arrow studies which measurable signatures of temporal direction survive loss of information under coarse-graining in finite stochastic systems.

## Current status

The project is implemented through bounded Stage 3 structural criteria:

- **Stage 0** — foundations / research question / success contract — complete;
- **Stage 1** — exact three-state reversible/irreversible arrow calibration — complete;
- **Stage 2** — complete four-state state-partition survival census and first Arrow Survival Map — complete;
- **Stage 3** — structural criteria for one-step arrow visibility plus a bounded higher-order separation — implemented;
- **Stage 4+** — intentionally not selected.

The Stage 0 Minimum Research Success contract was satisfied by Stages 1–2. Stage 3 is a second, bounded theoretical step: it explains the Stage 2 one-step split exactly and identifies where one-step structural information stops being sufficient.

## Primary question

> In finite stationary stochastic systems with measurable time-reversal asymmetry, how much of that asymmetry survives deterministic loss of state information under coarse-graining, and which coarse-grainings preserve, attenuate, or hide it at finite observation horizons?

## Primary observable

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

1. **Adjacent-pair three-state merges retain the arrow.** All four rotationally equivalent adjacent merges have `r_1=0.75`, rising to `r_4≈0.947203`.
2. **Opposite-pair three-state merges are undetected through `L=4`.** They have `A_L=0` for every frozen horizon.
3. **All seven two-macrostate observations are undetected through `L=4`.**
4. **No `memory_revealed_arrow` occurs for `L=1..4` in the frozen Stage 2 cycle.**
5. **Non-lumpability is not sufficient for arrow visibility.** Representative adjacent and opposite three-state merges are both non-lumpable, but only the adjacent merge retains the arrow.
6. **Every declared case satisfies the KL/data-processing bounds** `0 <= r_L <= 1`.

The key finite structural contrast is:

> the number of retained macro states does not by itself determine observable arrow survival; which microstates are identified matters.

Artifacts:

- `results/stage2_arrow_survival_map.md`
- `results/stage2_arrow_survival_map.csv`

## Stage 3 structural criteria

Stage 3 asks why the Stage 2 observation maps behave differently rather than enlarging the Stage 2 census.

### One-step criterion

For stationary macro flux

`F_ab = sum_{i in a} sum_{j in b} pi_i P_ij`,

we have exactly

`A_1(g) = D_KL(F || F^T)`.

Therefore

> `A_1(g)=0` if and only if the exact macro-flux matrix is symmetric.

This criterion reproduces all 14 Stage 2 one-step classifications with zero mismatches.

### Binary horizon floor and higher-order witness

For any stationary process on two observed symbols,

`A_1=A_2=0`.

Thus `L=3` is the first horizon at which a stationary binary observation can possibly reveal trajectory-reversal asymmetry.

Stage 3 includes a strictly positive four-state Markov witness with binary partition `01|23` for which

- the exact one-step macro flux is symmetric;
- observed paths are reversal-symmetric at `L=1,2`;
- observed paths are asymmetric at `L=3`;
- `A_3≈0.000709980636` and `A_4≈0.001485176667`.

So the one-step criterion is complete for `L=1` but not for arbitrary later horizons:

`one-step macro-flux symmetry != all-horizon trajectory reversibility`.

Artifacts:

- `docs/stage3_protocol.md`
- `docs/stage3_proofs.md`
- `results/stage3_structural_criteria.md`
- `results/stage3_structural_criteria.json`

## First-cycle Minimum Research Success — satisfied

The first cycle succeeded because it:

1. exactly distinguished a reversible control from a biased irreversible cycle;
2. computed coarse-grained trajectory probabilities without an unjustified Markov approximation;
3. exhaustively evaluated all 13 proper coarse-grainings plus the identity for `L=1..4`;
4. validated the expected KL/data-processing bounds;
5. explained an exact same-resolution structural contrast: adjacent-pair merges retain the arrow while opposite-pair merges do not within the frozen horizon.

A known/replicated finite result can satisfy this contract. Novelty is not required for this first-cycle success.

## Core guards

`observable irreversibility != ontological becoming`

`path-level time asymmetry != thermodynamic entropy production without additional physical assumptions`

`coarse-grained arrow loss != microscopic reversibility`

`undetected_through_L4 != absence of all higher-order time asymmetry`

`one-step macro-flux symmetry != all-horizon reversibility`

`A_1=0 != no hidden arrow`

`binary A_1=A_2=0 != binary all-horizon reversibility`

`non-lumpability != observable arrow`

`non-Markov observed dynamics != fundamental memory ontology`

`finite witness != universal higher-order classification theorem`

`exact finite-model result != empirical discovery`

`known result != meaningless result`

## Methodological rule

Do not enlarge the state space, observation horizon, or model class merely because a preferred effect is absent. Stage 3 stops after its bounded one-step theorem, binary floor result, and four-state higher-order witness. Stage 4 is not selected automatically; Stage 3 should be reviewed for scientific meaning and literature position first.
