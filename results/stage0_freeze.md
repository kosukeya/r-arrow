# Stage 0 Freeze Record

## Status

`stage0_status = foundations_frozen`

This record freezes the first-cycle r-arrow foundation. It is a protocol checkpoint, not a scientific result.

## Frozen project identity

**r-arrow — Robustness of Observable Time Asymmetry under Coarse-Graining**

`r = Robustness`.

## Frozen primary question

> In finite stationary stochastic systems with measurable time-reversal asymmetry, how much of that asymmetry survives deterministic loss of state information under coarse-graining, and which coarse-grainings preserve, attenuate, or hide it at finite observation horizons?

## Frozen primary observable

Finite-horizon path-level time-reversal KL divergence:

`A_L = D_KL(P(path) || P(reversed path))`.

Observed/coarse-grained path probabilities must be obtained by exact summation over compatible microtrajectories. The observed process must not be silently approximated as first-order Markov for the primary Stage 1–2 result.

## Frozen robustness quantity

For irreversible reference cases:

`r_L(g) = A_L(g) / A_L(identity)`.

Official project-name meaning remains `r = Robustness` regardless of later estimator refinement.

## Frozen horizons

`L in {1,2,3,4}`.

## Frozen Stage 1 models

Three-state circulant cycle.

Irreversible benchmark:

- clockwise `p=1/2`;
- counterclockwise `q=1/4`;
- self-loop `s=1/4`.

Reversible control:

- clockwise `p=3/8`;
- counterclockwise `q=3/8`;
- self-loop `s=1/4`.

## Frozen Stage 2 model

Four-state circulant cycle:

- clockwise `p=1/2`;
- counterclockwise `q=1/4`;
- self-loop `s=1/4`.

## Frozen Stage 2 observation family

All set partitions of the four microstates with at least two blocks:

- identity reference: 1;
- proper nontrivial coarse-grainings: 13;
- primary census total: 14 observations.

The one-block observation is only a sanity control.

## Frozen first-cycle success contract

The first research cycle succeeds when:

1. Stage 1 exactly distinguishes reversible and irreversible controls;
2. observed-path probabilities are computed without an unjustified Markov approximation;
3. all 13 proper Stage 2 coarse-grainings plus identity are evaluated at `L=1..4`;
4. KL/data-processing bounds are validated;
5. at least one nontrivial structural contrast is explained, or its absence in the frozen benchmark is explicitly established.

Novelty is **not** required for this success contract.

## Frozen anti-regress rule

Do not enlarge state count, horizon, model class, or ontology question before the Stage 2 result is complete merely because the hoped-for effect is absent.

Stage 3 is not selected.

## Interpretation boundary

`observable irreversibility != ontological becoming`

`coarse-grained non-detection != microscopic reversibility`

`finite-horizon non-detection != all-horizon reversibility`

`finite-model result != universal physical theorem`

`known result != meaningless result`

## Stage 0 verdict

The research question is finite, executable, outcome-neutral, and has a predeclared successful endpoint at Stage 2.

Stage 0 is ready for review and, once merged, Stage 1 may begin.
