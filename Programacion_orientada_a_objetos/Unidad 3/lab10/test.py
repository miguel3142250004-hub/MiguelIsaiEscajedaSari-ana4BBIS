#Lab 10. Automated testing
#Research and add below what the pytest library
# is used for and what is required to use it.

# --- RESEARCH ---------------------------------------------------------------
# What is pytest used for?
#   pytest is a testing framework for Python used to write and run automated
#   tests (unit, integration, functional). It lets you verify that your code
#   behaves as expected using plain `assert` statements, and gives detailed
#   reports when a test fails. Main features: fixtures (@pytest.fixture) to
#   prepare reusable test data, parametrized tests (@pytest.mark.parametrize),
#   exception checking (pytest.raises), automatic test discovery, and plugins.
#
# What is required to use it?
#   - Python 3.8 or higher installed.
#   - pytest installed via pip:  pip install pytest
#   - (Optional) a virtual environment (venv) to isolate dependencies.
#   - Test files named test_*.py or *_test.py, with test functions named test_*.
#   - Run it from the terminal with:  pytest   or   pytest -v

import pytest
