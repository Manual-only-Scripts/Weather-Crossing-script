from ...classes.ConsolColor import *
from ..env_loader.Load_ENV_variable import *
from ..wrappers import *

@timer
@tryer
def json_log_file(data):
    print(ConsolColor.PreSetUpColoredTextLine(f"Creating .json file for logging.", "i_tips"))

    with open(f"{Load_env_variable('OUT_PATH')}weather_data_response.json", "w") as file:
        file.write(str(data).replace('\'', '"'))

__all__ = ["json_log_file"]