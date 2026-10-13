"""app.py - Reactive marimo app for this project.

Marimo adds reactive controls.
Every function below is a marimo cell.

RUN LOCALLY:

  uv run marimo edit src/cintel/app.py     # edit
  uv run marimo run  src/cintel/app.py     # run as an app (CTRL+c quits)

WASM DEPENDENCIES:

Under WebAssembly (emscripten) the browser has no project environment.
This app uses polars in addition to marimo, so the first cell installs
polars with micropip when running under WASM.

NO LOGGING:

A browser-based WASM app has no persistent Python server to store log files,
so this notebook configures no logging.

PLAN CELLS FIRST

1. Imports (installs WASM deps, returns shared imports and constants)
2. Opening title and introduction (Markdown)
3. Load reference and current data (same cell handles local and WASM
   environments, via cintel.utils_system)
4. Threshold controls (sliders)
5. Compute drift summary (same logic as the CLI pipeline)
6. Show the results (summary table + per-metric drift flags)
7. Closing (Markdown)

Note: marimo triggers @app.cell functions automatically; we never call them.
The names starting with "_" are for our own organization; the engine ignores
them.
"""

# === ONLY THIS AT THE TOP OF THE FILE ===

import marimo

__generated_with = "0.25.0"

app = marimo.App(width="medium")

# === FIRST CELL IMPORTS AND RETURNS DEPENDENCIES TO MAKE IT SELF-CONTAINED ===


@app.cell
async def _():
    import sys

    if sys.platform == "emscripten":
        import micropip

        await micropip.install("polars")

    import marimo as mo
    import polars as pl

    from cintel.utils_stats import compare_error_rates
    from cintel.utils_system import compute_drift_summary, load_system_metrics

    return compare_error_rates, compute_drift_summary, load_system_metrics, mo, pl, sys


# === TITLE AND INTRODUCTION ===


@app.cell
def _(mo):
    mo.md(r"""
    # Drift Detection

    Compares average system behavior between a **reference** period and a
    **current** period, and flags a metric as drifting when the difference
    exceeds the threshold you set.

    Move the sliders below to see how sensitive drift detection becomes.
    """)


# === LOAD REFERENCE AND CURRENT DATA ===


@app.cell
def _(load_system_metrics, mo, sys):
    """Load reference and current data. Two environments, one cell.

    Locally, polars reads both CSVs from data/.
    Under WASM (emscripten), Pyodide's open_url() fetches both CSVs from
    public/ and load_system_metrics() reads them from there instead.
    """
    notebook_location = mo.notebook_location()

    if notebook_location is None:
        raise RuntimeError("Unable to determine notebook location.")

    reference_filename = "reference_metrics.csv"
    current_filename = "current_metrics.csv"

    if sys.platform == "emscripten":
        from pyodide.http import open_url  # ty: ignore[unresolved-import]

        reference_url = notebook_location / "public" / reference_filename
        current_url = notebook_location / "public" / current_filename
        reference_df = load_system_metrics(open_url(str(reference_url)))
        current_df = load_system_metrics(open_url(str(current_url)))
    else:
        data_dir = notebook_location.parents[1] / "data"
        reference_df = load_system_metrics(data_dir / reference_filename)
        current_df = load_system_metrics(data_dir / current_filename)

    return current_df, reference_df


# === THRESHOLD CONTROLS ===

# NOTE: This example uses fixed threshold values.
# The sliders' min/max/default are not dependent on the data,
# so it's safe to build all three in one cell
# (see the imports-cell WASM note above for the general marimo
# rule this follows).
#
# If you improve this to use DATA-DRIVEN thresholds instead,
# e.g. threshold =
# reference_df["requests"].mean() + 2 * reference_df["requests"].std()
# you would need to give that slider its OWN cell, with reference_df
# in its arguments.
#
# WHY: a cell reruns
# (and resets every widget it builds back to default)
# whenever ANY of its listed arguments change.

# If a data-driven slider shares a cell with fixed ones,
# the fixed sliders are forced to depend on reference_df too
# (just by being in the same cell).
# So they'd get silently reset to default any time the
# reference data changes,
# even though they never needed to depend on it at all.
#
# One cell per data-driven slider will keep each slider's reset
# behavior scoped to only what it truly needs.


@app.cell
def _(mo):
    requests_threshold = mo.ui.slider(
        0, 100, value=20, label="Requests drift threshold"
    )
    errors_threshold = mo.ui.slider(0, 10, value=2, label="Errors drift threshold")
    latency_threshold = mo.ui.slider(
        0, 3000, value=1000, step=100, label="Latency drift threshold (ms)"
    )
    mo.vstack([requests_threshold, errors_threshold, latency_threshold])
    return errors_threshold, latency_threshold, requests_threshold


# === COMPUTE DRIFT SUMMARY (SAME LOGIC AS THE CLI PIPELINE) ===


@app.cell
def _(
    compute_drift_summary,
    current_df,
    errors_threshold,
    latency_threshold,
    reference_df,
    requests_threshold,
):
    drift_df = compute_drift_summary(
        reference_df,
        current_df,
        requests_threshold=requests_threshold.value,
        errors_threshold=errors_threshold.value,
        latency_threshold=latency_threshold.value,
    )
    return (drift_df,)


# === COMPUTE STATISTICAL COMPARISON ===


@app.cell
def _(compare_error_rates, current_df, reference_df):
    stats_df = compare_error_rates(reference_df, current_df)
    return (stats_df,)


# === SHOW STATISTICAL RESULTS ===


@app.cell
def _(mo):
    mo.md("""
    ## Statistical Comparison

    Compare mean error rates between reference and current observations.

    The permutation-test p-value provides statistical evidence
    of a difference under the test assumptions.

    Statistical significance does not establish persistent drift
    or operational importance.
    """)


@app.cell
def _(mo, stats_df):
    mo.ui.table(stats_df)


# === SHOW THE RESULTS ===


@app.cell
def _(drift_df, mo):
    drift_summary_dict = drift_df.to_dicts()[0]
    flagged = [
        name.replace("_is_drifting_flag", "")
        for name, value in drift_summary_dict.items()
        if name.endswith("_is_drifting_flag") and value
    ]
    if flagged:
        message = f"**Drifting:** {', '.join(flagged)}"
    else:
        message = "**No metrics are drifting** at these thresholds."
    mo.md(message)


@app.cell
def _(drift_df, mo):
    mo.ui.table(drift_df)


# === TYPICALLY END WITH A MARKDOWN SOURCE LINK AND CLOSING ===


@app.cell
def _(mo):
    mo.md(r"""
    ---
    [😊 Learn more at marimo.io](https://marimo.io/)
    ---

    **Running locally?**
    To stop the app, click in the VS Code terminal,
    then press **CTRL** and **c** together (CTRL+c).
    When it asks "Are you sure you want to quit? (y/N)",
    type **y** and press **Enter**.
    ---
    """)


if __name__ == "__main__":
    app.run()
