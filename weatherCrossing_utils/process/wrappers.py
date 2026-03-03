"""
Utility decorators providing execution timing and safe‑execution wrappers.

The module defines two decorators—`timer` and `tryer`—that enhance functions
with additional runtime behavior. These decorators are intended to support
debugging, performance measurement, and user‑friendly error handling within
console‑based workflows.

Decorators
----------
timer(func):
    Measures how long the wrapped function takes to execute. After the function
    finishes, the elapsed time is printed in seconds with high precision.
    Returns the original function’s result unchanged.

tryer(func):
    Wraps the function call in a structured try/except/else/finally block.
    - Prints a colored “Operation starting” message before execution.
    - If the wrapped function raises an exception, a colored error message is
        displayed and `None` is returned.
    - If the function completes successfully, a colored success message is
        printed and the function’s return value is passed through.
    - Regardless of outcome, a colored “Operation ended” message is printed
        at the end.
    This decorator is useful for making console interactions more robust and
    readable, especially when user input or external operations may fail.

Exports
-------
__all__ = ["timer", "tryer"]
    Limits what is publicly exposed when importing the module with `from ... import *`.

"""


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