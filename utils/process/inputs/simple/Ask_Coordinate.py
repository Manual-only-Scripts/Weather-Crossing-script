from ....classes.ConsolColor import *
from ....classes.Coordinate import *
from ...wrappers import *

@tryer
def ask_for_cordinate() -> Coordinate:
    lon: float = float(input(ConsolColor.PreSetUpColoredTextLine("Enter longitude: ", "s_color")))
    lat: float = float(input(ConsolColor.PreSetUpColoredTextLine("Enter latitude: ", "s_color")))

    return Coordinate(lon, lat)

__all__ = ["ask_for_cordinate"]