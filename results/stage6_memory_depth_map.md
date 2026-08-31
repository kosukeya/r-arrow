# Stage 6 — Minimal Memory for Observable Arrow Detection

## Status

Stage 6 is complete for the frozen four-state family.

It separates **how far back an observer must look** from **how many exact linear coordinates are needed to update forward/reverse likelihoods**.

No new benchmark family, larger hidden state space, or higher detection-order search was introduced.

## Primary result 1 — raw history depth and exact linear representation dimension are different axes

For the frozen `higher_order_hidden_arrow_four_state` witness, the same exact joint forward/reverse linear rank occurs at three different detection depths:

| partition | `L_arrow` | forward rank | reverse rank | joint rank | contrast rank |
|---|---:|---:|---:|---:|---:|
| `0|12|3` | 1 | 3 | 3 | 6 | 6 |
| `0|1|23` | 2 | 3 | 3 | 6 | 6 |
| `01|23` | 3 | 3 | 3 | 6 | 6 |

Thus

`temporal detection depth != exact joint linear representation dimension`.

Stage 5's `L_arrow` says where a time-reversal-odd relation first appears in raw temporal order. Stage 6's joint rank says how many independent exact linear coordinates are needed to generate both forward and reverse observed word-likelihood series.

They answer different questions.

## Primary result 2 — even the current likelihood ratio is not enough memory

For every one of the eight finite-arrow partitions, Stage 6 finds an exact bounded counterexample within prefix length `<=3`:

- two distinct observed prefixes have the same current forward/reverse likelihood ratio;
- after the same next observed symbol, their updated ratios differ.

Therefore the scalar current ratio is not recursively sufficient state for any finite-arrow observation in the frozen witness family.

Representative examples:

### Order 1 — `0|12|3`

`Lambda(1)=Lambda(0)=1`, but after symbol `0`:

`Lambda(10)=8/11`,

`Lambda(00)=1`.

### Order 2 — `0|1|23`

`Lambda(02)=Lambda(0)=1`, but after symbol `1`:

`Lambda(021)=32/23`,

`Lambda(01)=1`.

### Order 3 — `01|23`

`Lambda(001)=Lambda(0)=1`, but after symbol `0`:

`Lambda(0010)=440/467`,

`Lambda(00)=1`.

So the observer must retain hidden contextual information beyond the current scalar arrow evidence.

## Primary result 3 — exact recursive filtering does compress raw history

Stage 6 implements an exact forward/reverse filter state consisting of two unnormalized hidden-state predictive rows.

Once these rows are known, the entire raw observed prefix can be discarded. The rows update recursively with each new symbol, and their sums reproduce exact direct forward/reverse word probabilities.

Thus a long observed history can be compressed into a fixed finite-dimensional internal state for this finite hidden-state family.

This is an exact representation statement, not a claim about physical memory bits.

## Primary result 4 — complete 15-partition Memory–Depth Map

| partition | `L_arrow` | forward rank | reverse rank | joint rank | contrast rank | ratio-only counterexample |
|---|---:|---:|---:|---:|---:|---|
| `0|1|2|3` | 1 | 3 | 3 | 6 | 6 | yes |
| `0|1|23` | 2 | 3 | 3 | 6 | 6 | yes |
| `0|12|3` | 1 | 3 | 3 | 6 | 6 | yes |
| `0|13|2` | 1 | 2 | 2 | 4 | 4 | yes |
| `01|2|3` | 1 | 3 | 3 | 6 | 6 | yes |
| `02|1|3` | infinity | 2 | 2 | 2 | 0 | no finite-arrow task |
| `03|1|2` | 2 | 3 | 3 | 6 | 6 | yes |
| `0|123` | infinity | 2 | 2 | 2 | 0 | no finite-arrow task |
| `01|23` | 3 | 3 | 3 | 6 | 6 | yes |
| `012|3` | infinity | 2 | 2 | 2 | 0 | no finite-arrow task |
| `013|2` | infinity | 1 | 1 | 1 | 0 | no finite-arrow task |
| `02|13` | infinity | 1 | 1 | 1 | 0 | no finite-arrow task |
| `023|1` | infinity | 2 | 2 | 2 | 0 | no finite-arrow task |
| `03|12` | 3 | 3 | 3 | 6 | 6 | yes |
| `0123` | infinity | 1 | 1 | 1 | 0 | no finite-arrow task |

Joint-rank values by detection class are:

- `L_arrow=1`: `{4,6}`;
- `L_arrow=2`: `{6}`;
- `L_arrow=3`: `{6}`;
- `L_arrow=infinity`: `{1,2}`.

Contrast-rank values are:

- `L_arrow=1`: `{4,6}`;
- `L_arrow=2`: `{6}`;
- `L_arrow=3`: `{6}`;
- `L_arrow=infinity`: `{0}`.

## Primary result 5 — process complexity and directional complexity separate cleanly

Every all-horizon-hidden observation has exact reversal-contrast rank `0`.

However its joint process rank is not generally zero: the seven hidden observations have joint rank `1` or `2`.

Therefore an observed stochastic process can still require a nontrivial exact representation even though its forward and reverse word processes are identical.

In this exact linear sense:

`process representation complexity != directional contrast complexity`.

The reversible four-cycle control has contrast rank `0` under all 15 partitions, as required.

## Primary result 6 — order 1 itself does not fix memory rank

Even within one detection order, linear complexity differs.

Among the four `L_arrow=1` observations:

- `0|13|2` has joint/contrast rank `4`;
- the other three have joint/contrast rank `6`.

So Stage 6 rules out both simplistic identifications:

- higher temporal order does not automatically mean larger exact linear rank;
- fixed temporal order does not determine exact linear rank either.

## Interpretation

Stage 3–5 showed that coarse-graining can push observable time-direction evidence out of one-step statistics and into longer temporal relations.

Stage 6 adds a second layer:

> the raw history required to *reveal* an arrow need not be the state that must be *stored* internally to update arrow evidence.

A fixed-dimensional forward/reverse filter can summarize the entire observed prefix. But that state generally must contain more information than the current likelihood ratio alone, because two histories with identical current evidence can carry different hidden contexts and react differently to the next observation.

The resulting conceptual chain is:

`coarse observation -> hidden-state ambiguity -> history dependence -> recursive internal state`.

This is a finite stochastic-process statement. It is not a claim that coarse-graining creates fundamental memory, subjective time, or ontological becoming.

## What Stage 6 does not establish

Stage 6 does **not** identify a unique information-theoretic `M_arrow` in bits.

The joint rank is minimal only within exact weighted-linear realizations of the paired forward/reverse word-likelihood series. Arbitrary nonlinear recursive encodings could require a different notion of minimality.

The contrast rank is arrow-specific in the sense that it vanishes exactly when the forward and reverse observed word series coincide, but contrast alone does not in general preserve the likelihood ratio.

Computational-mechanics causal-state complexity is not computed here. Finite hidden-state generation does not guarantee finite exact causal-state closure, and Stage 6 deliberately avoids open-ended or approximate mixed-state searches.

## Success contract

All six frozen conditions are satisfied:

1. exact recursive forward/reverse filtering implemented and validated against direct word probabilities;
2. exact ratio-only insufficiency counterexamples obtained for representative order 1/2/3 observations and, in the complete census, all eight finite-arrow partitions;
3. exact forward, reverse, joint, and reversal-contrast linear ranks computed for all 15 partitions;
4. `L_arrow` and joint linear rank shown to be distinct axes;
5. all all-horizon-hidden observations and all reversible-control observations have zero contrast rank;
6. a finite machine-readable Memory–Depth Map is frozen without expanding the model family.

## Core guards

`history depth != internal memory complexity`

`linear realization rank != physical memory bits`

`joint likelihood rank != uniquely defined nonlinear minimal discriminator memory`

`contrast rank != predictive complexity`

`likelihood ratio at one instant != sufficient recursive state in the frozen finite-arrow family`

`zero contrast rank != microscopic reversibility`

`coarse-graining-induced inference memory != fundamental memory ontology`

`observable arrow memory != ontological becoming`

## Primary Stage 6 conclusion

> In the frozen four-state family, observable-arrow detection depth and exact linear representation complexity are distinct. A fixed finite-dimensional forward/reverse filter can compress arbitrarily long raw observed prefixes, but the current scalar likelihood ratio is not recursively sufficient for any of the eight finite-arrow observations: equal current evidence can hide different internal contexts that update differently on the same next symbol. The same joint rank `6` occurs at `L_arrow=1,2,3`, while all-horizon-hidden observations retain nontrivial process rank `1` or `2` but have exactly zero reversal-contrast rank. Stage 6 therefore separates temporal depth, recursive representation complexity, and directional contrast complexity without claiming a unique memory cost in bits.
