"""drift_detector.py - Project script (example).

Author: Your Name Here
Date: 2026-mm-dd

Reference and Current System Metrics Data

- Data is taken from a system measured during two different periods.
- The reference data represents earlier, expected system behavior.
- The current data represents more recent system behavior.
- Each row represents one observation of system metrics.

- Each CSV file includes these columns:
  - requests: number of requests handled
  - errors: number of failed requests
  - total_latency_ms: total response time in milliseconds

Purpose

- Read reference and current system metrics from CSV files.
- Compare the two datasets using simple summary statistics.
- Detect meaningful changes in average system behavior.
- Provide a simple baseline comparison approach that supports drift detection.
- Save the comparison summary as a CSV artifact.
- Log the pipeline process to assist with debugging and transparency.

Questions to Consider

- What does "normal" system behavior look like?
- How can we compare current measurements to a historical baseline?
- When does a difference become large enough to indicate meaningful change?

Paths (relative to repo root)

    INPUT FILE: data/reference_metrics.csv
    INPUT FILE: data/current_metrics.csv
    OUTPUT FILE: artifacts/drift_summary.csv

Terminal command to run this file from the root project folder

    uv run python -m cintel.drift_detector

DESIGN:

Use this file to first learn and then apply your skills.

Reusable functions that do the work are kept in a utils file.
We import functions and pass in what they need through their parentheses.
Shared utility functions can be imported into a Python
module or a reactive marimo notebook app.

Reusable visualization functions may come from sources such as eda-vizkit.

SKILLS:

- Reading CSV files into Polars DataFrames.
- Defining and using constants for thresholds.
- Logging for debugging and transparency.
- Comparing reference and current datasets to detect drift.
"""

# === DECLARE IMPORTS ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
import polars as pl

from cintel.utils_system import compute_drift_summary, load_system_metrics

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P5", level="DEBUG")

# === DEFINE GLOBAL PATHS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

REFERENCE_FILE: Final[Path] = DATA_DIR / "reference_metrics.csv"
CURRENT_FILE: Final[Path] = DATA_DIR / "current_metrics.csv"

OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "drift_summary.csv"
SUMMARY_LONG_FILE: Final[Path] = ARTIFACTS_DIR / "drift_summary_long.csv"

# === DEFINE THRESHOLDS ===

# Analysts need to know their data and
# choose thresholds that make sense for their specific use case.

# Review the reference metrics to understand typical values
# and variability before setting thresholds.

# In this example, we compare current metrics to a reference period
# and flag drift when the difference exceeds these thresholds:

REQUESTS_DRIFT_THRESHOLD: Final[float] = 20.0
ERRORS_DRIFT_THRESHOLD: Final[float] = 2.0
LATENCY_DRIFT_THRESHOLD: Final[float] = 1000.0

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "REFERENCE_FILE", REFERENCE_FILE)
    log_path(LOG, "CURRENT_FILE", CURRENT_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    # Ensure the artifacts folder exists.
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # ----------------------------------------------------
    # STEP 1: READ REFERENCE AND CURRENT CSV INTO DATAFRAMES
    # ----------------------------------------------------
    # load_system_metrics() wraps polars' read_csv() — see utils_system.py.
    # Both files share the same schema (requests, errors, total_latency_ms),
    # so the same loader works for both periods.
    reference_df: pl.DataFrame = load_system_metrics(REFERENCE_FILE)
    current_df: pl.DataFrame = load_system_metrics(CURRENT_FILE)

    LOG.info(f"Loaded {reference_df.height} reference records")
    LOG.info(f"Loaded {current_df.height} current records")

    # ----------------------------------------------------
    # STEP 2: SUMMARIZE EACH PERIOD, COMPARE, AND FLAG DRIFT
    # ----------------------------------------------------
    # compute_drift_summary() does the full comparison in one call:
    # averages each period, combines them into one row, computes the
    # difference of means, and flags drift where |difference| exceeds
    # the given threshold — see utils_system.py for exactly how.
    LOG.info(f"REQUESTS_DRIFT_THRESHOLD: {REQUESTS_DRIFT_THRESHOLD}")
    LOG.info(f"ERRORS_DRIFT_THRESHOLD: {ERRORS_DRIFT_THRESHOLD}")
    LOG.info(f"LATENCY_DRIFT_THRESHOLD: {LATENCY_DRIFT_THRESHOLD}")

    drift_df: pl.DataFrame = compute_drift_summary(
        reference_df,
        current_df,
        requests_threshold=REQUESTS_DRIFT_THRESHOLD,
        errors_threshold=ERRORS_DRIFT_THRESHOLD,
        latency_threshold=LATENCY_DRIFT_THRESHOLD,
    )

    LOG.info("Calculated summary differences and drift flags")

    # ----------------------------------------------------
    # STEP 3: SAVE THE FLAT DRIFT SUMMARY AS AN ARTIFACT
    # ----------------------------------------------------
    drift_df.write_csv(OUTPUT_FILE)
    LOG.info(f"Wrote drift summary file: {OUTPUT_FILE}")

    # Take a look at the summary dataframe.
    # Lots of columns with one row of values.
    LOG.info("Drift summary dataframe:")
    LOG.info(drift_df)
    LOG.info("Let's make that a bit nicer to read...")
    LOG.info("All remaining steps are about creating a nicer display.")

    # ----------------------------------------------------
    # OPTIONAL STEP 3.1: LOG THE SUMMARY ONE FIELD PER LINE
    # ----------------------------------------------------
    # drift_df has one row with many columns.
    # Convert that one row to a dictionary so we can log:
    # column_name: value

    # The Polars to_dicts() function returns a list of dictionaries, one per row.
    # the [0] gets the first (and only) dictionary from the list.
    # We often count starting at zero
    # because the first row is 0 away from the start of the dataframe.
    drift_summary_dict = drift_df.to_dicts()[0]

    LOG.info("========================")
    LOG.info("Drift Detection Process: ")
    LOG.info("========================")
    LOG.info("1. Summarize each period with means.")
    LOG.info("2. Compute difference of means.")
    LOG.info("3. Flag drift if absolute difference of means exceeds a threshold.")
    LOG.info("========================")

    LOG.info("Drift summary (one field per line):")
    for field_name, field_value in drift_summary_dict.items():
        LOG.info(f"{field_name}: {field_value}")

    # ----------------------------------------------------
    # OPTIONAL STEP 4: CREATE A LONG-FORM ARTIFACT FOR DISPLAY
    # ----------------------------------------------------
    # Create a second artifact with one field per row.
    # This is easier to read than a single very wide row.
    # We create a new dataframe with two columns:
    # - field_name: the name of the summary field
    # - field_value: the value of the summary field (converted to string for display)

    drift_summary_long_df = pl.DataFrame(
        {
            "field_name": list(drift_summary_dict.keys()),
            "field_value": [str(value) for value in drift_summary_dict.values()],
        }
    )
    # ----------------------------------------------------
    # OPTIONAL STEP 4.1: SAVE THE LONG-FORM DRIFT SUMMARY AS AN ARTIFACT
    # ----------------------------------------------------
    drift_summary_long_df.write_csv(SUMMARY_LONG_FILE)
    LOG.info(f"Wrote long summary file: {SUMMARY_LONG_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
