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

from datetime import datetime
import calendar
import questionary

def _select_year() -> int:
    year: str = questionary.select(
            "Choose a year:",
            choices=[f"{datetime.now().year - i}" for i in range(4)]
        ).ask().lower()
    
    return int(year)

def _select_month() -> int:
    month: str = questionary.select(
            "Choose a month:",
            choices= [f"{i}" for i in range(1,13)]
        ).ask().lower()
    
    return int(month)

def _select_day(year: int, month: int) -> int:
    day: str = questionary.select(
            "Choose a day:",
            choices= [f"{i}" for i in range(1,calendar.monthrange(year, month)[1]+1)]
        ).ask().lower()
    
    return int(day)

def _monthIsInRange(month: int) -> bool:
    return month < 1 or month > 12

def _dayIsInRange(year: int, month: int, day: int) -> bool:
    return day < 1 or day > calendar.monthrange(year, month)[1]

@spacing
@tryer
def ask_for_Date(project: Project) -> Date:
    if not project.isGood:
        WrongValueExeption("The project is not good for process!")

    year: int = _select_year()
    month: int = _select_month()
    day: int = _select_day(year, month)

    if _monthIsInRange(month):
        WrongValueExeption("Month must be between 1 and 12.")

    if _dayIsInRange(year, month, day):
        WrongValueExeption(f"Day must be between 1 and {calendar.monthrange(year, month)[1]} for month {month}.")

    return Date(year, month, day)

__all__ = ["ask_for_Date"]