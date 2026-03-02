from ....classes.ConsolColor import *
from ....exeptions.Exeptions import *
from ....classes.Date import *
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