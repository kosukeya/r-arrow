# Stage 4 — Arrow Detection Frontier

## Status

Stage 4 classifies the exact first horizon at which observed trajectory time asymmetry becomes detectable under deterministic state coarse-graining.

The primary quantity is

`L_arrow(g;X) = min { L >= 1 : A_L(g;X) > 0 }`.

`L_arrow = infinity` is used only when the finite linear-equivalence certificate proves that the complete observed word process is identical to its time reverse at every finite horizon.

The fixed census contains three four-state models and all 15 set partitions of each model: 45 model/observation pairs total.

## Result 1 — the Stage 2 finite non-detections can now be closed exactly

For the Stage 2 `biased_four_cycle`, the exact frontier is:

| partition | macro states | L_arrow |
|---|---:|---:|
| `0|1|2|3` | 4 | 1 |
| `0|1|23` | 3 | 1 |
| `0|12|3` | 3 | 1 |
| `0|13|2` | 3 | infinity |
| `01|2|3` | 3 | 1 |
| `02|1|3` | 3 | infinity |
| `03|1|2` | 3 | 1 |
| `0|123` | 2 | infinity |
| `01|23` | 2 | infinity |
| `012|3` | 2 | infinity |
| `013|2` | 2 | infinity |
| `02|13` | 2 | infinity |
| `023|1` | 2 | infinity |
| `03|12` | 2 | infinity |
| `0123` | 1 | infinity |

Counts:

- `L_arrow=1`: 5 observations;
- `L_arrow=infinity`: 10 observations.

Stage 2 had nine **primary** observations (excluding the one-block control) that were only classified as `undetected_through_L4`.  Stage 4 now proves all nine to be exactly all-horizon reversible **under those observation maps**.

This is stronger than the Stage 2 finite statement, but it does not make the underlying biased micro chain reversible.

## Result 2 — one four-state system realizes detection depths 1, 2, 3, and infinity

For `higher_order_hidden_arrow_four_state`, the frontier is:

| partition | macro states | L_arrow | shortest witness when finite |
|---|---:|---:|---|
| `0|1|2|3` | 4 | 1 | `02` |
| `0|1|23` | 3 | 2 | `021` |
| `0|12|3` | 3 | 1 | `01` |
| `0|13|2` | 3 | 1 | `01` |
| `01|2|3` | 3 | 1 | `01` |
| `02|1|3` | 3 | infinity | — |
| `03|1|2` | 3 | 2 | `001` |
| `0|123` | 2 | infinity | — |
| `01|23` | 2 | 3 | `0010` |
| `012|3` | 2 | infinity | — |
| `013|2` | 2 | infinity | — |
| `02|13` | 2 | infinity | — |
| `023|1` | 2 | infinity | — |
| `03|12` | 2 | 3 | `0010` |
| `0123` | 1 | infinity | — |

Counts:

- `L_arrow=1`: 4 observations;
- `L_arrow=2`: 2 observations;
- `L_arrow=3`: 2 observations;
- `L_arrow=infinity`: 7 observations.

The Stage 3 binary witness is recovered exactly:

- partition `01|23`;
- `L_arrow=3`;
- shortest mismatch word `0010`;
- `Pr_forward(0010)=55/1024`;
- `Pr_reverse(0010)=467/8192` (equivalently the forward probability of `0100`).

The census also adds a new finite structural contrast: among the six three-macrostate observations of this same micro process, the first-detection depth can be `1`, `2`, or `infinity`.  Therefore macrostate count alone does not determine required history depth.

Among the seven binary observations, two have `L_arrow=3` and five have `L_arrow=infinity`.  The Stage 3 stationary-binary floor `L>=3` is therefore attained but is not sufficient for detection.

## Result 3 — reversible control stays reversible under every observation

For `reversible_four_cycle`, all 15 partitions have

`L_arrow = infinity`.

This is the expected control: deterministic observation cannot create trajectory time asymmetry that is absent from the reversible micro process.

## Result 4 — refinement monotonicity has no violations

The partition lattice of four states has 31 cover relations.  Across all three models, Stage 4 audits 93 fine-to-coarse cover comparisons.

There are zero violations of

`L_arrow(fine) <= L_arrow(coarse)`

when `infinity` is ordered after every finite horizon.

Thus the frozen frontier behaves exactly as data processing predicts: removing state distinctions can keep the required history depth unchanged, delay detection, or make the observed process all-horizon reversible, but cannot make an arrow appear earlier.

## Result 5 — what the resolution/history trade-off does and does not mean

The result is not a scalar law such as `macrostate_count * L_arrow = constant`.

Instead the trade-off is a partial-order statement on observation maps:

> along a deterministic coarse-graining chain, the minimum history depth needed for detection cannot decrease.

Partition structure matters strongly.  In the Stage 3 witness, observations with the same three-symbol resolution realize `L_arrow=1`, `2`, and `infinity`.

So the primary object is the **observation-map lattice decorated by detection depth**, not macrostate count by itself.

## Exact all-horizon certificate

The Stage 4 algorithm does not scan `L=1,2,...` until a chosen cutoff.

It compares the observed forward process and the observation of the stationary time-reversed micro chain using a direct-sum finite linear representation.  Exact rational reachable-space closure has dimension at most `2n`; for the frozen four-state models this ambient bound is 8.

If a nonzero word-probability difference is generated, breadth-first closure returns a shortest counterexample.  If the reachable space closes with zero output difference, equality of every finite observed word probability is certified.

This is an implementation of the standard finite-dimensional HMP / weighted-automaton equivalence viewpoint, not a new equivalence theorem.

## Stage 4 success contract

All frozen conditions are realized:

1. `L_arrow` and exact `infinity` semantics are implemented without arbitrary horizon extension;
2. the equivalence machinery reproduces the Stage 2 adjacent/opposite distinction and the Stage 3 `L_arrow=3` binary witness;
3. all 45 model/partition pairs are classified;
4. the partition refinement frontier has zero monotonicity violations;
5. the complete finite result is reported without increasing the hidden-state count beyond four or searching larger horizons for a preferred effect.

## Interpretation guards

`L_arrow = infinity under g != microscopic reversibility`

`later detection != arrow created by observation`

`history-depth trade-off != universal uncertainty principle`

`same macrostate count != same detection depth`

`finite equivalence certificate != universal theorem about time`

`observable trajectory irreversibility != ontological becoming`

## Primary Stage 4 conclusion

> In the frozen four-state family, deterministic loss of state resolution can only preserve, delay, or completely hide the first detectable trajectory arrow along the partition-refinement order.  The required history depth is strongly partition-dependent rather than determined by macrostate count: the Stage 3 witness realizes `L_arrow=1,2,3,infinity`, while every Stage 2 observation previously undetected through `L=4` is now certified all-horizon reversible under that observation.

The complete machine-readable 45-row frontier is stored in `results/stage4_detection_frontier.csv`.
