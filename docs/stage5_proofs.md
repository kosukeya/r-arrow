# Stage 5 Proof Notes

These notes separate exact finite-process identities used by Stage 5 from benchmark-specific observations.

## 1. Reversal-odd path component

At horizon `L`, let `P_L(w)` be the exact stationary observed probability of word `w=(y_0,...,y_L)`. Let `R` reverse a word.

Define

`O_L(w) = [P_L(w)-P_L(Rw)]/2`.

Then `O_L(Rw)=-O_L(w)`. Moreover,

`O_L=0`

iff

`P_L(w)=P_L(Rw)` for every word `w`,

iff the horizon-`L` forward and reversed path laws are identical,

iff

`A_L = D_KL(P_L || R P_L) = 0`.

Thus the Stage 4 quantity can be written exactly as

`L_arrow = min {L>=1 : O_L != 0}`,

with `infinity` reserved for exact all-horizon equivalence.

## 2. Odd mass

Choose one representative from each unordered non-palindromic reversal pair `{w,Rw}` and define

`Delta_L(w)=P_L(w)-P_L(Rw)`.

Then

`M_L = sum_pairs |Delta_L(w)|`

is exactly the total-variation distance between `P_L` and `R P_L`, because the full `L1` difference counts each reversal pair twice and total variation contributes the factor `1/2`.

`M_L` is an exact magnitude diagnostic. It is not the KL arrow strength `A_L`, and it does not define temporal order.

## 3. Temporal marginalization of the odd component

Let `m` drop the final symbol from a word of length `L+1`.

Stationarity gives

`m_* P_L = P_{L-1}`.

For the reversed law, summing the final coordinate of `R P_L` is equivalent to summing the initial coordinate of `P_L`, which by stationarity yields `R P_{L-1}`. Therefore

`m_* (R P_L) = R P_{L-1}`.

By linearity,

`m_* O_L = O_{L-1}`.

Consequently, if `L_arrow=k>1`, then

`O_k != 0`

but

`m_* O_k = O_{k-1}=0`.

The first detectable time-odd component is therefore invisible to the shorter temporal description obtained by marginalization. This is a statement about path statistics, not about a newly created physical arrow.

## 4. Micro-to-macro cancellation identity

For deterministic observation `g`, let `C(w)` be the set of microtrajectories that map coordinatewise to observed word `w`.

Then

`P_g(w) = sum_{x in C(w)} P_X(x)`.

Reversal is a bijection from `C(w)` to `C(Rw)`, so

`P_g(Rw) = sum_{x in C(w)} P_X(Rx)`.

Subtracting gives

`Delta_g(w) = sum_{x in C(w)} [P_X(x)-P_X(Rx)]`.

Thus an observed time-odd word difference is an exact signed residual of microtrajectory reversal differences. Positive and negative micro contributions can partially or completely cancel under the observation map.

This identity explains the accounting performed by `micro_reversal_contributions`; it does not imply that cancellation is the only useful structural description at arbitrary order.

## 5. First-detection hierarchy in the frozen witness

Stage 4 already proved the exact detection classes of all 15 partitions of `higher_order_hidden_arrow_four_state`:

- four at `L_arrow=1`;
- two at `L_arrow=2`;
- two at `L_arrow=3`;
- seven at `L_arrow=infinity`.

Stage 5 does not rediscover these classes by a larger horizon scan. It uses the Stage 4 exact equivalence result to identify the finite first horizon, then analyzes the exact odd path law only through that already-certified depth.

For `L_arrow=2` and `3`, every lower odd component is exactly zero and the first nonzero component lies in the kernel of temporal marginalization to the preceding horizon.

For `L_arrow=infinity`, Stage 4's finite linear-equivalence certificate implies `O_L=0` for every finite `L`; Stage 5 does not infer infinity from its illustrative `L=1..3` profiles.

## 6. What Stage 5 does not prove

Stage 5 does not establish that every detection order corresponds to a unique graph motif, cycle type, waiting-time pattern, or memory mechanism.

It also does not prove a universal formula predicting `L_arrow` directly from a partition without constructing the relevant observed process.

The bounded claim is narrower:

> the exact first-detection depth is the lowest temporal order with a surviving reversal-odd path component, and in the frozen representative observations the corresponding macro difference can be traced exactly to signed cancellation among compatible irreversible microtrajectories.

Whether a more compact arbitrary-order structural criterion exists remains open after this stage.