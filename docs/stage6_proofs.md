# Stage 6 Proof Notes — Exact Arrow Memory

## 1. Recursive forward/reverse filter

For a deterministic observation map `g`, let `D_y` be the diagonal selector for observed symbol `y`.

For an observed word

`w = y_0 ... y_k`, 

define unnormalized forward and reverse rows

`r_+(w) = pi D_y0 P ... D_yk P`,

`r_-(w) = pi D_y0 P^R ... D_yk P^R`.

Because `P 1 = 1` and `P^R 1 = 1`,

`r_+(w) 1 = P_+(w)`,

`r_-(w) 1 = P_-(w)`.

After a new symbol `a`,

`r_+(wa) = r_+(w) D_a P`,

`r_-(wa) = r_-(w) D_a P^R`.

Therefore `(r_+, r_-)` is an exact recursive state: the raw observed prefix need not be retained once these rows are known.

Stage 6 tests these row sums against the independent exact `observed_word_probability` implementation.

## 2. Why the current likelihood ratio alone need not be recursive state

Let

`Lambda(w) = P_+(w)/P_-(w)`.

A scalar `Lambda(w)` would be recursively sufficient only if equal current ratios implied equal next-step ratio updates for every common symbol.

The frozen family gives exact counterexamples.

### Order 1 representative `0|12|3`

Prefixes `1` and `0` both satisfy

`Lambda = 1`.

Appending symbol `0` gives

`Lambda(10) = 8/11`,

`Lambda(00) = 1`.

So the scalar current ratio does not determine its own update.

### Order 2 representative `0|1|23`

Prefixes `02` and `0` both satisfy `Lambda=1`, but appending `1` gives

`Lambda(021) = 32/23`,

`Lambda(01) = 1`.

### Order 3 representative `01|23`

Prefixes `001` and `0` both satisfy `Lambda=1`, but appending `0` gives

`Lambda(0010) = 440/467`,

`Lambda(00) = 1`.

These are constructive proofs of insufficiency for the selected representatives. The complete Stage 6 census finds such a bounded exact counterexample for every one of the eight finite-arrow partitions.

The mechanism is hidden context: equal scalar evidence can accompany different forward/reverse hidden-state predictive rows, so the same next observed symbol changes the two hypotheses differently.

## 3. Exact linear realization rank

A finite observed hidden Markov process has symbol operators

`M_y = D_y P`.

A scalar word series has linear form

`p(w) = alpha M_w omega`.

For the forward/reverse pair, Stage 6 uses block-diagonal symbol operators

`M_y^(+/-) = diag(D_y P, D_y P^R)`

with a joint initial row and two output columns selecting the forward and reverse blocks.

The reachable row space is the span of

`alpha M_u`

over all prefixes `u`.

The observable column space is the span of

`M_v omega`

over all suffixes `v` and output channels.

The rank of the exact pairing between these finite-dimensional spaces is the Hankel/weighted-linear minimal realization rank for the represented word series.

Stage 6 computes this with exact rational Gaussian elimination; it does not truncate a horizon.

## 4. Joint likelihood rank versus reversal-contrast rank

The joint vector series is

`w -> (P_+(w), P_-(w))`.

Its minimal rank measures exact linear representation dimension for both hypothesis likelihoods.

Separately define the signed contrast series

`d(w) = P_+(w) - P_-(w)`.

Its minimal rank is computed from initial row `[pi,-pi]` and one all-ones output functional.

If the observed forward and reverse processes are exactly equal for every finite word, then `d(w)=0` identically and its Hankel rank is exactly zero.

Conversely, if any word differs, the contrast series is nonzero and its rank is positive.

Thus

`contrast rank = 0 <=> exact all-horizon observed reversibility`.

This does **not** imply that the observed process itself has zero predictive/representational complexity.

## 5. Why temporal depth and linear rank are different quantities

In the frozen four-state witness:

- `0|12|3` has `L_arrow=1` and joint rank `6`;
- `0|1|23` has `L_arrow=2` and joint rank `6`;
- `01|23` has `L_arrow=3` and joint rank `6`.

Therefore the same exact linear representation dimension occurs at three distinct first-detection depths.

Also among `L_arrow=1` observations, `0|13|2` has joint rank `4` while the other three order-1 observations have joint rank `6`.

Hence neither direction of a one-to-one identification is available in this frozen family:

`L_arrow != joint linear rank`.

The former asks **how far back the first time-odd relation lies**; the latter asks **how many independent exact linear coordinates are needed to generate/update the two hypothesis likelihood series**.

## 6. All-horizon hidden observations

The seven `L_arrow=infinity` observations all have reversal-contrast rank `0`, as required by Stage 4 exact equivalence.

However their joint ranks are `1` or `2` rather than zero.

So an observed process can require a nontrivial exact representation while requiring no directional contrast representation at all:

`process representation complexity != arrow-specific contrast complexity`.

The reversible four-cycle control has contrast rank `0` under all 15 partitions as well.

## 7. What is and is not minimal here

Stage 6 establishes exact **linear realization** minima.

It does not prove that the joint linear rank is the minimum number of physical memory states, Shannon bits, or the minimum dimension under arbitrary nonlinear recursive encodings.

Likewise, the contrast rank alone does not generally preserve the likelihood ratio, because a signed difference does not determine numerator and denominator separately.

Therefore the safe conclusions are:

- exact recursive filtering is finite-dimensional;
- the scalar current ratio is insufficient in every finite-arrow partition of the frozen witness;
- exact joint and contrast linear minima can be computed finitely;
- temporal detection depth, process representation rank, and directional contrast rank are distinct quantities.

## 8. Causal-state boundary

Stage 6 does not infer finite computational-mechanics causal states from finite hidden-state generation.

No open-ended mixed-state closure search or approximate reconstruction is used. A future causal-state stage would require its own bounded success contract and literature comparison.
