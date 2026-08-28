# Stage 4 Proof Notes

These notes separate the general finite-process propositions used by Stage 4 from the benchmark-specific census.

## 1. History-depth monotonicity

Let `P_{L+1}` denote the stationary observed path law on `L+2` symbols and `P_{L+1}^R` its reversed law.  Project a path to its first `L+1` symbols.

Stationarity makes the projected forward law equal to `P_L`.  Projecting the reversed law gives `P_L^R`: summing the final coordinate of the reversed representation is equivalent to summing the leading coordinate of the stationary forward path.

KL data processing therefore gives

`D_KL(P_{L+1} || P_{L+1}^R) >= D_KL(P_L || P_L^R)`

and hence

`A_{L+1} >= A_L`.

Consequences:

- once `A_L>0`, every later horizon also has positive arrow evidence;
- a finite first-detection horizon is well-defined;
- this proposition says nothing about how quickly `A_L` grows.

## 2. Observation-refinement monotonicity

Suppose a coarse observation factors through a fine one:

`g_coarse = h o g_fine`.

Applying `h` coordinatewise to a fine observed trajectory deterministically maps its forward path law to the coarse forward path law, and likewise maps its reversed law to the coarse reversed law.

KL data processing gives, at every `L`,

`A_L(g_coarse) <= A_L(g_fine)`.

If the coarse observation first detects at finite `L`, the fine observation must already have positive arrow evidence at that same horizon or earlier.  Therefore

`L_arrow(g_fine) <= L_arrow(g_coarse)`,

with `infinity` ordered after all finite values.

## 3. Stationary micro time reversal

For a finite stationary Markov chain with positive stationary distribution `pi`, define

`P_rev[i,j] = pi[j] P[j,i] / pi[i]`.

Then

`pi[i] P_rev[i,j] = pi[j] P[j,i]`.

For any micro path `(x_0,...,x_L)`, its probability under the reversed chain is

`pi[x_0] product_t P_rev[x_t,x_{t+1}]`.

Substituting the definition telescopes the stationary factors and yields

`pi[x_L] product_t P[x_{t+1},x_t]`,

which is exactly the forward probability of the reversed micro path.

After any deterministic state observation, summing compatible micro paths preserves this equality.  Therefore the observed process is all-horizon time-reversal symmetric exactly when the observed word process generated from `P` is equivalent to the observed word process generated from `P_rev`.

## 4. Finite linear representation of observed words

For observed symbol `y`, let `D_y` be the diagonal matrix that keeps hidden states mapped to `y` and zeros the others.

For a nonempty observed word `w=(y_0,...,y_k)`,

`Pr(w) = pi D_y0 P D_y1 P ... D_yk P 1`.

The final `P` is harmless because `P 1 = 1`.

Thus the process is represented by an initial row `pi`, symbol matrices `D_y P`, and final column `1`.

## 5. Direct-sum equivalence certificate

Build a direct-sum representation of the forward and reversed observed processes:

- initial difference row: `[pi, -pi]`;
- each symbol acts block-diagonally with `D_y P` and `D_y P_rev`;
- final column is all ones in both blocks.

For any word `w`, the resulting scalar is exactly

`Pr_forward(w) - Pr_reverse(w)`.

All reachable difference rows lie in a vector space of dimension at most `2n`.  Starting from the initial row, repeatedly multiply by every symbol matrix and keep only linearly independent rows.  Exact rational Gaussian elimination decides independence.

The process terminates after at most `2n` independent reachable rows have been added.

If the final functional is zero on every row of the closed reachable space, it is zero on every linear combination and hence on every reachable word row.  The two observed processes then assign the same probability to every finite word.

If a generated row has a nonzero final value, its generating word is a finite counterexample.  Breadth-first expansion yields a shortest mismatch horizon.  A dependent zero-output row need not be expanded: all its successors are linear combinations of successors of the stored spanning rows, and a nonzero output of such a combination would require a nonzero output in the generated spanning closure.

## 6. Meaning of the certificate

For an observation `g`:

- a counterexample word gives finite `L_arrow`;
- closure with no counterexample certifies `L_arrow = infinity` for that exact finite stationary model and deterministic observation.

This does **not** imply the micro chain is reversible.  It says only that the selected observed word process is statistically indistinguishable from its time reverse at every finite horizon.
