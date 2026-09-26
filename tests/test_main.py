"""tests/test_main.py - Smoke test for the example.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
"""


def test_app_runs() -> None:
    """Confirm the example module runs without error."""
    from cintel.drift_detector import main

    main()
