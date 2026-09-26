# Glossary

## Quick Lookup

Common terms used in this module:

- **Baseline** - a reference period representing expected or normal system behavior
- **Reference Dataset** - the dataset representing baseline system behavior
- **Current Dataset** - the dataset representing recent system observations
- **Baseline Comparison** - comparing current metrics to a reference baseline
- **Change Detection** - identifying meaningful differences between time periods
- **Statistical Drift Detection** - using statistical methods to determine whether changes are significant
- **Drift** - a sustained change in system behavior over time, observed when recent data consistently differs from a historical reference or baseline.

## Baseline

A **baseline** represents expected system behavior based on a historical period.
Analysts often compare current data to a baseline to determine whether the system is behaving normally.

## Reference Dataset

A dataset representing the **baseline period** used for comparison.
Example: last week's system metrics.

## Current Dataset

A dataset representing **recent system behavior**.
Example: today's or this week's system metrics.

## Baseline Comparison

The process of comparing summary statistics between two time periods.
Baseline comparisons help analysts identify potential changes in system behavior.
Example:

```text
reference_avg_latency
current_avg_latency
difference = current - reference
```

## Change Detection

The process of identifying meaningful differences between datasets or time periods.

## Drift

**Drift** occurs when system behavior changes persistently over time relative to a historical baseline.
Baseline comparisons can provide early evidence that drift may be occurring.
Examples include:

- increasing latency
- rising error rates
- declining throughput

## Statistical Drift Detection

A more advanced approach that uses statistical tests to determine whether observed changes are likely due to random variation or represent a true shift in system behavior.
These techniques provide stronger evidence that system behavior has changed.
Examples include:

- distribution comparison tests
- hypothesis tests
- statistical control methods

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
