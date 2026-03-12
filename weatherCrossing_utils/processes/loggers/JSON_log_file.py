"""
Creates a JSON log file from the provided API response data.

This module defines the `json_log_file` function, which saves raw weather API
response data into a JSON‑formatted file. The function is wrapped with the
`timer` and `tryer` decorators, adding execution‑time measurement and structured
error handling with colored console messages.

Function
--------
json_log_file(data):
    Writes the given data dictionary to a file named
    'weather_data_response.json' inside the directory specified by the
    OUT_PATH environment variable. The data is converted into a JSON‑like
    string by replacing single quotes with double quotes to ensure valid
    JSON formatting.

    The function prints a colored status message before writing the file and
    confirms successful execution through the decorators’ output.

Behavior
--------
- The output file is overwritten each time the function is called.
- The file is saved in the directory defined by the OUT_PATH environment
    variable.
- If an exception occurs during file creation or writing, the `tryer`
    decorator handles it and prints a colored error message.

Exports
-------
__all__ = ["json_log_file"]
    Makes the JSON logging function available for import from this module.

"""


from ...classes import *
from ..env_loader import *
from ..wrappers import *

@timer
@tryer
def json_log_file(project: Project):
    print(ConsolColor.PreSetUpColoredTextLine(f"Creating .json file for logging.", "i_tips"))

    with open(f"{Load_env_variable('OUT_PATH')}weather_data_response.json", "w") as file:
        file.write(str(project.project_data).replace('\'', '"'))

__all__ = ["json_log_file"]