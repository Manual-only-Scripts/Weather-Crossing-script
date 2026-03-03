"""
Represents a simple calendar date with year, month, and day components.

The `Date` class provides a lightweight structure for storing and accessing
date information. It uses `__slots__` for memory efficiency and exposes
properties for controlled access to the year, month, and day fields. The class
is primarily used for constructing API query parameters and formatting dates
in a consistent way across the application.

Attributes
----------
year : int
    The calendar year.
month : int
    The calendar month (1–12).
day : int
    The day of the month.

Behavior
--------
- Stores date components as integers.
- Provides property getters and setters for each field.
- Formats itself as a string in `YYYY-M-M` format via `__str__`.

Example
-------
>>> d = Date(2026, 3, 15)
>>> str(d)
'2026-3-15'

Exports
-------
__all__ = ["Date"]
    Makes the Date class available for import.
"""


class Date:
    __slots__ = ["_year", "_month", "_day"]

    def __init__(self, year: int, month: int, day: int) -> None:
        self._year: int = year
        self._month: int = month
        self._day: int = day

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value: int):
        self._month = value

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value: int):
        self._day = value

    def __str__(self) -> str:
        return f"{self._year}-{self._month}-{self._day}"

__all__ = ["Date"]