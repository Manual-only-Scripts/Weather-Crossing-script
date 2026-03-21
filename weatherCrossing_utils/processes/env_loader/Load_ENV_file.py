"""
Loads environment variables from a .env file into the application environment.

This module provides the `Load_env_file` function, which uses the `python-dotenv`
library to load key–value pairs from a specified `.env` file. The function is
decorated with `timer` and `tryer`, adding execution‑time measurement and
structured error handling with colored console messages for clearer feedback.

Function
--------
Load_env_file(file_path: str = ".env"):
    Loads environment variables from the file located at `file_path`. If the
    file exists and is readable, its contents are added to the process
    environment. A colored status message is printed before loading begins.

Behavior
--------
- Uses colored console output to indicate which environment file is being loaded.
- Loads variables into the environment using `load_dotenv`.
- Relies on the `tryer` decorator to catch unexpected errors and provide
    user‑friendly console feedback.
- Measures execution time through the `timer` decorator.

Exports
-------
__all__ = ["Load_env_file"]
    Makes the environment‑file loader available for import.

"""


from ...classes import *
from ..wrappers import *

from dotenv import load_dotenv

@spacing
@timer
@tryer
def Load_env_file(file_path: str = ".env"):
    print(ConsolColor.PreSetUpColoredTextLine(f"Loading environment file: {file_path}", "i_tips"))

    load_dotenv(file_path)


__all__ = ["Load_env_file"]