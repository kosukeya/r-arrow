# Stage 3 — Structural Criteria for Arrow Visibility

## Status

Stage 3 converts the Stage 2 observation census into a bounded structural explanation.

It establishes one exact general criterion at `L=1`, one exact general fact for stationary binary observations through `L=2`, and one four-state constructive witness showing that higher-order irreversibility can remain hidden until `L=3`.

This is not a complete arbitrary-horizon theory of arrow-preserving observation maps.

## Result 1 — exact one-step criterion

For deterministic observation `g:X->Y`, define the stationary macro flux

`F_ab = sum_{i:g(i)=a} sum_{j:g(j)=b} pi_i P_ij`.

Then

`F_ab = Pr(Y_0=a,Y_1=b)`

and therefore

`A_1(g;X)=D_KL(F || F^T)`.

Hence

> `A_1(g;X)=0` if and only if the exact stationary macro-flux matrix is symmetric.

Equivalently, any unequal macro pair `F_ab != F_ba` is a one-step arrow witness (with `+infinity` possible under a one-way support mismatch).

This gives a complete structural criterion for one-step arrow visibility.

## Result 2 — Stage 2 is explained at L=1 by macro flux

The criterion reproduces every Stage 2 one-step classification.

For representative adjacent merge `01|2|3`:

- `F_AB-F_BA = 1/16`;
- `F_BC-F_CB = 1/16`;
- `F_CA-F_AC = 1/16`.

The macro-flux matrix is asymmetric, so `A_1>0`.

For representative opposite merge `02|1|3`:

- `F_AB=F_BA=3/16`;
- `F_AC=F_CA=3/16`;
- `F_BC=F_CB=0`.

The macro-flux matrix is symmetric, so `A_1=0`.

Across all 14 Stage 2 primary observations, the exact macro-flux criterion and the path-KL `A_1` classification have zero mismatches.

Thus the Stage 2 adjacent-vs-opposite contrast at one step is an instance of a general stationary macro-flux identity rather than a benchmark-specific numerical accident.

## Result 3 — stationary binary observations cannot reveal an arrow before L=3

For any stationary process over two symbols `{0,1}`, regardless of whether it is Markov:

`A_1=A_2=0`.

At `L=1`, stationarity forces `Pr(01)=Pr(10)`.

At `L=2`, all length-three words are palindromic except the reversal pairs

- `001 <-> 100`;
- `011 <-> 110`.

Stationarity of the two-letter marginals `00` and `11` forces equality within each pair.

Therefore `L=3` is the first horizon at which a stationary binary observation can possibly display trajectory-reversal asymmetry.

This does **not** say that every binary process has an arrow at `L=3`; it only establishes the earliest possible horizon.

## Result 4 — the L=3 possibility is attained by a positive four-state witness

The frozen Stage 3B transition matrix is

```
P = [
  [1/16, 1/4,  7/16, 1/4 ],
  [1/4,  7/16, 1/4,  1/16],
  [1/4,  1/4,  1/4,  1/4 ],
  [7/16, 1/16, 1/16, 7/16],
]
```

It is strictly positive and doubly stochastic, with stationary distribution

`pi=(1/4,1/4,1/4,1/4)`.

Use binary partition

`01|23`.

The observed one-step macro-flux matrix is exactly

```
[[1/4, 1/4],
 [1/4, 1/4]]
```

and is symmetric.

Observed arrow strengths are:

| L | A_L(01|23) |
|---:|---:|
| 1 | 0 |
| 2 | 0 |
| 3 | 0.000709980636 |
| 4 | 0.001485176667 |

The underlying micro-process is already irreversible at one step; its corresponding values are approximately:

| L | A_L(micro) |
|---:|---:|
| 1 | 0.117446528296 |
| 2 | 0.234893056593 |
| 3 | 0.352339584889 |
| 4 | 0.469786113186 |

Thus the binary observation hides all one- and two-step arrow evidence while retaining a small higher-order arrow.

An exact `L=3` path witness is

- `Pr(0010)=55/1024 = 440/8192`;
- `Pr(0100)=467/8192`.

Since `0100` is the reverse of `0010` and the probabilities differ by `27/8192`, the observed path law is exactly time-asymmetric at `L=3`.

## Result 5 — what the criterion can and cannot do

Stage 3A is complete at one step:

`macro-flux symmetry <=> A_1=0`.

But Stage 3B gives the constructive separation

`macro-flux symmetry != all-horizon trajectory reversibility`.

Therefore a criterion based only on one-step macro currents cannot classify all higher-order arrows.

Higher-order classification must retain more path structure than the one-step quotient flux matrix alone.

Stage 3 does not yet establish whether a compact graph/cycle/memory criterion exists for arbitrary finite `L`.

## Stage 3 success contract

All five frozen Stage 3 conditions are realized by the synchronized Stage 3 tree:

1. exact one-step macro-flux criterion implemented and tested;
2. complete Stage 2 one-step split reproduced with zero criterion/KL mismatches;
3. stationary-binary `A_1=A_2=0` proof recorded;
4. positive four-state binary witness has exact symmetry through `L=2` and asymmetry at `L=3`;
5. general propositions and benchmark-specific witness are kept explicitly separate.

## Interpretation guards

`one-step macro-flux symmetry != all-horizon reversibility`

`A_1=0 != no hidden arrow`

`binary A_1=A_2=0 != binary all-horizon reversibility`

`higher-order arrow != ontological becoming`

`finite witness != universal higher-order classification theorem`

`structural criterion != privileged physical observer without further justification`

## Primary Stage 3 conclusion

> One-step arrow visibility under deterministic coarse-graining is completely characterized by asymmetry of the stationary macro-flux matrix, but that criterion is not sufficient for higher-order trajectory irreversibility: stationary binary observations are necessarily symmetric through `L=2`, while a strictly positive four-state hidden process can first reveal an arrow at `L=3`.
