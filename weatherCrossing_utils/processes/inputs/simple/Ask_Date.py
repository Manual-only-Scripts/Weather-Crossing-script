"""
Provides console‑based input and validation for creating a Date object.

This module defines the `ask_for_Date` function, which interactively prompts the
user to enter a valid year, month, and day. The function validates the input
against real calendar constraints and returns a `Date` instance. It is wrapped
with the `tryer` decorator, adding structured error handling and colored console
messages for a clearer user experience.

Helper Functions
----------------
_monthIsInRange(month: int) -> bool:
    Checks whether the given month falls outside the valid range of 1–12.
    Returns True if the month is invalid.

_dayIsInRange(year: int, month: int, day: int) -> bool:
    Checks whether the given day is outside the valid range for the specified
    year and month, using Python’s `calendar.monthrange` for accuracy.
    Returns True if the day is invalid.

Function
--------
ask_for_Date() -> Date:
    Prompts the user to enter a year, month, and day. Each value is converted
    to an integer and validated. If the month or day is invalid, a
    WrongValueExeption is raised and handled by the decorator.

    Returns:
        A `Date` object constructed from the validated year, month, and day.

Behavior
--------
- Displays colored prompts for each input field.
- Ensures the month is between 1 and 12.
- Ensures the day is valid for the given month and year.
- Uses the `tryer` decorator to handle invalid input gracefully and provide
    user‑friendly console feedback.

Exports
-------
__all__ = ["ask_for_Date"]
    Makes the date‑input function available for import from this module.

"""


from ....classes import *
from ....exeptions import *
from ....classes import *
from ...wrappers import *

import calendar

def _monthIsInRange(month: int) -> bool:
    return month < 1 or month > 12

def _dayIsInRange(year: int, month: int, day: int) -> bool:
    return day < 1 or day > calendar.monthrange(year, month)[1]

@tryer
def ask_for_Date() -> Date:
    year: int = int(input(ConsolColor.PreSetUpColoredTextLine("Enter year (e.g., 2026): ", "s_color")))
    month: int = int(input(ConsolColor.PreSetUpColoredTextLine("Enter month (1-12): ", "s_color")))
    day: int = int(input(ConsolColor.PreSetUpColoredTextLine(f"Enter day (1-{calendar.monthrange(year, month)[1]}): ", "s_color")))

    if _monthIsInRange(month):
        WrongValueExeption("Month must be between 1 and 12.")

    if _dayIsInRange(year, month, day):
        WrongValueExeption(f"Day must be between 1 and {calendar.monthrange(year, month)[1]} for month {month}.")

    return Date(year, month, day)

__all__ = ["ask_for_Date"]