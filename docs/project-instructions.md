# Project Instructions

## Goal

Apply **baseline comparison and drift detection**
to investigate changes in system behavior.

## A. Set Up Machine

Complete [Workflow A: Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/)
if your machine is not ready.

## B. Explore Example Project

Follow [Workflow B: Explore Example Project](https://denisecase.github.io/pro-analytics-02/workflow-b-explore-example-project/).

Explore how the example:

- Reads reference and current datasets.
- Calculates summary statistics for each period.
- Computes differences between corresponding means.
- Applies thresholds to produce drift flags.
- Saves the comparisons as artifacts.

Consider how the selected metrics and thresholds
affect the interpretation of system change.

## C. Start New Project

Follow [Workflow C: Start New Project](https://denisecase.github.io/pro-analytics-02/workflow-c-start-new-project/).

IMPORTANT: New repository name:
**cintel-05-drift-detection**.

VERIFY: You have completed git add-commit-push to GitHub at least twice.

## D. Apply Skills

Follow [Workflow D: Apply Skills](https://denisecase.github.io/pro-analytics-02/workflow-d-apply-skills/).

**Your problem:** Determine whether an increase
in errors reflects increased workload
or a change in service reliability.

You may use the example reference and current datasets
or choose two comparable datasets from another scenario.

### Progression 1. Your Project Works Like the Example

Ensure your new custom project runs like the example.

Verify that key files have been updated to use **your GitHub account** and
the **new custom repository name**.

### Progression 2. Make a Technical Modification

Change one drift threshold.

Run the pipeline again and observe whether
the corresponding drift flag changes.

Explain the effect of your modification.

### Progression 3. Apply to a New Problem

Investigate changes in service reliability,
not just changes in raw activity counts.

- Calculate error rates for both periods.
- Compare reference and current error rates.
- Choose and explain a meaningful comparison threshold.
- Identify changes that may warrant investigation.
- Save the comparison results as artifacts.
- Interpret the findings.

Distinguish observed differences from evidence
of meaningful or persistent drift.

## E. Finalize Project

Follow [Workflow E: Finalize Project](https://denisecase.github.io/pro-analytics-02/workflow-e-finalize/).

Use `docs/index.md` to report:

- Reference and current datasets.
- Comparison metrics and thresholds.
- Technical modifications.
- Differences and drift indicators.
- A visual comparing the periods.
- Interpretation, limitations, and possible actions.

Include a clickable link to your repository and artifacts.

## Success

- [ ] README.md project-specific links use **your GitHub account**
- [ ] README.md project-specific links use **your custom repository name**.
- [ ] docs/index.md project-specific links use **your GitHub account**
- [ ] docs/index.md project-specific links use **your custom repository name**.
- [ ] pyproject.toml `name` has been changed to use **your custom repository name**.
- [ ] The `src/cintel` folder reflects your authorship and custom work.
- [ ] All necessary commands are provided and work successfully.
- [ ] Links to the Professional Python Guide (pro-analytics-02) remain unchanged.
- [ ] Commit history shows **at least** the git add-commit-push history required in the instructions.

---

[◄ Back to Home](index.md)
