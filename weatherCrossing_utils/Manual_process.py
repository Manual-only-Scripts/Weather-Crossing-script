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


from .classes import *
from .processes import *

import questionary
import os

def _OutPutDirExists() -> bool:
    return os.path.exists(f"{Load_env_variable('OUT_PATH')}")

def _LoggingWaySelection(project: Project):
    match ask_for_log_file_extention():
            case "pdf":
                pdf_log_file(project)
            case "json":
                json_log_file(project)
            case "csv":
                csv_log_file(project)
            case "xlsx":
                xlsx_log_file(project)
            case ["pdf", "json", "csv", "xlsx"]:
                data = fetch_api(project)
                pdf_log_file(project)
                json_log_file(project)
                csv_log_file(project)
                xlsx_log_file(project)
            case _:
                print(ConsolColor.PreSetUpColoredTextLine("No logging way is selected. No logging will be done.", "warning"))

def main_manual_process():
    Load_env_file()

    if _OutPutDirExists():
        print(ConsolColor.PreSetUpColoredTextLine(f"Output directory is ready at: {Load_env_variable('OUT_PATH')}", "success"))
    
    else:
        print(ConsolColor.PreSetUpColoredTextLine(f"Failed to create output directory at: {Load_env_variable('OUT_PATH')}", "warning"))
        os.makedirs(f"{Load_env_variable('OUT_PATH')}")

    while True:
        project:Project = Project()

        ask_for_cordinate(project)
        project.startDate = ask_for_Date(project)
        project.endDate = ask_for_Date(project)
        ask_for_unitGroup(project)
        ask_for_weather_parameters(project)
        ask_for_project_name(project)

        url_generator(project)
        fetch_api(project)

        _LoggingWaySelection(project)

        can_go = questionary.select(
            "Do you want to fech more data from the API?:",
            choices=[
                "Yes",
                "No"
            ]
        ).ask().lower()

        if can_go == "no":
            break

        del project


__all__ = ["main_manual_process"]