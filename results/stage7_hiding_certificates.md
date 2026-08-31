# Stage 7 — Structural Certificates for All-Horizon Arrow Hiding

## Status

Stage 7 is complete for the frozen four-state family.

The Stage 4–6 question

`which observations have L_arrow=infinity?`

is refined into

`what exact structural certificate explains P_forward(w)=P_reverse(w) for every finite observed word?`

## Primary result 1 — simple hidden-state relabeling explains none of the primary cases

The complete four-state permutation group contains only `4! = 24` elements. Stage 7 exhaustively tests every permutation for every primary partition.

A permutation certificate must satisfy all of:

- `g(sigma(x))=g(x)`;
- stationary-mass preservation;
- exact reversal conjugacy `P_rev[i,j]=P[sigma(i),sigma(j)]`.

For the irreversible higher-order witness:

- permutation certificates across all 15 partitions: **0**;
- permutation certificates across the 7 all-horizon-hidden partitions: **0**.

Thus the frozen all-horizon hiding is **not** explained by a literal observation-invisible relabeling of the four hidden microstates.

This is a bounded finite-family result. The permutation criterion is sufficient, not necessary.

## Primary result 2 — all seven hidden observations are linear-only certified

Every Stage 4 all-horizon-hidden observation admits an exact invertible intertwiner between minimal forward and reverse weighted-linear realizations.

Certificate taxonomy for the primary witness:

- `finite_arrow`: **8**;
- `permutation`: **0**;
- `linear_only`: **7**;
- `unresolved`: **0**.

So every positive target is structurally closed within the frozen certificate hierarchy without enlarging the model family.

## Primary result 3 — observable minimization removes the forward/reverse difference

The seven hidden observations have minimal scalar observed-process ranks only `1` or `2`:

- rank `1`: `013|2`, `02|13`, `0123`;
- rank `2`: `02|1|3`, `0|123`, `012|3`, `023|1`.

For all seven, the independently reduced forward and reverse realizations use the same exact canonical observable coordinates and the verified intertwiner is the identity matrix in those reduced coordinates.

This does **not** mean the original four hidden states are identical forward and backward. It means that after unreachable/unobservable redundancy is quotiented out, the complete observed word process has the same minimal representation in both directions.

In this frozen family:

`different hidden forward/reverse descriptions -> same minimal observable dynamics`.

## Complete primary taxonomy

| partition | `L_arrow` | certificate class | permutation count | minimal linear rank |
|---|---:|---|---:|---:|
| `0|1|2|3` | 1 | finite_arrow | 0 | — |
| `0|1|23` | 2 | finite_arrow | 0 | — |
| `0|12|3` | 1 | finite_arrow | 0 | — |
| `0|13|2` | 1 | finite_arrow | 0 | — |
| `01|2|3` | 1 | finite_arrow | 0 | — |
| `02|1|3` | infinity | linear_only | 0 | 2 |
| `03|1|2` | 2 | finite_arrow | 0 | — |
| `0|123` | infinity | linear_only | 0 | 2 |
| `01|23` | 3 | finite_arrow | 0 | — |
| `012|3` | infinity | linear_only | 0 | 2 |
| `013|2` | infinity | linear_only | 0 | 1 |
| `02|13` | infinity | linear_only | 0 | 1 |
| `023|1` | infinity | linear_only | 0 | 2 |
| `03|12` | 3 | finite_arrow | 0 | — |
| `0123` | infinity | linear_only | 0 | 1 |

## Representative linear-only explanation — `02|1|3`

Take the observed prefix `0`.

The exact unnormalized hidden predictive rows are different:

Forward:

`(5/64, 1/8, 11/64, 1/8)`

Reverse:

`(1/8, 1/8, 1/8, 1/8)`.

So there is no claim that the forward and reverse hidden states coincide. Nevertheless both rows have the same observed word probability:

`Pr_forward(0)=Pr_reverse(0)=1/2`.

After exact observable minimization, this partition has rank `2`. The same prefix is represented in both directions by the reduced state

`(1/2, 1/8)`.

The exact minimal intertwiner is

`[[1,0],[0,1]]`.

Thus the original hidden predictive descriptions differ, while all distinctions that survive into the minimal observed process are identical forward and backward.

This is the correct representative explanation for this family. Stage 7 does not invent a one-to-one microtrajectory pairing when no microstate permutation certificate exists.

## Positive control

For the reversible four-cycle, `P=P_rev`. Therefore the identity microstate permutation is a valid observation-preserving reversal certificate under every one of the 15 partitions.

This confirms that the permutation machinery detects the transparent symmetry when it is actually present.

## Relationship to earlier stages

Stage 4:

`all-horizon equality can be decided exactly`.

Stage 5:

`all temporal-order reversal-odd components vanish`.

Stage 6:

`reversal-contrast rank is zero while process rank can remain nonzero`.

Stage 7:

`the hidden forward/reverse generators need not be related by a state permutation; nevertheless, after exact observable minimization, all seven hidden observations have identical minimal forward/reverse dynamics`.

The resulting chain is:

`observation map -> hidden distinctions become unobservable/redundant -> forward/reverse minimal observed realizations coincide -> contrast series is zero -> L_arrow=infinity`.

## What Stage 7 does not establish

Stage 7 does not prove that every all-horizon reversible hidden Markov observation must lack a permutation certificate or must reduce to the same chosen canonical coordinates in every implementation.

Minimal linear realizations are unique only up to similarity; identity intertwiners here reflect the exact deterministic reduction convention used after both directions generate the same scalar series.

No claim is made that the eliminated hidden directions are physically unreal, thermodynamically irrelevant, or ontologically redundant.

No arbitrary-HMM reversibility theorem is claimed.

## Success contract

All six frozen conditions are satisfied:

1. exact observation-preserving permutation sufficient criterion implemented and proved;
2. complete 7-target / 8-negative-control permutation census completed;
3. all seven positive targets receive exact minimal linear intertwiners;
4. reversible control receives the identity permutation certificate under all 15 observations;
5. complete taxonomy freezes `8 finite_arrow / 7 linear_only / 0 unresolved`;
6. representative hidden-row versus minimal-state explanation is recorded exactly.

## Core guards

`no permutation certificate != no all-horizon reversibility`

`linear-only certificate != literal hidden-state relabeling`

`identity in minimal coordinates != identity of hidden generators`

`observable minimization != physical elimination`

`all-horizon observed reversibility != microscopic reversibility`

`representation equivalence != ontological equivalence`

`observable arrow hiding != ontological blockness`

## Primary Stage 7 conclusion

> In the frozen irreversible four-state witness, none of the fifteen observations—including all seven all-horizon-hidden cases—admits an observation-preserving microstate permutation that conjugates the forward chain to its stationary time reverse. Nevertheless every all-horizon-hidden observation has an exact rank-1 or rank-2 minimal linear certificate: after removing hidden directions that do not survive into the observed word process, the forward and reverse minimal realizations are identical in the chosen canonical coordinates. All-horizon hiding in this family is therefore a representation-level observable equivalence rather than a literal hidden-state relabeling symmetry.
