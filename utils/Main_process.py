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