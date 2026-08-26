# Stage 1 Baseline — Exact Three-State Arrow Benchmark

## Status

`stage1_status = calibration_passed`

Stage 1 calibrates the path-level time-reversal-asymmetry observable frozen in Stage 0. It is a benchmark/validation result, not a novelty or empirical-discovery claim.

## Frozen models

### Reversible control

- clockwise `p = 3/8`
- counterclockwise `q = 3/8`
- self-loop `s = 1/4`

### Biased cycle

- clockwise `p = 1/2`
- counterclockwise `q = 1/4`
- self-loop `s = 1/4`

Both chains have exact stationary distribution

`pi = (1/3, 1/3, 1/3)`.

## Independent calibration checks

### 1. Stationary current

For the reversible control, every stationary current is exactly zero.

For the biased cycle,

- `J_01 = 1/12`
- `J_12 = 1/12`
- `J_20 = 1/12`

with the reverse directions equal to `-1/12`.

Therefore the biased benchmark has a clockwise stationary circulation even though its one-time stationary state distribution is uniform.

### 2. Detailed balance

- reversible control: satisfied exactly;
- biased cycle: violated exactly.

### 3. Exhaustive trajectory enumeration

All paths are enumerated rather than sampled.

| Horizon `L` | Number of paths |
|---:|---:|
| 1 | 9 |
| 2 | 27 |
| 3 | 81 |
| 4 | 243 |

As a frozen example in the biased chain,

- `Pr(0,1,2) = 1/12`;
- `Pr(2,1,0) = 1/48`.

The forward path is four times as probable as its reverse.

### 4. Path-level arrow strength

The frozen observable is

`A_L = D_KL(P(path) || P(reversed path))`.

For the reversible control,

`A_L = 0`

for every frozen horizon `L=1..4`.

For the biased cycle, direct exhaustive enumeration agrees with the independent analytic oracle

`A_L = (L/4) ln 2`.

| `L` | Enumerated `A_L` | Analytic `A_L` |
|---:|---:|---:|
| 1 | 0.17328679513998632 | 0.17328679513998632 |
| 2 | 0.34657359027997264 | 0.34657359027997264 |
| 3 | 0.5198603854199589 | 0.5198603854199589 |
| 4 | 0.6931471805599453 | 0.6931471805599453 |

The growth is linear in path horizon for this frozen Markov benchmark.

## CI validation

Initial Stage 1 implementation PR workflow run #1 passed all **17 tests**.

The tests independently validate:

- stochastic-matrix validity;
- exact stationary distributions;
- exact probability currents;
- detailed balance / detailed-balance violation;
- exhaustive path counts;
- exact path-distribution normalization;
- frozen forward/reverse example probabilities;
- zero arrow for the reversible control;
- positive arrow for the biased benchmark;
- agreement with `A_L=(L/4) ln 2`;
- linear horizon growth;
- KL non-negativity on the frozen models.

## What Stage 1 establishes

Stage 1 establishes a trusted finite benchmark for detecting **observable trajectory-level temporal direction**:

- a reversible stationary process is assigned zero arrow strength;
- an irreversible stationary circulation is assigned positive arrow strength;
- the same reversible/irreversible classification is independently supported by stationary current and detailed balance;
- exhaustive trajectory enumeration agrees with an analytic result.

This is sufficient to use the same path-law machinery as the measurement layer for Stage 2 coarse-graining.

## What Stage 1 does not establish

Stage 1 does **not** establish:

- ontological becoming;
- a fundamental arrow of time;
- thermodynamic entropy production without additional physical interpretation;
- a new empirical fact;
- robustness under coarse-graining;
- local-arrow alignment across distinct systems.

Those claims are outside the Stage 1 calibration contract.

## Meaning checkpoint

The practical meaning of Stage 1 is simple:

> We now have an independently checked instrument that distinguishes a process whose observed histories are statistically reversible from one whose observed histories carry a directional circulation.

The next scientific question is no longer "can we measure the arrow in this toy model?" but the Stage 2 question:

> When state information is deliberately lost, how much of this measurable trajectory-level direction remains visible?

`observable irreversibility != ontological becoming`

`Stage 1 calibration != new empirical discovery`
