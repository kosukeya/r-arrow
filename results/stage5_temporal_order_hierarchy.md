# Stage 5 — Temporal-Order Hierarchy of Observable Irreversibility

## Status

Stage 5 explains the already frozen Stage 4 detection-depth classes of `higher_order_hidden_arrow_four_state` in terms of exact time-reversal-odd path structure and signed microtrajectory cancellation.

It does **not** add larger state spaces or search beyond the Stage 4 detection depths.

## Result 1 — `L_arrow` is the first nonzero reversal-odd temporal order

For observed path law `P_L`, define

`O_L(w) = [P_L(w)-P_L(Rw)]/2`.

Then

`O_L=0 <=> A_L=0`.

Therefore

`L_arrow = min {L>=1 : O_L != 0}`,

with `L_arrow=infinity` only when the Stage 4 exact equivalence certificate proves `O_L=0` for every finite horizon.

For stationary path laws, dropping the final symbol satisfies

`marginalize(O_L)=O_(L-1)`.

Hence when `L_arrow=k>1`, the first nonzero odd component is lost exactly when one temporal step is removed: it lies in the kernel of temporal marginalization to order `k-1`.

This is the precise Stage 5 meaning of a higher-order observed arrow.

## Result 2 — the 15-partition detection hierarchy is reproduced exactly

For the frozen four-state witness:

| partition | macro states | `L_arrow` | first-detection odd pairs | first-detection odd mass |
|---|---:|---:|---:|---:|
| `0|1|2|3` | 4 | 1 | 3 | `9/64` |
| `0|1|23` | 3 | 2 | 3 | `27/1024` |
| `0|12|3` | 3 | 1 | 3 | `9/64` |
| `0|13|2` | 3 | 1 | 3 | `9/64` |
| `01|2|3` | 3 | 1 | 3 | `9/64` |
| `02|1|3` | 3 | infinity | — | — |
| `03|1|2` | 3 | 2 | 3 | `27/1024` |
| `0|123` | 2 | infinity | — | — |
| `01|23` | 2 | 3 | 4 | `27/2048` |
| `012|3` | 2 | infinity | — | — |
| `013|2` | 2 | infinity | — | — |
| `02|13` | 2 | infinity | — | — |
| `023|1` | 2 | infinity | — | — |
| `03|12` | 2 | 3 | 4 | `27/4096` |
| `0123` | 1 | infinity | — | — |

Counts remain exactly:

- `L_arrow=1`: 4;
- `L_arrow=2`: 2;
- `L_arrow=3`: 2;
- `L_arrow=infinity`: 7.

No detection class above 3 is introduced.

## Result 3 — order 2 and order 3 are genuinely invisible at every lower temporal order

Representative order-2 observation `0|1|23` has:

- `L=1`: zero odd pairs, odd mass `0`;
- `L=2`: 3 odd pairs, odd mass `27/1024`.

The exact order-2 odd component marginalizes to the zero order-1 odd component.

Representative order-3 observation `01|23` has:

- `L=1`: zero odd pairs, odd mass `0`;
- `L=2`: zero odd pairs, odd mass `0`;
- `L=3`: 4 odd pairs, odd mass `27/2048`.

The exact order-3 odd component marginalizes to the zero order-2 odd component.

Thus the longer history is not merely increasing the magnitude of already-visible one-step evidence. In these cases it exposes a time-odd component that is exactly absent from every shorter path description.

## Result 4 — exact micro-to-macro cancellation in representative classes

For deterministic observation `g`, an observed word difference satisfies

`P_g(w)-P_g(Rw) = sum_{x:g(x)=w} [P_X(x)-P_X(Rx)]`.

Stage 5 evaluates that sum exactly for the shortest Stage 4 witness in three representative finite classes.

### Order 1 — `0|12|3`, witness `01`

- compatible micro paths: 2;
- nonzero micro contributions: 1;
- positive total: `3/64`;
- negative total: `0`;
- cancelled mass: `0`;
- macro residual: `3/64`.

Here the selected shortest macro witness contains a direct surviving micro reversal imbalance with no positive/negative cancellation.

### Order 2 — `0|1|23`, witness `021`

- compatible micro paths: 2;
- nonzero micro contributions: 2;
- positive total: `3/256`;
- negative total: `-3/1024`;
- cancelled mass: `3/1024`;
- macro residual: `9/1024`.

The observed triplet arrow is a partial residual after opposite-signed irreversible micro contributions are merged by the observation map.

### Order 3 — `01|23`, witness `0010`

- compatible micro paths: 16;
- nonzero micro contributions: 8;
- positive total: `93/16384`;
- negative total: `-147/16384`;
- cancelled mass: `93/16384`;
- macro residual: `-27/8192`.

The order-3 witness is therefore also an exact signed residual of substantial positive/negative microtrajectory cancellation.

These three representatives show increasingly deep cancellation structure, but Stage 5 does **not** promote that representative pattern into a universal law that higher `L_arrow` must always mean more cancellation.

## Result 5 — all-horizon hidden is qualitatively different from delayed detection

For representative `02|1|3`, Stage 4 already certified exact all-horizon observed reversibility.

Its illustrative Stage 5 profile has zero odd pairs and zero odd mass at `L=1,2,3`, but `L_arrow=infinity` is **not** inferred from this finite profile. It follows from the exact finite HMP/weighted-automaton equivalence certificate.

Thus Stage 5 separates:

- lower-order cancellation followed by a surviving higher-order odd component (`L_arrow=2` or `3`);
- complete observable reversal cancellation at every finite temporal order (`L_arrow=infinity`).

## Result 6 — temporal order is not arrow magnitude

The two binary order-3 observations have the same detection depth but different first-detection odd masses:

- `01|23`: `27/2048`;
- `03|12`: `27/4096`.

So `L_arrow` measures **where time asymmetry first appears in temporal order**, not how strong the asymmetry is once it appears.

This distinction is essential:

`temporal order != arrow strength`.

## What Stage 5 explains

The Stage 4 black-box map

`observation map -> L_arrow`

is refined into

`observation map -> signed cancellation of micro reversal differences -> first surviving reversal-odd temporal component -> L_arrow`.

For the frozen representatives, this gives an exact account of how coarse-graining can:

1. leave a direct one-step imbalance visible;
2. cancel all one-step evidence while retaining a triplet-level odd component;
3. cancel all one- and two-step evidence while retaining a four-symbol odd component;
4. cancel observable time-odd structure at every finite order.

## What Stage 5 does not explain

No universal graph motif, cycle type, or partition-only formula predicting arbitrary `L_arrow` was established.

The exact odd hierarchy and cancellation accounting are stronger explanations than a bare detection-depth table, but a compact arbitrary-order structural criterion remains open.

Stage 5 therefore stops here rather than enlarging the state space or searching for higher orders.

## Success contract

All five frozen conditions are satisfied:

1. exact reversal-odd hierarchy implemented and tied to `A_L=0`;
2. Stage 4 classes `1,2,3,infinity` reproduced on all 15 partitions;
3. first-detection order-2 and order-3 odd components marginalize exactly to zero lower-order components;
4. micro contribution sums reproduce the selected macro word differences exactly;
5. no universal motif/partition criterion is overclaimed.

## Interpretation guards

`temporal order != arrow strength`

`higher-order odd component != newly created physical arrow`

`microtrajectory cancellation != destruction of microscopic irreversibility`

`kernel of temporal marginalization != hidden ontological time`

`L_arrow=infinity under g != microscopic reversibility`

`representative motif != universal motif taxonomy`

`finite four-state hierarchy != arbitrary-order theorem`

`observable trajectory irreversibility != ontological becoming`

## Primary Stage 5 conclusion

> In the frozen four-state witness, the Stage 4 detection depth is exactly the lowest temporal order at which a reversal-odd observed path component survives coarse-graining. Delayed detection at orders 2 and 3 is not merely weaker one-step evidence: the odd component is exactly absent at every lower order and appears as a signed residual of irreversible microtrajectory contributions that partially cancel under observation. All-horizon hidden observations are different again: their complete observed word process is exactly reversal symmetric. The decomposition explains the frozen hierarchy but does not yet yield a universal partition-only predictor of `L_arrow`.
