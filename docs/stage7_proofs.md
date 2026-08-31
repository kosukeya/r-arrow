# Stage 7 proof notes — Structural certificates for all-horizon hiding

## 1. Observation-preserving reversal conjugacy is sufficient

Let `P` be a finite irreducible stationary Markov chain with stationary law `pi`, and let `P^R` denote the stationary time-reversed transition matrix.

Let `g:X->Y` be a deterministic observation map. Suppose a permutation `sigma:X->X` satisfies:

1. `g(sigma(x)) = g(x)` for every microstate `x`;
2. `pi(sigma(x)) = pi(x)` for every microstate `x`;
3. `P^R[i,j] = P[sigma(i),sigma(j)]` for every pair `i,j`.

For an observed word `w=(y_0,...,y_L)`, its forward probability is

`sum_{x_0:L : g(x_t)=y_t} pi[x_0] prod_t P[x_t,x_{t+1}]`.

Apply `sigma` pointwise to every compatible microtrajectory. Because `sigma` is a bijection and preserves `g`, this maps the compatible-path set to itself. By stationary preservation and reversal conjugacy, the weight of each transformed path under the reverse model equals the original forward weight. Therefore the complete sums agree:

`Pr_forward(w) = Pr_reverse(w)`

for every finite observed word `w`.

Hence the observed process is all-horizon time-reversal symmetric and `L_arrow=infinity`.

This is a sufficient certificate only. The converse is not assumed.

## 2. Why failure of the permutation test is inconclusive

An observed hidden process can have redundant or unobservable hidden coordinates. Two distinct hidden generators can therefore define the same scalar observed word series without being related by a literal permutation of hidden states.

Thus

`no observation-preserving reversal permutation`

must not be read as

`observable forward and reverse processes differ`.

Stage 4 remains the authoritative equality decision. Stage 7 only asks what structural certificate realizes that already-certified equality.

## 3. Minimal weighted-linear realization

For a deterministic observation map, define one symbol operator `M_y=D_y P` for each observed symbol `y`.

The scalar word probability is

`f(w)=alpha M_w beta`,

where `alpha=pi`, `beta=1`, and `M_w` is the ordered product of symbol operators.

The exact minimal linear dimension of this scalar series is the rank of its finite Hankel pairing between the reachable row span and observable column span.

Stage 7 constructs a reduced realization by selecting an exact full-rank Hankel minor. If `R` is the selected reachable-row matrix and `O` the selected observable-column matrix, then

`H = R O`

is invertible. Reduced coordinates are evaluations against `O`, and the reduced symbol operator is

`A_y = H^{-1} R M_y O`.

The reduced initial row and output column are obtained by the same exact coordinate map. No floating-point tolerance is used.

## 4. Minimal equivalent realizations admit an intertwiner

Let the reduced forward and reverse realizations have the same minimal rank `r` and generate the same scalar word series.

Choose `r` prefix words whose forward reduced states form an invertible row matrix `F`. Because the two minimal realizations generate the same Hankel series, the corresponding reverse reduced states form an invertible matrix `R`.

Define

`T = F^{-1} R`.

Then direct exact verification checks:

- `alpha_+ T = alpha_-`;
- `A_y^+ T = T A_y^-` for every symbol;
- `T beta_- = beta_+`.

Therefore every word evaluation is preserved:

`alpha_+ A_w^+ beta_+ = alpha_- A_w^- beta_-`.

Stage 7 uses the verified equations themselves as the certificate; it does not infer equality merely from matching ranks.

## 5. Permutation and linear certificates are different claims

A permutation certificate says the **micro hidden states themselves** can be relabeled, invisibly to the observer, so as to turn forward dynamics into reverse dynamics.

A linear certificate says only that after removing unreachable/unobservable redundancy, the **observable word-process representations** are similar.

Therefore

`linear_only`

does not imply an unobserved literal state permutation exists.

## 6. Stage 6 contrast rank connection

If a Stage 7 certificate establishes

`P_forward(w)=P_reverse(w)` for every word,

then the signed scalar series

`P_forward-P_reverse`

is identically zero. Its exact minimal linear rank is therefore zero, matching the Stage 6 reversal-contrast result.

The converse from zero contrast rank to a simple micro permutation is not asserted.

## 7. Representative explanation rule

If the certificate is permutation-based, a literal microtrajectory partner may be shown.

If the certificate is linear-only, Stage 7 instead compares forward and reverse hidden predictive rows after the same observed prefix. These hidden rows may differ even though their probabilities agree. The rows are then mapped to their exact minimal observable coordinates and compared through `T`.

This is deliberately weaker than claiming a one-to-one microtrajectory pairing.

## Guards

- sufficient permutation criterion != necessary condition;
- minimal linear similarity != microscopic symmetry;
- same observed word series != same hidden generator;
- all-horizon hiding != microscopic reversibility;
- exact representation certificate != thermodynamic explanation;
- observed time-reversal symmetry != ontological blockness.
