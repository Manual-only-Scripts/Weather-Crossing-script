"""
Interactive console selection of weather‑data parameters.

This module provides the `ask_for_weather_parameters` function, which displays a
list of available weather fields and allows the user to select specific
parameters by entering their corresponding numbers, a comma‑separated list, or
the keyword "all". The function validates the input and returns a list of
selected parameter names. It uses colored console output for clarity and raises
errors when the input is invalid.

Helper Functions
----------------
_listOptions():
    Prints the full list of available weather parameters with numbered indices
    and instructions for how to select them.

_userInputIsEmpty(user_input: str) -> bool:
    Returns True if the user submitted an empty string.

_userInputIsAll(user_input: str) -> bool:
    Returns True if the user typed "all", indicating that all parameters should
    be selected.

_returnAll() -> list[str]:
    Returns the complete list of available weather parameters.

_indexIsInRange(index: int) -> bool:
    Checks whether a numeric index corresponds to a valid parameter in the list.

_returnFew(user_input: str) -> list[str]:
    Parses a comma‑ or semicolon‑separated list of numbers, validates each
    index, and returns the corresponding parameter names. Raises ValueError if
    any index is invalid.

Main Function
-------------
ask_for_weather_parameters() -> list[str] | None:
    Displays the parameter list and prompts the user for input. The function
    supports three input modes:
    - "all": selects every available parameter.
    - empty input: treated as invalid and triggers an error.
    - comma‑ or semicolon‑separated numbers: selects specific parameters.

    Returns:
        A list of selected parameter names, or None if the input was invalid.

Behavior
--------
- Uses colored console messages for prompts, errors, and success feedback.
- Validates user input thoroughly before returning results.
- Ensures that only valid parameter indices are accepted.
- Prints a completion message regardless of success or failure.

Exports
-------
__all__ = ["ask_for_weather_parameters"]
    Makes the parameter‑selection function available for import.

"""


from ....classes import *
from ....exeptions.Exeptions import *

option_list: list[str] = ["Datetime","temp","tempmax","tempmin","dew","humidity","precip","windgust","windspeed","cloudcover","solarradiation","solarenergy","uvindex","visibility"]

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

def ask_for_weather_parameters() -> list[str] | None:
    _listOptions()

    try:
        user_input: str = input(ConsolColor.PreSetUpColoredTextLine("?.: ", "s_color")).strip().lower()

        if _userInputIsAll(user_input):
            print(ConsolColor.PreSetUpColoredTextLine(f"Weather parameters is selected. ({user_input})", "success"))
            return _returnAll()
        
        if _userInputIsEmpty(user_input):
            WrongValueExeption("Parameters is empty.")

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
            print(ConsolColor.PreSetUpColoredTextLine(f"Successful Weather parameters selection. ({user_input})", "success"))
            return selected_options

    finally:
        print(ConsolColor.PreSetUpColoredTextLine("Weather parameters input attempt completed.", "info"))

__all__ = ["ask_for_weather_parameters"]