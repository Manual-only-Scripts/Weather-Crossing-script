from ....classes.ConsolColor import *
from ....exeptions.Exeptions import *

option_list: list[str] = ["Datetime","temp","tempmax","tempmin","dew","humidity","precip","windgust","windspeed","cloudcover","solarradiation","solarenergy","uvindex","visibility"]

def _listOptions():
    print(ConsolColor.PreSetUpColoredTextLine("What do you need from the list:", "s_color"))
    for optionIndex in range(len(option_list)):
        print(ConsolColor.PreSetUpColoredTextLine(f"\t{optionIndex+1})- {option_list[optionIndex]}", "s_color"))
    print(ConsolColor.PreSetUpColoredTextLine("Type the numbers of the options you need separated by commas (e.g., 1,3,5) or type all if you need all. If you want to leave press enter.:", "s_color"))

def _userInputIsEmpty(user_input: str)-> bool:
    return user_input == ""

def _userInputIsAll(user_input) -> bool:
    return user_input.lower() == "all"

def _returnAll() -> list[str]:
    return option_list


selected_options: list[str] = []

def _indexIsInRange(index) -> bool:
    return 1 <= index <= len(option_list)

def _returnFew(user_input) -> list[str]:
    selected_indices: list[int] = [int(x.strip()) for x in user_input.split(",") or user_input.split(";")]
    for index in selected_indices:
        if _indexIsInRange(index):
            selected_options.append(option_list[index - 1])
        else:
            raise ValueError("Invalid input. Please enter valid option numbers separated by commas, 'all', or press enter to leave:")
    
    return selected_options

def ask_for_weather_parameters() -> list[str] | None:
    _listOptions()

    try:
        user_input: str = input(ConsolColor.PreSetUpColoredTextLine("?.: ", "s_color")).strip().lower()

        if _userInputIsAll(user_input):
            print(ConsolColor.PreSetUpColoredTextLine(f"Weather parameters is selected. ({user_input})", "success"))
            return _returnAll()
        
        if _userInputIsEmpty(user_input):
            WrongValueExeption("Parameters is empty.")

    except ValueError as ve:
        print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
        return None

    else:
        try:
            _returnFew(user_input)

        except ValueError as ve:
            print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
            return None

        else:
            print(ConsolColor.PreSetUpColoredTextLine(f"Successful Weather parameters selection. ({user_input})", "success"))
            return selected_options

    finally:
        print(ConsolColor.PreSetUpColoredTextLine("Weather parameters input attempt completed.", "info"))

__all__ = ["ask_for_weather_parameters"]