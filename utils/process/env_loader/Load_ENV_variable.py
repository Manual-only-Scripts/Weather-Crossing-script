from ...classes.ConsolColor import *
from ..wrappers import *

import os

@timer
@tryer
def Load_env_variable(variable_name: str) -> str | None:
    print(ConsolColor.PreSetUpColoredTextLine(f"Loading environment variables: {variable_name}", "i_tips"))
    env_variable: str = str(os.getenv(variable_name))

    return env_variable

__all__ = ["Load_env_variable"]