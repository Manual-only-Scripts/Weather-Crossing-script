from ...exeptions.Exeptions import *
from ...classes.ConsolColor import *
from .URL_generator import *
from ..wrappers import *

import requests

@timer
@tryer
def fetch_api():
    url: str = url_generator()
    
    if url is None:
        WrongValueExeption("Wrong url content")

    print(ConsolColor.PreSetUpColoredTextLine(f"Asking the API for data.", "i_tips"))
    
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    return response.json()