# cintel-05-drift-detection

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![CI](https://github.com/denisecase/cintel-05-drift-detection/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/denisecase/cintel-05-drift-detection/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://denisecase.github.io/cintel-05-drift-detection/)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> Detect changes in system behavior by comparing current and reference data.

## Project Overview

Author: Denise Case

Date: 2026 October

This project introduces drift detection.

The goal is to compare current measurements against a reference period
and identify changes that exceed defined thresholds.

The project is configured in
[pyproject.toml](pyproject.toml).

## Data

The example uses two datasets from `data/`:

- **Reference data** - measurements representing earlier system behavior.
- **Current data** - measurements representing a more recent period.

Both datasets include:

- `requests` - number of requests handled.
- `errors` - number of failed requests.
- `total_latency_ms` - total response time in milliseconds.

## Approach

The pipeline uses Polars to:

1. Calculate summary statistics for both periods.
2. Calculate differences between reference and current averages.
3. Compare the differences against drift thresholds.
4. Record which measurements indicate drift.

Explore these project components:

- [pyproject.toml](pyproject.toml) - project configuration and dependencies.
- [src/cintel/drift_detector.py](src/cintel/drift_detector.py) - drift detection pipeline.
- [data/](data/) - reference and current measurements.
- [artifacts/](artifacts/) - generated comparisons.
- [tests/](tests/) - automated tests.
- [.github/workflows/](.github/workflows/) - automated checks and documentation deployment.
- [docs/](docs/) - project documentation.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
to set up your machine and project environment.

From a VS Code terminal in the project root:

```shell
uv run python -m cintel.drift_detector
```

## Results

The pipeline produces:

- `artifacts/drift_summary.csv` - summary comparisons and drift flags.
- `artifacts/drift_summary_long.csv` - comparison results in a longer format.

Review the differences and drift flags.
Consider whether the selected thresholds are appropriate
for the monitored system.

Successful execution produces a terminal message:

```shell
========================
Pipeline executed successfully!
========================
```

A `project.log` file is created in the project root.

This confirms that the Python pipeline executes
and the logging system works.

## Verification

Run the automated tests:

```shell
uv run pytest
```

## Project Documentation

The [hosted documentation site](https://denisecase.github.io/cintel-05-drift-detection/)
is published using Zensical and GitHub Pages.

The documentation site is used to present the project report,
covering such sections as data, methods, results, visualizations,
interpretation, and conclusions.

## CI/CD and GitHub Actions

This project includes continuous integration and continuous deployment (CI/CD)
to check project files and publish the docs.
GitHub Actions include:

- [CI: Python and Documentation Checks](https://github.com/denisecase/cintel-05-drift-detection/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/denisecase/cintel-05-drift-detection/actions/workflows/deploy-zensical.yml)

## Developer Reference

Follow the
[Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
for **detailed instructions and troubleshooting**.

### Initialize and Update the Python Environment

With the project open in VS Code, open a VS Code terminal.
Paste each command and hit Enter or Return after to run it.

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

Set up and run the git hooks to perform
basic checks automatically before
any changes get pushed to GitHub.

In the VS Code terminal,
paste each command and hit Enter or Return after to run it.

```shell
uv run prek install --force
uv run prek update --freeze --cooldown-days 7

git add -A
uv run prek run --all-files
# repeat if changes were made
uv run prek run --all-files
```

### Run Common Chores

Run linters, formatters, type checks, tests, and
build the documentation.

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git add-commit-push to GitHub

After making useful changes, save your work to GitHub.

```shell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Developer Tools

This project uses professional Python tools to support development,
testing, documentation, and code quality.

- [uv](https://docs.astral.sh/uv/) - Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) - Python linting and formatting, configured in [.ruff.toml](.ruff.toml).
- [ty](https://docs.astral.sh/ty/) - Python type checking.
- [pytest](https://docs.pytest.org/) - automated Python testing, configured in [.pytest.toml](.pytest.toml).
- [prek](https://prek.j178.dev/) - Git hooks and automated checks, configured in [prek.toml](prek.toml).
- [Zensical](https://zensical.org/) - project documentation, configured in [zensical.toml](zensical.toml).

## Links

- [Hosted Documentation](https://denisecase.github.io/cintel-05-drift-detection/)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)
