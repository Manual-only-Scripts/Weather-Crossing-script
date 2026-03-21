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


from ..env_loader import *
from ...exeptions import *
from ...classes import *
from ..wrappers import *

@spacing
@timer
@tryer
def url_generator(project:Project) -> str | None:
    if not project.isGood:
        WrongValueExeption("The project is not good for process!")

    parameters: list = [project.coordinate, project.startDate, project.endDate, project.unitGroup, project.weatherParams]
    for i in parameters:
        if i is None:
            WrongValueExeption("Wrong input type")

    weather_param: list[str] | str = parameters[4] if parameters[4] is not None else ""

    url: str = f"{Load_env_variable("API_URL")}{parameters[0]}/{parameters[1]}/{parameters[2]}?key={Load_env_variable("API_KEY")}&include=days&unitGroup={parameters[3]}&elements={','.join(weather_param)}"
    project.url = url

__all__ = ["url_generator"]