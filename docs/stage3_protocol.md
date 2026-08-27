# Stage 3 Protocol — Structural Criteria for Arrow-Visible Observation Maps

## 0. Status and role

Stage 3 begins only after the first r-arrow research cycle (Stages 0–2) has completed successfully.

Its purpose is not to enlarge the Stage 2 census. It asks why some deterministic observation maps retain trajectory-level time-reversal asymmetry while others hide it.

Stage 3 is deliberately split into two bounded claims:

- **Stage 3A — one-step structural criterion**: derive an exact necessary-and-sufficient condition for `A_1(g)>0`.
- **Stage 3B — higher-order separation**: show, with the smallest practical finite construction used here, that one-step symmetry does not imply trajectory-level symmetry at all later horizons.

No Stage 4 direction is selected by this protocol.

## 1. Retained observable and coarse-graining semantics

All Stage 0 definitions remain in force.

For a stationary finite Markov chain `X_t` with transition matrix `P`, stationary distribution `pi`, and deterministic observation map `g:X->Y`, the observed path law is always computed by exact summation over compatible microtrajectories.

The trajectory arrow remains

`A_L(g;X) = D_KL(Pr_g(y_0,...,y_L) || Pr_g(y_L,...,y_0))`.

Stage 3 does not redefine the arrow metric and does not silently re-Markovize the observed process.

## 2. Stage 3A — exact one-step macro-flux criterion

For macrostates `a,b in Y`, define the stationary macro flux

`F_ab = sum_{i:g(i)=a} sum_{j:g(j)=b} pi_i P_ij`.

Because the chain is stationary,

`F_ab = Pr(Y_0=a, Y_1=b)`.

Therefore

`A_1(g;X) = sum_{a,b} F_ab log(F_ab/F_ba) = D_KL(F || F^T)`.

### Stage 3A proposition

For any finite stationary Markov chain and any deterministic state partition:

- `A_1(g;X)=0` **iff** `F_ab=F_ba` for every macrostate pair `(a,b)`;
- `A_1(g;X)>0` whenever the macro-flux matrix is not symmetric and the forward/reverse supports are mutually compatible;
- if some `F_ab>0` while `F_ba=0`, then `A_1=+infinity` under the Stage 0 convention.

Thus one-step arrow visibility is completely characterized by exact symmetry of the stationary macro-flux matrix.

This is a structural criterion, not a new definition of arrow.

## 3. Stage 3B — binary stationarity floor

A two-symbol stationary process cannot display trajectory-reversal asymmetry at horizons `L=1` or `L=2`.

### Binary proposition

For any stationary process `Y_t` taking values in `{0,1}` (Markov or non-Markov):

`A_1(Y)=A_2(Y)=0`.

Reason:

- length-2 paths (`L=1`) have only the non-palindromic pair `01 <-> 10`, and stationarity gives `Pr(01)=Pr(10)`;
- length-3 paths (`L=2`) are either palindromes or belong to the reversal pairs `001 <-> 100` and `011 <-> 110`;
- stationarity gives `Pr(001)=Pr(100)` from the two decompositions of `Pr(00)`, and similarly `Pr(011)=Pr(110)` from `Pr(11)`.

Therefore `L=3` is the first horizon at which a stationary binary observation can possibly reveal a hidden arrow.

This proposition is about the observation alphabet and stationarity; it is not a claim that every binary process has `A_3>0`.

## 4. Frozen Stage 3B witness

Use the four-state positive, doubly stochastic transition matrix

```
P = [
  [1/16, 1/4,  7/16, 1/4 ],
  [1/4,  7/16, 1/4,  1/16],
  [1/4,  1/4,  1/4,  1/4 ],
  [7/16, 1/16, 1/16, 7/16],
]
```

with uniform stationary distribution

`pi=(1/4,1/4,1/4,1/4)`.

Use the deterministic binary partition

`01|23`.

Frozen verification horizons are

`L in {1,2,3,4}`.

Expected qualitative pattern:

- micro process is irreversible;
- observed binary process has `A_1=0` and `A_2=0` exactly;
- observed binary process has `A_3>0`;
- `A_4>0` is recorded as an additional bounded check.

The scientific point of this witness is not the parameter choice itself. It demonstrates that the Stage 3A macro-flux criterion is complete for `L=1` but is not a complete criterion for finite-horizon trajectory irreversibility.

## 5. Stage 2 regression requirement

The Stage 3A macro-flux criterion must correctly reproduce every Stage 2 `L=1` classification:

- the four adjacent-pair three-state merges have asymmetric macro flux and `A_1>0`;
- the two opposite-pair three-state merges have symmetric macro flux and `A_1=0`;
- every two-state Stage 2 observation has symmetric one-step macro flux and `A_1=0`.

This is a regression check only; Stage 3 does not repeat the full Stage 2 census as a new result.

## 6. Stage 3 success contract

Stage 3 is complete when all of the following hold:

1. **Exact one-step criterion** — executable exact macro-flux computation agrees with `A_1=0 iff F=F^T` on declared tests.
2. **Stage 2 explanation** — the criterion reproduces the complete Stage 2 one-step visible/hidden split.
3. **Binary floor** — tests and proof record that stationary binary observations are reversal-symmetric through `L=2`.
4. **Higher-order witness** — the frozen positive four-state witness with partition `01|23` has exact path symmetry at `L=1,2` but exact path asymmetry at `L=3`.
5. **No silent generalization** — the final report distinguishes the general Stage 3A/binary propositions from the benchmark-specific Stage 3B witness.

A valid Stage 3 result may conclude that no simple graph-only criterion beyond `L=1` is yet established.

## 7. Stop / anti-regress rules

Before the Stage 3 report is complete:

1. do not increase the witness state count beyond 4;
2. do not inspect `L>4` merely to amplify the higher-order effect;
3. do not add continuous time, stochastic observation channels, empirical data, or quantum models;
4. do not redefine `A_L`;
5. do not claim a complete arbitrary-horizon structural theorem from the Stage 3B witness;
6. do not begin local-arrow alignment or system-to-system arrow transport;
7. do not select Stage 4 before Stage 3 is reviewed.

## 8. Interpretation guards

`one-step macro-flux symmetry != all-horizon reversibility`

`A_1=0 != no hidden arrow`

`binary A_1=A_2=0 != binary processes are reversible at all horizons`

`higher-order arrow != ontological becoming`

`non-Markov observed dynamics != fundamental memory ontology`

`finite witness != universal higher-order classification theorem`

`structural criterion != privileged physical observer without further justification`

## 9. Evidence hierarchy

1. exact identities / short proofs;
2. exact rational flux and path probabilities;
3. executable tests;
4. machine-readable result artifact;
5. interpretive report.
