# r-arrow Research Question

## Status

Stage 0 foundation document. This file freezes the initial research question for the first r-arrow research cycle (Stages 0–2).

## Name

**r-arrow — Robustness of Observable Time Asymmetry under Coarse-Graining**

The official meaning of `r` is **Robustness**.

A secondary mathematical use of `r` is permitted for a retained-arrow ratio defined in the Stage 0 protocol, but the project name does not depend on that particular estimator surviving later refinement.

## Primary research question

> **In finite stationary stochastic systems with measurable time-reversal asymmetry, how much of that asymmetry survives deterministic loss of state information under coarse-graining, and which coarse-grainings preserve, attenuate, or hide it at finite observation horizons?**

The first research cycle deliberately asks this question only for small finite discrete-time Markov chains and exact finite state partitions.

## Why this question

The project does **not** begin by asking whether time itself objectively becomes. It begins with a quantity that can be defined and checked within stochastic-process theory: statistical distinguishability between forward and time-reversed observed trajectories.

The methodological pattern inherited from t-search is:

`raw phenomenon -> declared transformation -> surviving measurable structure`.

The transformation studied here is information loss induced by a deterministic observation map / state partition.

## Scientific target

For a stationary process `X_t`, define a finite-horizon observable arrow strength by the Kullback–Leibler divergence between the probability law of a length-`L` trajectory and that of its time reversal. For a deterministic coarse-graining `g : X -> Y`, compare the full-state arrow strength with the arrow strength of the observed process `Y_t = g(X_t)`.

The project asks:

1. Can a reversible and an irreversible finite chain be distinguished exactly by this path-level quantity?
2. How does deterministic state coarse-graining change the observable arrow strength?
3. Which partitions leave a one-step arrow visible, which hide it, and which reveal asymmetry only when longer observed histories are used?
4. Can at least one preserved/attenuated/hidden contrast be explained structurally in terms of the underlying current/cycle and the information retained by the observation map?

## Initial scope

Frozen for Stages 0–2:

- finite state spaces;
- stationary discrete-time Markov chains;
- bidirectionally supported cycle benchmarks with self-loops;
- deterministic state coarse-grainings represented by set partitions;
- exact finite-horizon path distributions;
- horizons `L in {1,2,3,4}` for the first survival census;
- natural logarithms, so KL quantities are measured in nats.

Not frozen beyond Stage 2:

- continuous-time processes;
- empirical-data inference;
- temporal subsampling;
- stochastic observation channels;
- larger graph families;
- hidden-state parameter reconstruction;
- thermodynamic interpretation beyond the path-level observable;
- any metaphysical interpretation.

## Explicit non-goals

The first research cycle does not attempt to establish any of the following:

- ontological becoming;
- the block universe or eternalism;
- a universal definition of the physical arrow of time;
- a universal coarse-graining invariant;
- a new law of thermodynamics;
- an empirical discovery;
- a theorem about arbitrary hidden Markov processes.

## Literature anchoring, not novelty claim

The project starts inside an established scientific context rather than treating coarse-grained irreversibility as a new phenomenon.

Relevant anchors include:

- U. Seifert, “From Stochastic Thermodynamics to Thermodynamic Inference,” *Annual Review of Condensed Matter Physics* 10, 171–192 (2019), DOI: 10.1146/annurev-conmatphys-031218-013554.
- G. Teza and A. L. Stella, “Exact Coarse Graining Preserves Entropy Production out of Equilibrium,” *Physical Review Letters* 125, 110601 (2020), DOI: 10.1103/PhysRevLett.125.110601.
- D. J. Skinner and J. Dunkel, “Estimating Entropy Production from Waiting Time Distributions,” *Physical Review Letters* 127, 198101 (2021), DOI: 10.1103/PhysRevLett.127.198101.
- J. Degünther, J. van der Meer, and U. Seifert, “Fluctuating entropy production on the coarse-grained level: Inference and localization of irreversibility,” *Physical Review Research* 6, 023175 (2024), DOI: 10.1103/PhysRevResearch.6.023175.
- A. M. Maier, J. H. Fritz, and U. Seifert, “Pedestrian's approach to large deviations in semi-Markov processes with an application to entropy production,” *Physical Review E* 113, 014119 (2026), DOI: 10.1103/44r5-fjdm.

These references establish that entropy production / irreversibility under partial observation and coarse-graining is a real research domain. Stage 0 makes **no claim that the r-arrow ratio or the Stage 2 survival map is novel**. Novelty is a later literature-audit question and is not required for the first research cycle to count as successful.

## Core interpretation guards

`observable irreversibility != ontological becoming`

`coarse-grained arrow loss != microscopic reversibility`

`finite-horizon non-detection != absence of all higher-order time asymmetry`

`finite Markov result != universal physical theorem`

`simulation / exact finite-model validation != empirical discovery`

`robustness over a declared observation family != representation-independent physical constant`

## First-cycle endpoint

Stages 0–2 form a complete first research cycle. Stage 3 is intentionally not selected in advance.

The cycle is considered scientifically useful if it produces a validated finite benchmark and a complete four-state coarse-graining survival map with at least one structural explanation, even if the observed phenomenon is already known in the literature.
