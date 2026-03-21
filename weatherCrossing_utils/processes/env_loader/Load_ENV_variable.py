"""
Loads a specific environment variable and returns its value as a string.

This module provides the `Load_env_variable` function, which retrieves the value
of a given environment variable using Python’s `os.getenv`. The function is
decorated with `timer` and `tryer`, adding execution‑time measurement and
structured error handling with colored console messages for clearer feedback.

Function
--------
Load_env_variable(variable_name: str) -> str | None:
    Attempts to load the value of the environment variable specified by
    `variable_name`. The function prints a colored status message before
    retrieving the value. If the variable exists, its value is returned as a
    string; if not, the function returns None.

Behavior
--------
- Uses colored console output to indicate which variable is being loaded.
- Returns the environment variable’s value as a string, even if empty.
- Returns None when the variable does not exist.
- Relies on the `tryer` decorator to catch unexpected errors and provide
    user‑friendly console feedback.
- Measures execution time through the `timer` decorator.

Exports
-------
__all__ = ["Load_env_variable"]
    Makes the environment‑variable loader available for import.

"""


from ...classes import *
from ..wrappers import *

import os

@spacing
@timer
@tryer
def Load_env_variable(variable_name: str) -> str | None:
    print(ConsolColor.PreSetUpColoredTextLine(f"Loading environment variables: {variable_name}", "i_tips"))
    env_variable: str = str(os.getenv(variable_name))

    return env_variable

__all__ = ["Load_env_variable"]