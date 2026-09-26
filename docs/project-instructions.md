# Project Instructions

## WEDNESDAY: Complete Workflow Phase 1-3

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/).

Complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Read & Understand**
3. Phase 3. **Take Ownership**

## FRIDAY/SUNDAY: Complete Workflow Phases 4-5

Complete:

1. Phase 4. **Make a Technical Modification**
2. Phase 5. **Apply the Skills to a New Problem**

## Topic

Drift detection for monitoring changes in system behavior.

In this project, you compare **recent system behavior** with a **baseline reference period** to determine whether the system has changed.

Drift detection helps analysts determine when a system is behaving differently than expected.

## Learning Objectives

After completing this project, you should be able to:

- Explain what drift means in a monitoring system
- Compare current observations to a reference baseline
- Detect when system metrics shift away from normal behavior
- Run and validate a professional Python project
- Interpret evidence that suggests system behavior has changed

## Example Code

The example file is located in:

```text
src/cintel/drift_detector_case.py
```

It demonstrates:

- reading a **reference dataset** representing baseline behavior
- reading a **current dataset** representing recent observations
- computing summary statistics for both periods
- comparing the two periods to detect drift
- writing results to an artifacts file
- logging the pipeline process

Run the example and review the code before creating your own version.

## Dataset

The example datasets are located in the `data/` folder.

Typical files include:

- `reference_metrics_case.csv`
- `current_metrics_case.csv`

The **reference dataset** represents normal system behavior.

The **current dataset** represents more recent system activity.

Drift detection compares these two periods to determine whether the system has changed.

## Your Phase 4: Technical Modification Task

Using the example as a guide:

1. Copy `src/cintel/drift_detector_case.py`.
2. Rename the copy to `src/cintel/drift_detector_yourname.py`.
3. Run your copied file to confirm it executes correctly.
4. Modify the program by changing how drift is evaluated.

Possible modifications include:

- adjusting the drift threshold
- comparing additional metrics
- changing the summary statistic used for comparison
- adding additional logging or output columns

Then:

- run the project
- confirm the drift results appear in the output artifact
- confirm the program logs useful messages

The goal of this phase is to practice modifying a working drift detection pipeline.

## Phase 5: Apply the Skills

In Phase 5 you apply drift detection to a new situation.

Possible approaches include:

- comparing two different time periods in a dataset
- detecting drift in website traffic or system performance
- evaluating whether error rates or latency have shifted
- monitoring changes in operational metrics

Update your documentation in `docs/` to explain:

- what datasets you compared
- what drift indicators you used
- what changes you observed
- what those changes might mean for the system

**Drift detection** is an important component of **continuous intelligence**,
helping analysts identify when system behavior begins to change.

If you would like to apply these skills to a real dataset instead of the provided example data, see suggested datasets:

https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/

---

[◄ Back to 🏠 Home](index.md)
