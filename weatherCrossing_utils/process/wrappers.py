from ..classes.ConsolColor import *
from ..exeptions.Exeptions import *

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start: float = time.time()
        result = func(*args, **kwargs)
        end: float = time.time()
        print(f"Took {end-start:.8f} second\n\n")
        return result
    return wrapper

def tryer(func):
    def wrapper(*args, **kwargs):
        print(ConsolColor.PreSetUpColoredTextLine("Operation starting", "s_color"))
        try:
            resoult = func(*args, **kwargs)

        except Exception as e:
            print(ConsolColor.PreSetUpColoredTextLine(f"Invalid operation: {e}", "danger"))
            return None

        else:
            print(ConsolColor.PreSetUpColoredTextLine(f"Successful operation is done", "success"))
            return resoult

        finally:
            print(ConsolColor.PreSetUpColoredTextLine("Operation ended.", "info"))
            print("\n"*4)
    return wrapper

__all__ = ["timer", "tryer"]