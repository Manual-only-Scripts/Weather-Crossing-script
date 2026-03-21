"""
Interactive console input for creating a Coordinate object.

This module provides the `ask_for_cordinate` function, which prompts the user to
enter a longitude and latitude value. The function converts the input into
floating‑point numbers and returns a `Coordinate` instance. It is wrapped with
the `tryer` decorator, ensuring that invalid input is handled gracefully with
colored console messages.

Function
--------
ask_for_cordinate() -> Coordinate:
    Prompts the user to enter longitude and latitude values. Both inputs are
    converted to floats. If the input cannot be converted or another error
    occurs, the `tryer` decorator handles the exception and prints a readable
    error message.

    Returns:
        A `Coordinate` object containing the provided longitude and latitude.

Behavior
--------
- Displays colored prompts for longitude and latitude.
- Converts user input to floating‑point numbers.
- Returns a validated `Coordinate` instance for use in API queries or other
    geospatial operations.

Exports
-------
__all__ = ["ask_for_cordinate"]
    Makes the coordinate‑input function available for import from this module.

"""


from ....classes import *
from ...wrappers import *
from ....exeptions import *

@spacing
@tryer
def ask_for_cordinate(project: Project) -> Coordinate | None:
    if not project.isGood:
        WrongValueExeption("The project is not good for process!")

    lon: float = float(input(ConsolColor.PreSetUpColoredTextLine("Enter longitude: ", "s_color")))
    lat: float = float(input(ConsolColor.PreSetUpColoredTextLine("Enter latitude: ", "s_color")))

    project.coordinate = Coordinate(lon, lat)

__all__ = ["ask_for_cordinate"]