"""r-arrow finite stochastic-process tools."""

from .benchmarks import (
    biased_four_cycle,
    biased_three_cycle,
    higher_order_hidden_arrow_four_state,
    reversible_three_cycle,
)
from .coarse_grain import (
    declared_partitions,
    is_strongly_lumpable,
    observed_arrow_strength,
    observed_path_distribution,
    partition_label,
    robustness_ratio,
    set_partitions,
)
from .irreversibility import arrow_strength, biased_cycle_analytic_arrow
from .markov import (
    detailed_balance_holds,
    probability_current,
    stationary_distribution,
    validate_transition_matrix,
)
from .structural import (
    first_asymmetric_horizon,
    macro_flux_is_symmetric,
    observed_paths_are_reversal_symmetric,
    one_step_arrow_visible_by_flux,
    path_distribution_is_reversal_symmetric,
    reversal_asymmetry_witnesses,
    stationary_macro_flux,
)
from .trajectories import path_distribution, path_probability, reverse_path

__all__ = [
    "arrow_strength",
    "biased_cycle_analytic_arrow",
    "biased_four_cycle",
    "biased_three_cycle",
    "declared_partitions",
    "detailed_balance_holds",
    "first_asymmetric_horizon",
    "higher_order_hidden_arrow_four_state",
    "is_strongly_lumpable",
    "macro_flux_is_symmetric",
    "observed_arrow_strength",
    "observed_path_distribution",
    "observed_paths_are_reversal_symmetric",
    "one_step_arrow_visible_by_flux",
    "partition_label",
    "path_distribution",
    "path_distribution_is_reversal_symmetric",
    "path_probability",
    "probability_current",
    "reversal_asymmetry_witnesses",
    "reverse_path",
    "reversible_three_cycle",
    "robustness_ratio",
    "set_partitions",
    "stationary_distribution",
    "stationary_macro_flux",
    "validate_transition_matrix",
]
