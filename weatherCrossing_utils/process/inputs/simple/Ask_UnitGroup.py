"""
Provides a console‑based input prompt for selecting a weather data unit group.

This module defines the `ask_for_unitGroup` function, which interactively asks
the user to specify the desired unit system for weather‑related API queries.
The function is wrapped with the `tryer` decorator, adding structured error
handling and colored console messages for a more readable user experience.

Function
--------
ask_for_unitGroup() -> str:
    Prompts the user to enter either "metric" or "imperial" as the unit group.
    The input is normalized to lowercase and validated. If the user enters an
    invalid value, a ValueError is raised and handled by the decorator.

    Returns:
        A string representing the selected unit group ("metric" or "imperial").

Behavior
--------
- Displays a colored prompt asking for the unit group.
- Rejects any value other than "metric" or "imperial".
- Returns the validated unit group for use in API requests or configuration.

Exports
-------
__all__ = ["ask_for_unitGroup"]
    Makes the input function available for import from this module.

"""


from ....classes import *
from ...wrappers import *

@tryer
def ask_for_unitGroup() -> str:
    unit_group: str = input(ConsolColor.PreSetUpColoredTextLine("Enter the unit group (metric/imperial): ", "s_color")).strip().lower()

    if unit_group not in ["metric", "imperial"]:
        raise ValueError("Unit group must be metric or imperial.")
    
    return unit_group

__all__ = ["ask_for_unitGroup"]