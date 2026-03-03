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