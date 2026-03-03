"""
This module orchestrates the main execution flow of the application. It handles
environment loading, output directory preparation, API data retrieval, and
logging the fetched data in user‑selected formats.

Core Responsibilities
---------------------
- Load environment variables from a .env file.
- Ensure that the output directory defined by OUT_PATH exists or is created.
- Interactively fetch data from an external API.
- Log the retrieved data in PDF, JSON, or both formats based on user input.

Functions
---------
_OutPutDirExists():
    Checks whether the output directory specified by the OUT_PATH environment
    variable exists. If it does not exist, the function attempts to create it.
    Returns True if the directory exists or is successfully created.

_LoggingWaySelection():
    Determines the logging format(s) selected by the user. Depending on the
    choice (PDF, JSON, or both), it retrieves data from the API and passes it
    to the appropriate logging functions. If no valid option is selected, a
    warning message is displayed.

main_process():
    Entry point of the module. Loads environment variables, prepares the output
    directory, and enters an interactive loop where:
        1. The user selects the logging format.
        2. API data is fetched and logged accordingly.
        3. The user decides whether to continue fetching additional data.
    The loop terminates when the user chooses not to continue.

Usage
-----
Call `main_process()` to start the interactive data‑fetching and logging
workflow. The process continues until the user explicitly stops it.
"""


from .process.inputs.complex.Ask_Logging_Extention import *
from .process.env_loader.Load_ENV_variable import *
from .process.env_loader.Load_ENV_file import *
from .process.loggers.JSON_log_file import *
from .process.loggers.PDF_log_file import *
from .process.api.FETCH_api import *
from .process.wrappers import *

import os

def _OutPutDirExists():
    return os.path.exists(f"{Load_env_variable('OUT_PATH')}") or os.makedirs(f"{Load_env_variable('OUT_PATH')}")

def _LoggingWaySelection():
    match ask_for_log_file_extention():
            case ["pdf"]:
                pdf_log_file(fetch_api())
            case ["json"]:
                json_log_file(fetch_api())
            case ["pdf", "json"]:
                data = fetch_api()
                pdf_log_file(data)
                json_log_file(data)
            case _:
                print(ConsolColor.PreSetUpColoredTextLine("No logging way is selected. No logging will be done.", "warning"))

def main_process():
    Load_env_file()

    if _OutPutDirExists():
        print(ConsolColor.PreSetUpColoredTextLine(f"Output directory is ready at: {Load_env_variable('OUT_PATH')}", "success"))
    
    #else:
    #    print(ConsolColor.PreSetUpColoredTextLine(f"Failed to create output directory at: {Load_env_variable('OUT_PATH')}", "danger"))
    #    os.makedirs(f"{Load_env_variable('OUT_PATH')}")

    while True:
        _LoggingWaySelection()

        can_go = input(ConsolColor.PreSetUpColoredTextLine("Do you want to fech more data from the API? (yes | no)\n?.:", "s_color")).strip().lower()

        if can_go == "no":
            break

__all__ = ["main_process"]