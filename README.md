# r-arrow

**r-arrow — Robustness of Observable Time Asymmetry under Coarse-Graining**

`r` stands for **Robustness**.

r-arrow studies which measurable signatures of temporal direction survive loss of information under coarse-graining in finite stochastic systems.

## Current status

Stage 0 — foundations / research question / success contract — is frozen for review on `research/stage-0-foundations`.

The first research cycle is deliberately small:

- **Stage 0** — freeze the question, observables, benchmark family, interpretation guards, and success contract;
- **Stage 1** — exact three-state reversible/irreversible arrow benchmark;
- **Stage 2** — complete four-state state-partition survival census and first Arrow Survival Map;
- **Stage 3+** — intentionally not selected yet.

Stage 2 is a valid endpoint for the first research cycle. Novelty is not required for the cycle to count as successful.

## Primary question

> In finite stationary stochastic systems with measurable time-reversal asymmetry, how much of that asymmetry survives deterministic loss of state information under coarse-graining, and which coarse-grainings preserve, attenuate, or hide it at finite observation horizons?

## Frozen primary observable

At finite horizon `L`, r-arrow measures trajectory-level time asymmetry with

`A_L = D_KL(P(path) || P(reversed path))`.

For a deterministic coarse-graining `g`, observed trajectory probabilities are computed by summing all compatible microtrajectories. The observed process is **not** silently re-approximated as first-order Markov.

For irreversible references,

`r_L(g) = A_L(g) / A_L(identity)`.

The project name remains `r = Robustness`; this ratio is a first-cycle statistic, not the definition of the project.

## Minimum Research Success

The first cycle is successful once it:

1. exactly distinguishes a reversible control from a biased irreversible cycle;
2. computes coarse-grained trajectory probabilities without an unjustified Markov approximation;
3. exhaustively evaluates all 13 proper coarse-grainings of the frozen four-state cycle plus the identity reference for `L=1..4`;
4. validates the expected KL/data-processing bounds;
5. explains at least one nontrivial structural contrast between coarse-grainings, or establishes that no such contrast occurs in the frozen benchmark.

A known/replicated finite result can satisfy this contract.

## Stage 0 artifacts

- `docs/research_question.md`
- `docs/stage0_protocol.md`
- `results/stage0_freeze.md`

## Core guards

`observable irreversibility != ontological becoming`

`coarse-grained arrow loss != microscopic reversibility`

`finite-horizon non-detection != absence of all higher-order time asymmetry`

`finite Markov result != universal physical theorem`

`known result != meaningless result`

## Methodological rule

Do not enlarge the state space, observation horizon, or model class merely because a preferred effect is absent. Finish the frozen Stage 2 census first, evaluate the success contract, and only then decide whether a Stage 3 is scientifically justified.
