# Detecting Changes in System Behavior

Continuous Intelligence | Project 05 | Example Report

## Overview

This project examines whether recent system behavior
differs meaningfully from an earlier reference period.

The objective is to detect changes in operational metrics
that may indicate a need for investigation.

## Data

Two datasets represent different observation periods:

- Reference data representing earlier behavior.
- Current data representing more recent behavior.

Each contains measurements of requests,
errors, and total latency.

[View Reference Data](https://github.com/denisecase/cintel-05-drift-detection/blob/main/data/reference_metrics_case.csv)

[View Current Data](https://github.com/denisecase/cintel-05-drift-detection/blob/main/data/current_metrics_case.csv)

## Methods

The pipeline calculates the mean of each metric
for both observation periods.

It then calculates:

    difference = current_mean - reference_mean

Drift is flagged when the absolute difference
exceeds the configured threshold.

The example thresholds are:

- Requests: 20.
- Errors: 2.
- Total latency: 1,000 milliseconds.

These thresholds are illustrative and should
be justified for a production monitoring system.

## Results

| Metric             | Reference Mean | Current Mean | Difference |
| ------------------ | -------------: | -----------: | ---------: |
| Requests           |          128.3 |        164.5 |      +36.2 |
| Errors             |            2.3 |          6.3 |       +4.0 |
| Total latency (ms) |          3,835 |        5,670 |     +1,835 |

**All three metrics exceeded their configured thresholds.**

[View Drift Results](https://github.com/denisecase/cintel-05-drift-detection/blob/main/artifacts/drift_summary_case.csv)

[View Detailed Summary](https://github.com/denisecase/cintel-05-drift-detection/blob/main/artifacts/drift_summary_long_case.csv)

## Interpretation

The current period shows higher average request volume,
higher average errors, and greater total latency.

These changes suggest that the system is operating
differently from its reference behavior.

An analyst could investigate whether the changes
reflect increased workload, changing demand,
or a potential performance problem.

## Limitations

The approach compares means using fixed thresholds.

It does not account for variability,
statistical significance, or seasonal patterns.

Higher request volume may also explain part
of the increase in errors and total latency.

Additional normalized signals, such as error rate
and average latency per request, would help
distinguish workload changes from degraded performance.

## Conclusion

Baseline comparisons provide a practical starting point
for detecting changes in operational behavior.

Drift indicators are evidence for investigation,
not proof that a system is malfunctioning.

## Documentation Index

- **Home** - this landing page
- [**Project Instructions**](project-instructions.md)
- [**Glossary**](glossary.md)
- [**API**](api.md)
- [**Reactive App**](./app/index.html)

## Project Links

- [GitHub Repository](https://github.com/denisecase/cintel-05-drift-detection)
- [Example Pipeline](https://github.com/denisecase/cintel-05-drift-detection/blob/main/src/cintel/drift_detector.py)
- [Results and Artifacts](https://github.com/denisecase/cintel-05-drift-detection/tree/main/artifacts)

## Project Resources

- [Project Instructions](project-instructions.md)
- [Professional Python Guide](https://denisecase.github.io/pro-analytics-02/)
- [Professional Python Project Explainer](https://pup-pack.github.io/professional-python-project-explainer/).
- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)
