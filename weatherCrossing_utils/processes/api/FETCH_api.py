"""
Fetches weather data from the external API using a generated request URL.

This module provides the `fetch_api` function, which constructs a full API
request URL using the `url_generator` function and then performs an HTTP GET
request to retrieve weather data. The function is wrapped with `timer` and
`tryer`, adding execution‑time measurement and structured error handling with
colored console messages.

Function
--------
fetch_api() -> dict:
    Generates a complete API request URL, validates it, and sends an HTTP GET
    request using the `requests` library. If the response status code is not
    200, an exception is raised. When successful, the function returns the
    parsed JSON response as a Python dictionary.

Behavior
--------
- Calls `url_generator()` to assemble the request URL from user‑provided inputs.
- Validates that the generated URL is not None.
- Prints a colored message indicating that the API is being queried.
- Sends the request and checks the HTTP status code.
- Raises an exception if the API request fails.
- Returns the JSON response when successful.
- Uses decorators to provide timing information and user‑friendly error output.

Exports
-------
__all__ = ["fetch_api"]
    Makes the API‑fetching function available for import.

"""


from ...exeptions import *
from ...classes import *
from .URL_generator import *
from ..wrappers import *

import requests

@timer
@tryer
def fetch_api(project: Project):
    url = project.url

    if url is None:
        WrongValueExeption("Wrong url content")

    print(ConsolColor.PreSetUpColoredTextLine(f"Asking the API for data.", "i_tips"))
    
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    return response.json()

__all__ = ["fetch_api"]