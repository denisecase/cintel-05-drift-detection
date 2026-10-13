"""utils_stats.py.

Statistical comparisons for system monitoring.

Compare error rates between reference and current observations.

A permutation test evaluates evidence of a difference in mean
error rates. Statistical evidence does not establish persistence,
causation, or operational importance.
"""

from collections.abc import Sequence
from statistics import fmean

import polars as pl
from scipy.stats import permutation_test


def extract_error_rates(df: pl.DataFrame) -> list[float]:
    """Return error rates for observations with positive request counts."""
    required_columns = {"requests", "errors"}

    if not required_columns.issubset(df.columns):
        raise ValueError("Data must contain requests and errors columns.")

    rates_df = df.filter(pl.col("requests") > 0).select(
        (pl.col("errors") / pl.col("requests")).alias("error_rate")
    )

    rates = [float(value) for value in rates_df["error_rate"].to_list()]

    if len(rates) < 2:
        raise ValueError("At least two valid observations are required.")

    return rates


def difference_in_means(
    reference: Sequence[float],
    current: Sequence[float],
) -> float:
    """Return the current mean minus the reference mean."""
    return fmean(current) - fmean(reference)


def compare_error_rates(
    reference_df: pl.DataFrame,
    current_df: pl.DataFrame,
) -> pl.DataFrame:
    """Compare mean error rates using a two-sided permutation test.

    Uses 9,999 randomized permutations and a fixed random seed
    for reproducible results.

    The test assumes observations are exchangeable under the null
    hypothesis. Temporal dependence may invalidate this assumption.

    Returns a one-row DataFrame containing descriptive statistics
    and the permutation-test p-value.
    """
    reference_rates = extract_error_rates(reference_df)
    current_rates = extract_error_rates(current_df)

    reference_mean = fmean(reference_rates)
    current_mean = fmean(current_rates)

    result = permutation_test(
        (reference_rates, current_rates),
        statistic=difference_in_means,
        permutation_type="independent",
        alternative="two-sided",
        n_resamples=9_999,
        rng=42,
    )

    return pl.DataFrame(
        {
            "reference_count": [len(reference_rates)],
            "current_count": [len(current_rates)],
            "reference_mean_error_rate": [reference_mean],
            "current_mean_error_rate": [current_mean],
            "difference_percentage_points": [100.0 * (current_mean - reference_mean)],
            "permutation_p_value": [float(result.pvalue)],
        }
    )
