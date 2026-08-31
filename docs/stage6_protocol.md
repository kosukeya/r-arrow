# Stage 6 Protocol — Minimal Memory for Observable Arrow Detection

## Status

Stage 6 is a bounded continuation of merged Stage 5.

The question is no longer only how far back an observer must look (`L_arrow`), but how much exact internal state is needed to update forward-versus-reverse evidence recursively without retaining the raw history.

## Frozen primary question

> For the fixed Stage 3–5 four-state observed processes, how much exact finite-dimensional internal state is needed to preserve recursive forward/reverse likelihood information, and how does that representation complexity compare with the temporal detection depth `L_arrow`?

## Core distinction

Stage 6 separates four notions that must not be conflated:

1. `L_arrow` — first temporal order at which observed reversal asymmetry is nonzero;
2. current likelihood ratio — present forward/reverse evidence for one observed prefix;
3. minimal joint linear realization rank — smallest exact linear state dimension sufficient to generate both forward and reverse word likelihoods;
4. reversal-contrast rank — smallest exact linear state dimension of the signed series `P_forward - P_reverse`.

Neither linear rank is called a physical memory in bits.

## Stage 6A — Exact recursive arrow filter

For a deterministic observation map `g`, maintain two unnormalized predictive rows after an observed prefix `w`:

`r_+(w) = pi D_y0 P ... D_yk P`

`r_-(w) = pi D_y0 P^R ... D_yk P^R`.

Their row sums are exactly the observed prefix likelihoods

`p_+(w)` and `p_-(w)`.

The pair `(r_+, r_-)` can be updated symbol by symbol, so the raw prefix need not be stored.

The likelihood ratio is

`Lambda(w) = p_+(w) / p_-(w)`

when the denominator is positive.

## Stage 6B — Likelihood-ratio sufficiency audit

A scalar current ratio is recursively sufficient only if any two prefixes with the same current ratio necessarily produce the same updated ratio after every common next symbol.

Stage 6 searches only the already-frozen representative depth `<=3` for explicit exact counterexamples. A counterexample proves insufficiency; failure to find one is not a universal sufficiency theorem.

For all-horizon reversible observations, Stage 4 already proves `Lambda(w)=1` for every finite observed word, so the directional task is trivial there.

## Stage 6C — Exact minimal linear realization ranks

The observed process is represented as a weighted linear system with symbol operators `D_y P`.

For the forward/reverse pair, use their direct-sum symbol operators and two output functionals. The exact minimal joint linear realization rank is the rank of the reachable/observable Hankel pairing.

Stage 6 also computes:

- forward scalar process rank;
- reverse scalar process rank;
- joint forward/reverse rank;
- signed reversal-contrast rank for `P_forward - P_reverse`.

The contrast rank is zero exactly when the observed forward and reverse word series are identical.

## Stage 6D — Frozen family census

Primary family:

- `higher_order_hidden_arrow_four_state`;
- all 15 deterministic state partitions.

Negative control:

- `reversible_four_cycle`;
- all 15 partitions if exact computation remains trivial (expected for four states).

No new hidden-state family is introduced.

## Stage 6E — Memory–Depth Map

For each primary partition record at least:

- partition label;
- macrostate count;
- `L_arrow` from exact Stage 4 equivalence;
- forward linear rank;
- reverse linear rank;
- joint forward/reverse linear rank;
- reversal-contrast linear rank;
- whether an exact ratio-only insufficiency witness is found within the frozen prefix depth;
- the witness, if any.

Representative classes remain:

- order 1: `0|12|3`;
- order 2: `0|1|23`;
- order 3: `01|23`;
- all-horizon hidden: `02|1|3`.

## Causal-state baseline rule

Computational-mechanics causal states are not a primary Stage 6 success requirement.

A finite hidden Markov generator need not yield a finite exact causal-state machine. Stage 6 therefore does not start an open-ended mixed-state search and does not introduce approximate CSSR or simulation-based inference.

If a finite exact causal-state closure is not already certified by a bounded method, report it as not established and stop that track.

## Success contract

Stage 6 succeeds if it:

1. implements an exact recursive forward/reverse filter and validates it against direct word probabilities;
2. gives an exact representative counterexample showing whether the current likelihood ratio alone is recursively sufficient for finite-arrow observations;
3. computes exact minimal scalar, joint, and contrast linear ranks for the frozen 15-partition witness family;
4. compares those ranks with `L_arrow` without assuming a monotone relationship;
5. verifies the reversible/all-horizon-hidden controls have zero reversal-contrast rank;
6. records a machine-readable Memory–Depth Map and stops without enlarging the model family.

## Stop rules

Do not add:

- more than four hidden states;
- detection horizons beyond the already frozen Stage 5 classes merely to find a preferred effect;
- stochastic observation channels;
- continuous time;
- empirical data;
- neural/RNN memory models;
- approximate causal-state reconstruction;
- thermodynamic entropy-production assumptions;
- quantum models;
- local-arrow alignment;
- Stage 7 selection.

## Interpretation guards

`history depth != internal memory complexity`

`linear realization rank != physical memory bits`

`joint likelihood rank != uniquely defined nonlinear minimal discriminator memory`

`contrast rank != predictive complexity`

`likelihood ratio at one instant != sufficient recursive state in general`

`zero contrast rank != microscopically reversible dynamics`

`coarse-graining-induced inference memory != fundamental memory ontology`

`finite four-state result != universal theorem about observers or time`

`observable arrow memory != ontological becoming`
