"""
Interactive console selection of logging file extensions.

This module provides the `ask_for_log_file_extention` function, which displays a
list of available logging formats (PDF and JSON) and allows the user to select
one or both. The user may enter the keyword "all", a comma‑separated list of
indices, or press Enter to leave the selection empty. Input is validated and
appropriate feedback is shown using colored console messages.

Helper Functions
----------------
_listOptions():
    Prints the list of available logging extensions with numbered indices and
    instructions for how to select them.

_userInputIsEmpty(user_input: str) -> bool:
    Returns True if the user submitted an empty string.

_userInputIsAll(user_input: str) -> bool:
    Returns True if the user typed "all", indicating that all extensions should
    be selected.

_returnAll() -> list[str]:
    Returns the complete list of available logging extensions.

_indexIsInRange(index: int) -> bool:
    Checks whether a numeric index corresponds to a valid extension in the list.

_returnFew(user_input: str) -> list[str]:
    Parses a comma‑ or semicolon‑separated list of numbers, validates each
    index, and returns the corresponding extensions. Raises ValueError if any
    index is invalid.

Main Function
-------------
ask_for_log_file_extention() -> list[str] | None:
    Displays the extension list and prompts the user for input. The function
    supports three input modes:
    - "all": selects every available logging extension.
    - empty input: treated as invalid and triggers an error.
    - comma‑ or semicolon‑separated numbers: selects specific extensions.

    Returns:
        A list of selected logging extensions, or None if the input was invalid.

Behavior
--------
- Uses colored console messages for prompts, errors, and success feedback.
- Validates user input thoroughly before returning results.
- Ensures that only valid extension indices are accepted.
- Prints a completion message regardless of success or failure.

Exports
-------
__all__ = ["ask_for_log_file_extention"]
    Makes the logging‑extension selection function available for import.

"""


from ....classes import *
from ....exeptions import *

option_list: list[str] = ["pdf","json"]

def _listOptions():
    print(ConsolColor.PreSetUpColoredTextLine("What do you need from the list:", "s_color"))
    for optionIndex in range(len(option_list)):
        print(ConsolColor.PreSetUpColoredTextLine(f"\t{optionIndex+1})- {option_list[optionIndex]}", "s_color"))
    print(ConsolColor.PreSetUpColoredTextLine("Type the numbers of the options you need separated by commas (e.g., 1,3,5) or type all if you need all. If you want to leave press enter.:", "s_color"))

def _userInputIsEmpty(user_input: str)-> bool:
    return user_input == ""

def _userInputIsAll(user_input) -> bool:
    return user_input.lower() == "all"

def _returnAll() -> list[str]:
    return option_list


selected_options: list[str] = []

def _indexIsInRange(index) -> bool:
    return 1 <= index <= len(option_list)

def _returnFew(user_input) -> list[str]:
    selected_indices: list[int] = [int(x.strip()) for x in user_input.split(",") or user_input.split(";")]
    for index in selected_indices:
        if _indexIsInRange(index):
            selected_options.append(option_list[index - 1])
        else:
            raise ValueError("Invalid input. Please enter valid option numbers separated by commas, 'all', or press enter to leave:")
    
    return selected_options

def ask_for_log_file_extention() -> list[str] | None:
    _listOptions()

    try:
        user_input: str = input(ConsolColor.PreSetUpColoredTextLine("?.: ", "s_color")).strip().lower()

        if _userInputIsAll(user_input):
            print(ConsolColor.PreSetUpColoredTextLine(f"Logging extention is selected. ({user_input})", "success"))
            return _returnAll()
        
        if _userInputIsEmpty(user_input):
            WrongValueExeption("Extention is empty.")

    except ValueError as ve:
        print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
        return None

    else:
        try:
            _returnFew(user_input)

        except ValueError as ve:
            print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
            return None

        else:
            print(ConsolColor.PreSetUpColoredTextLine(f"Successful Logging extention selection. ({user_input})", "success"))
            return selected_options

    finally:
        print(ConsolColor.PreSetUpColoredTextLine("Logging extention input attempt completed.", "info"))

__all__ = ["ask_for_log_file_extention"]