# Stage 3 Proof Notes — Structural Arrow Criteria

## 1. One-step macro-flux criterion

Let `X_t` be a finite stationary Markov chain with stationary distribution `pi`, transition matrix `P`, and deterministic observation map `g:X->Y`.

For observed macrostates `a,b`, define

`F_ab = sum_{i:g(i)=a} sum_{j:g(j)=b} pi_i P_ij`.

By direct marginalization,

`Pr(Y_0=a,Y_1=b)=F_ab`.

The reversed one-step observed path `(b,a)` has probability `F_ba`. Therefore

`A_1(g;X) = sum_{a,b} F_ab log(F_ab/F_ba)`

which is exactly

`D_KL(F || F^T)`

when the matrix entries are viewed as a normalized distribution over ordered macrostate pairs.

KL non-negativity gives `A_1>=0`, with equality iff the two distributions are identical. Hence

`A_1(g;X)=0  <=>  F_ab=F_ba for every a,b`.

If the flux matrix is asymmetric and forward/reverse supports match, `A_1>0`. If some `F_ab>0` while `F_ba=0`, the Stage 0 convention gives `A_1=+infinity`.

Thus exact symmetry of the stationary macro-flux matrix is a necessary-and-sufficient structural criterion for one-step arrow invisibility.

## 2. Why this explains the Stage 2 adjacent/opposite split

For the frozen Stage 2 four-cycle, the adjacent merge `01|2|3` has exact macro-current differences

- `F_AB-F_BA=1/16`,
- `F_BC-F_CB=1/16`,
- `F_CA-F_AC=1/16`.

Its macro-flux matrix is therefore asymmetric and `A_1>0`.

For the opposite merge `02|1|3`, exact observed fluxes balance:

- `F_AB=F_BA=3/16`,
- `F_AC=F_CA=3/16`,
- `F_BC=F_CB=0`.

Its macro-flux matrix is symmetric and `A_1=0`.

The Stage 2 result is therefore not merely a numerical contrast at `L=1`: it is an instance of the general macro-flux criterion.

## 3. Stationary binary processes are reversal-symmetric through L=2

Let `Y_t` be any stationary process on the binary alphabet `{0,1}`. Markovity is not assumed.

### Horizon L=1

The only non-palindromic reversal pair is

`01 <-> 10`.

Stationarity implies equal one-time marginals at consecutive positions. Using

`Pr(Y_0=0)=Pr(00)+Pr(01)`

and

`Pr(Y_1=0)=Pr(00)+Pr(10)`,

stationarity gives

`Pr(01)=Pr(10)`.

The paths `00` and `11` are palindromes. Therefore every length-2 path has the same probability as its reverse, so `A_1=0`.

### Horizon L=2

Length-3 binary paths are either palindromes

`000, 010, 101, 111`

or belong to one of two nontrivial reversal pairs:

`001 <-> 100`

and

`011 <-> 110`.

For the first pair, stationarity of the length-2 word `00` gives

`Pr(Y_0Y_1=00) = Pr(000)+Pr(001)`

and

`Pr(Y_1Y_2=00) = Pr(000)+Pr(100)`.

These two marginals are equal by stationarity, hence

`Pr(001)=Pr(100)`.

Likewise stationarity of the length-2 word `11` gives

`Pr(011)=Pr(110)`.

Thus every length-3 binary path has the same probability as its reverse and `A_2=0`.

Therefore a stationary binary process can first become trajectory-irreversible only at horizon `L=3` or later.

## 4. Stage 3B witness shows L=3 is attainable

The frozen Stage 3B four-state Markov chain is strictly positive and doubly stochastic. Under the binary partition `01|23`, its observed macro-flux matrix is

```
[[1/4, 1/4],
 [1/4, 1/4]]
```

so Stage 3A predicts `A_1=0`.

The binary proposition also forces `A_2=0`.

At `L=3`, however, the observed length-4 paths

`0010`

and its reverse

`0100`

have exact probabilities

`Pr(0010)=55/1024 = 440/8192`

and

`Pr(0100)=467/8192`.

They differ by

`-27/8192`.

Hence the observed path distribution is not reversal-symmetric at `L=3`, and therefore `A_3>0`.

This gives a constructive separation:

`macro-flux symmetry (A_1=0) != all-horizon trajectory reversibility`.

## 5. What is and is not proved

Proved here:

1. an exact arbitrary-finite-state criterion for `A_1=0` under deterministic state observation;
2. an arbitrary-stationary-binary-process result that `A_1=A_2=0`;
3. a four-state positive witness showing binary higher-order irreversibility can occur at `L=3`.

Not proved here:

- a complete structural criterion for arbitrary `L`;
- a graph-topology-only criterion for higher-order arrow visibility;
- a universal minimum hidden-state count for every class of observation map;
- any ontological claim about becoming or fundamental time.
