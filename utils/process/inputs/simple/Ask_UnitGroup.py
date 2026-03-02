from ....classes.ConsolColor import *
from ...wrappers import *

@tryer
def ask_for_unitGroup() -> str:
    unit_group: str = input(ConsolColor.PreSetUpColoredTextLine("Enter the unit group (metric/imperial): ", "s_color")).strip().lower()

    if unit_group not in ["metric", "imperial"]:
        raise ValueError("Unit group must be metric or imperial.")
    
    return unit_group

__all__ = ["ask_for_unitGroup"]