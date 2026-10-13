# Glossary

## Quick Lookup

Common terms used in this module:

- **Baseline** - reference behavior used for comparison, not necessarily normal or desirable behavior
- **Reference Dataset** - the dataset representing baseline system behavior
- **Current Dataset** - the dataset representing recent system observations
- **Baseline Comparison** - comparing current metrics to a reference baseline
- **Drift Flag** - an indicator that a measured difference exceeds a defined threshold
- **Change Detection** - identifying differences between datasets or time periods
- **Drift** - a meaningful change in system behavior or data distribution relative to a baseline
- **Statistical Drift Detection** - using statistical methods to evaluate evidence of changes in data distributions

## Baseline

A **baseline** represents reference system behavior, often measured during a historical period.

Analysts compare current observations to this reference to identify changes.

A baseline does not necessarily represent normal, healthy, or desirable behavior.
Its suitability depends on the context and purpose of the analysis.

## Reference Dataset

A dataset representing the **baseline period** used for comparison.
Example: last week's system metrics.

## Current Dataset

A dataset representing **recent system behavior**.
Example: today's or this week's system metrics.

## Baseline Comparison

The process of comparing summary statistics between two datasets or time periods.

In this project, the pipeline compares means:

```text
difference = current_mean - reference_mean
```

Positive differences indicate an increase.
Negative differences indicate a decrease.

A difference alone does not establish that meaningful drift has occurred.

## Drift Flag

A **drift flag** indicates that the absolute difference between a current mean and a reference mean exceeds a configured threshold.

```text
drift_flag = abs(difference) > threshold
```

A flagged metric provides evidence that further investigation may be warranted.

A drift flag does not establish statistical significance or persistence.

## Change Detection

The process of identifying meaningful differences between datasets or time periods.

## Drift

**Drift** is a meaningful change in system behavior or data distribution relative to a reference baseline.

Examples include:

- increasing latency
- rising error rates
- declining throughput

Baseline comparisons can provide evidence of possible drift.

However, comparing the means of two datasets does not establish whether a change is persistent or statistically significant.

Additional observations or statistical analysis may be needed.

## Statistical Drift Detection

An approach that uses statistical methods to evaluate evidence that a data distribution has changed relative to a reference.

Examples include:

- distribution comparison tests
- hypothesis tests
- statistical control methods

These methods account for sampling variability and can provide stronger evidence of change than fixed thresholds alone.

Statistical significance does not necessarily imply practical importance or persistent change.

## Summary Statistics

Simple numerical summaries used to describe a dataset.
Summary statistics help compare system behavior between two periods.
Common examples include:

- mean (average)
- minimum
- maximum
- count

---

[◄ Back to 🏠 Home](index.md)
