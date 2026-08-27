# Stage 2 — Four-State Coarse-Graining Survival Census

## Status

This report records the frozen Stage 2 result for the first r-arrow research cycle.

Stage 2 asks a deliberately finite question:

> For the frozen four-state irreversible cycle, which deterministic state partitions preserve, attenuate, or hide trajectory-level time-reversal asymmetry at horizons `L=1..4`?

The result is a finite classification of the declared observation family. It is not a universal theorem about coarse-graining or time.

## Benchmark

Microstates: `{0,1,2,3}` on the directed cycle

`0 -> 1 -> 2 -> 3 -> 0`

with transition probabilities

- clockwise `p=1/2`;
- counterclockwise `q=1/4`;
- self-loop `s=1/4`.

The stationary distribution is uniform. The full-state trajectory arrow is

`A_L(identity) = (L/4) ln 2`

for `L=1..4`, numerically:

| L | A_L(identity) |
|---:|---:|
| 1 | 0.173286795140 |
| 2 | 0.346573590280 |
| 3 | 0.519860385420 |
| 4 | 0.693147180560 |

## Observation family

All 15 set partitions of four microstates are enumerable exactly.

The frozen primary census excludes only the one-block observation and therefore contains:

- 1 identity observation;
- 13 proper coarse-grainings;
- 14 primary observations total.

For every observation, the macro trajectory law is computed by summing all compatible microtrajectory probabilities. No first-order Markov approximation replaces this exact law.

## Arrow Survival Map

`r_L = A_L(g) / A_L(identity)`.

| partition | macro states | r_1 | r_2 | r_3 | r_4 | frozen classification | L* | lumpable |
|---|---:|---:|---:|---:|---:|---|---:|---|
| `0|1|2|3` | 4 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | full reference | 1 | yes |
| `0|1|23` | 3 | 0.750000 | 0.896241 | 0.929461 | 0.947203 | retained through L4 | 1 | no |
| `0|12|3` | 3 | 0.750000 | 0.896241 | 0.929461 | 0.947203 | retained through L4 | 1 | no |
| `0|13|2` | 3 | 0 | 0 | 0 | 0 | undetected through L4 | — | no |
| `01|2|3` | 3 | 0.750000 | 0.896241 | 0.929461 | 0.947203 | retained through L4 | 1 | no |
| `02|1|3` | 3 | 0 | 0 | 0 | 0 | undetected through L4 | — | no |
| `03|1|2` | 3 | 0.750000 | 0.896241 | 0.929461 | 0.947203 | retained through L4 | 1 | no |
| `0|123` | 2 | 0 | 0 | 0 | 0 | undetected through L4 | — | no |
| `01|23` | 2 | 0 | 0 | 0 | 0 | undetected through L4 | — | no |
| `012|3` | 2 | 0 | 0 | 0 | 0 | undetected through L4 | — | no |
| `013|2` | 2 | 0 | 0 | 0 | 0 | undetected through L4 | — | no |
| `02|13` | 2 | 0 | 0 | 0 | 0 | undetected through L4 | — | yes |
| `023|1` | 2 | 0 | 0 | 0 | 0 | undetected through L4 | — | no |
| `03|12` | 2 | 0 | 0 | 0 | 0 | undetected through L4 | — | no |

The corresponding `A_L` values are stored in `results/stage2_arrow_survival_map.csv`.

## Result 1 — same nominal resolution, different arrow survival

The main Stage 2 structural contrast is between adjacent-pair and opposite-pair three-state observations.

### Adjacent merge

Consider `01|2|3`, with macro states

- `A={0,1}`;
- `B={2}`;
- `C={3}`.

The exact one-step observed joint probabilities retain an oriented macro cycle:

- `Pr(A,B)-Pr(B,A)=1/16`;
- `Pr(B,C)-Pr(C,B)=1/16`;
- `Pr(C,A)-Pr(A,C)=1/16`.

Accordingly the observable arrow survives at every frozen horizon. Its retained fraction is

`0.75 -> 0.896240625180 -> 0.929460848501 -> 0.947203072883`.

By rotational symmetry the same result holds for all four adjacent-pair merges.

### Opposite merge

Consider `02|1|3`, with macro states

- `A={0,2}`;
- `B={1}`;
- `C={3}`.

Here the exact one-step observed fluxes balance:

- `Pr(A,B)=Pr(B,A)=3/16`;
- `Pr(A,C)=Pr(C,A)=3/16`;
- there is no direct `B <-> C` transition.

The observed path KL is zero for every frozen horizon `L=1..4`.

By rotational symmetry the same result holds for the other opposite-pair merge `0|13|2`.

Therefore, within the frozen benchmark:

> reducing four microstates to three macro states does not by itself determine arrow survival; which states are identified matters.

This satisfies the first-cycle requirement for a nontrivial same-resolution structural contrast.

## Result 2 — all two-macrostate observations are undetected through L4

All seven two-block partitions have

`A_1=A_2=A_3=A_4=0`.

The correct finite claim is only:

`two-state observations in the frozen family are undetected_through_L4`.

Do not infer all-horizon reversibility from this finite census.

## Result 3 — no memory-revealed arrow occurs in the frozen census

A `memory_revealed_arrow` would require

`A_1=0` and `A_L>0` for some `L in {2,3,4}`.

No declared Stage 2 observation has this pattern.

This is a valid negative result for the frozen family. The horizon is not enlarged merely to search for the preferred phenomenon.

## Result 4 — non-lumpability is not sufficient for arrow visibility

Both representative three-state coarse-grainings

- adjacent `01|2|3`;
- opposite `02|1|3`

are not strongly lumpable.

Yet the first retains a positive arrow while the second is undetected through `L=4`.

Thus, in this finite benchmark:

`non-lumpability != observable time-reversal asymmetry`.

Likewise, non-Markovian effective structure alone must not be interpreted as a time arrow or as ontological memory.

## Data-processing validation

Every declared result satisfies

`0 <= A_L(g) <= A_L(identity)`

and therefore

`0 <= r_L(g) <= 1`

within the declared numerical tolerance.

The identity observation exactly reproduces the micro trajectory law.

## First-cycle success contract

The scientific outputs now realize all five frozen Minimum Research Success conditions:

1. Stage 1 exactly discriminated reversible and irreversible benchmarks.
2. Stage 2 computes observed paths by exact microtrajectory summation without re-Markovization.
3. All 14 primary observations are evaluated for `L=1..4`.
4. KL/data-processing bounds are validated throughout the census.
5. Adjacent vs opposite three-state merges provide an exact same-resolution structural contrast.

The repository should be called first-cycle complete only after the result artifacts and tests pass together on the synchronized Stage 2 head.

## Interpretation guards

`observable irreversibility != ontological becoming`

`coarse-grained arrow loss != microscopic reversibility`

`undetected_through_L4 != absent_at_all_horizons`

`non-lumpability != observable arrow`

`non-Markov observed dynamics != fundamental memory ontology`

`finite partition census != universal coarse-graining theorem`

`exact finite-model result != empirical discovery`

## Primary finite conclusion

> In the frozen four-state cycle, observable time-reversal asymmetry is sensitive to the structure of information loss, not merely to the number of retained macro states: adjacent-pair three-state coarse-grainings retain the arrow, whereas opposite-pair three-state coarse-grainings and every two-state coarse-graining are undetected through `L=4`.
