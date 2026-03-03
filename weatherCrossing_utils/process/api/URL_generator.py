"""
Builds a complete weather‑API request URL using user‑provided parameters.

This module defines the `url_generator` function, which collects all required
inputs for a weather‑data API call—coordinates, start date, end date, unit
group, and selected weather parameters—and assembles them into a fully
formatted request URL. The function is wrapped with `timer` and `tryer`,
providing execution‑time measurement and structured error handling with
colored console messages.

Inputs
------
The function relies on interactive input functions to gather:
- Coordinates (longitude and latitude)
- Start date for the query
- End date for the query
- Unit group ("metric" or "imperial")
- Weather parameters to include in the API response

Each of these helper functions may return `None` if the user input is invalid.
The URL generator checks for this and raises a `WrongValueExeption` when any
required value is missing.

Function
--------
url_generator(...) -> str:
    Constructs a URL using:
    - Base API URL from environment variables
    - API key from environment variables
    - User‑provided coordinates and date range
    - Unit group selection
    - Comma‑separated list of weather parameters

    Returns:
        A fully assembled URL string ready for use in an API request.

Behavior
--------
- Validates that all required inputs are present.
- Uses environment variables `API_URL` and `API_KEY` to build the request.
- Joins selected weather parameters into a comma‑separated string.
- Returns the final URL or raises an exception if inputs are invalid.
- Uses decorators to provide timing information and user‑friendly error output.

Exports
-------
__all__ = ["url_generator"]
    Makes the URL generator available for import.

"""


from ..inputs.complex.Ask_Weather_Parameters import *
from ..env_loader.Load_ENV_variable import *
from ..inputs.simple.Ask_Coordinate import *
from ..inputs.simple.Ask_UnitGroup import *
from ..inputs.simple.Ask_Date import *
from ...exeptions.Exeptions import *
from ...classes.ConsolColor import *
from ..wrappers import *


@timer
@tryer
def url_generator(cordinates = ask_for_cordinate(), start_Date = ask_for_Date(), end_Date = ask_for_Date(), unit_group = ask_for_unitGroup(), weather_params = ask_for_weather_parameters()) -> str:
    
    parameters: list = [cordinates, start_Date, end_Date, unit_group, weather_params]
    for i in parameters:
        if i is None:
            WrongValueExeption("Wrong input type")

    weather_param: list[str] | str = weather_params if weather_params is not None else ""

    url: str = f"{Load_env_variable("API_URL")}{cordinates}/{start_Date}/{end_Date}?key={Load_env_variable("API_KEY")}&include=days&unitGroup={unit_group}&elements={','.join(weather_param)}"
    
    return url

__all__ = ["url_generator"]