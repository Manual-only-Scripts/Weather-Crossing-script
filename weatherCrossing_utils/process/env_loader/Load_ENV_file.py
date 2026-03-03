from ...classes.ConsolColor import *
from ..wrappers import *

from dotenv import load_dotenv

@timer
@tryer
def Load_env_file(file_path: str = ".env"):
    print(ConsolColor.PreSetUpColoredTextLine(f"Loading environment file: {file_path}", "i_tips"))

    load_dotenv(file_path)


__all__ = ["Load_env_file"]