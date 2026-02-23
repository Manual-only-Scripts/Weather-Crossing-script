from dotenv import load_dotenv
from colorama import Style
from fpdf import FPDF
import requests
import calendar
import time
import os

class ConsolColor:
    @staticmethod
    def CustomColoredText(text : str, r : int, g : int, b : int) -> str:
        """
        Colors a given text to a given RGB color

        Args:
            szoveg (`str`): The text that you want to color.
            r (`int`): RGB color red.
            g (`int`): RGB color green.
            b (`int`): RGB color blue.

        Returns:
            `str`: Gives back the colored text.
        """
    
        color : str = f"\x1b[38;2;{r};{g};{b}m"
        coloredText : str = f"{color}{text}{Style.RESET_ALL}"
        return coloredText

    @staticmethod
    def PreSetUpColoredTextLine(text : str, textType : str) -> str:
        """
        Gives back a line of colored text with pre coded colors.

        Args:
            text (str): The text you want to color.
            textType (str): The color type.

        Returns:
            str: The colored text.

        ## Types
            `ni_tips` -> `not_important_tips` -> Tips that can be overlooked. It is a black color rgb(0,0,0).
            `i_tips` -> `important_tips` -> Tips that can make this process faster.
            `s_color` -> `system_color` -> The basic color that this code use.
            `is_color` -> `important_system_color` -> The system color that you sould look out for.
            `p_error` -> `possible_error` -> This colored message can lead to errors.
            `warning` -> `warning` -> This colored message is a warning.
            `danger` -> `danger` -> This colored message is a danger.
            `success` -> `success` -> This color means that the task went good.
            `info` -> `information` -> This colored message is an information.
        """

        Color : str = ""
        match textType:
            case "ni_tips":
                Color = f"\x1b[38;2;0;0;0m"
            case "i_tips":
                Color = f"\x1b[38;2;150;150;150m"
            case "s_color":
                Color = f"\x1b[38;2;200;200;200m"
            case "is_color":
                Color = f"\x1b[38;2;255;255;255m"
            case "p_error":
                Color = f"\x1b[38;2;255;230;0m"
            case "warning":
                Color = f"\x1b[38;2;255;100;0m"
            case "danger":
                Color = f"\x1b[38;2;255;0;0m"
            case "success":
                Color = f"\x1b[38;2;0;255;0m"
            case "info":
                Color = f"\x1b[38;2;0;0;255m"

        coloredText : str = f"{Color}{text}{Style.RESET_ALL}"
        return coloredText

    @staticmethod
    def PreSetUpColorStart(textType : str) -> str:
        """
        Gives back the start of colored line.

        Args:
            text (str): The text you want to color.
            textType (str): The color type.

        Returns:
            str: The colored text.

        ## Types
            `ni_tips` -> `not_important_tips` -> Tips that can be overlooked. It is a black color rgb(0,0,0).
            `i_tips` -> `important_tips` -> Tips that can make this process faster.
            `s_color` -> `system_color` -> The basic color that this code use.
            `is_color` -> `important_system_color` -> The system color that you sould look out for.
            `p_error` -> `possible_error` -> This colored message can lead to errors.
            `warning` -> `warning` -> This colored message is a warning.
            `danger` -> `danger` -> This colored message is a danger.
            `info` -> `information` -> This colored message is an information.
        """
    
        Color: str = ""
        match textType:
            case "ni_tips":
                Color = f"\x1b[38;2;0;0;0m"
            case "i_tips":
                Color = f"\x1b[38;2;150;150;150m"
            case "s_color":
                Color = f"\x1b[38;2;200;200;200m"
            case "is_color":
                Color = f"\x1b[38;2;255;255;255m"
            case "p_error":
                Color = f"\x1b[38;2;255;230;0m"
            case "warning":
                Color = f"\x1b[38;2;255;100;0m"
            case "danger":
                Color = f"\x1b[38;2;255;0;0m"
            case "info":
                Color = f"\x1b[38;2;0;0;255m"

        finalColor : str = f"{Color}"
        return finalColor

    @staticmethod
    def PreSetUpColorEnd() -> str:
        """
        Gives back the end of colored line.

        Returns:
            str: The end of colored text.
        """
        finalColorEnd = f"{Style.RESET_ALL}"
        return finalColorEnd   

class coordinate:
    __slots__ = ["_x", "_y"]

    type coordinateType = int | float

    def __init__(self, longitude: coordinateType, latitude: coordinateType) -> None:
        self._x: coordinate.coordinateType = longitude
        self._y: coordinate.coordinateType = latitude

    @property
    def longitude(self) -> coordinateType:
        return self._x

    @longitude.setter
    def longitude(self, value: coordinateType):
        self._x = value

    @property
    def latitude(self) -> coordinateType:
        return self._y

    @latitude.setter
    def latitude(self, value: coordinateType):
        self._y = value

    def __str__(self) -> str:
        return f"{self._x},{self._y}"

class date:
    __slots__ = ["_year", "_month", "_day"]

    def __init__(self, year: int, month: int, day: int) -> None:
        self._year: int = year
        self._month: int = month
        self._day: int = day

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value: int):
        self._month = value

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value: int):
        self._day = value

    def __str__(self) -> str:
        return f"{self._year}-{self._month}-{self._day}"

def timer(func):
    def wrapper(*args, **kwargs):
        start: float = time.time()
        result = func(*args, **kwargs)
        end: float = time.time()
        print(f"Took {end-start:.8f} second\n\n")
        return result
    return wrapper

def try_tester(func):
    def wrapper(*args, **kwargs):
        print(ConsolColor.PreSetUpColoredTextLine("Operation starting", "s_color"))
        try:
            resoult = func(*args, **kwargs)

        except Exception as e:
            print(ConsolColor.PreSetUpColoredTextLine(f"Invalid operation: {e}", "danger"))
            return None

        else:
            print(ConsolColor.PreSetUpColoredTextLine(f"Successful operation is done", "success"))

            return resoult

        finally:
            print(ConsolColor.PreSetUpColoredTextLine("Operation ended.", "info"))
    return wrapper

@try_tester
def ask_for_cordinate() -> coordinate:
    lon: float = float(input(ConsolColor.PreSetUpColoredTextLine("Enter longitude: ", "s_color")))
    lat: float = float(input(ConsolColor.PreSetUpColoredTextLine("Enter latitude: ", "s_color")))

    return coordinate(lon, lat)

@try_tester
def ask_for_date() -> date:
    year: int = int(input(ConsolColor.PreSetUpColoredTextLine("Enter year (e.g., 2026): ", "s_color")))
    month: int = int(input(ConsolColor.PreSetUpColoredTextLine("Enter month (1-12): ", "s_color")))
    day: int = int(input(ConsolColor.PreSetUpColoredTextLine(f"Enter day (1-{calendar.monthrange(year, month)[1]}): ", "s_color")))

    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")

    if day < 1 or day > calendar.monthrange(year, month)[1]:
        raise ValueError(f"Day must be between 1 and {calendar.monthrange(year, month)[1]} for month {month}.")

    return date(year, month, day)

@try_tester
def ask_for_unitGroup() -> str:
    unit_group: str = input(ConsolColor.PreSetUpColoredTextLine("Enter the unit group (metric/imperial): ", "s_color")).strip().lower()

    if unit_group not in ["metric", "imperial"]:
        raise ValueError("Unit group must be metric or imperial.")
    
    return unit_group

def ask_for_weather_parameters() -> list[str] | None:
    option_list: list[str] = ["datetime","temp","tempmax","tempmin","dew","humidity","precip","windgust","windspeed","cloudcover","solarradiation","solarenergy","uvindex","visibility"]
    print(ConsolColor.PreSetUpColoredTextLine("What do you need from the list:", "s_color"))
    for optionIndex in range(len(option_list)):
        print(ConsolColor.PreSetUpColoredTextLine(f"\t{optionIndex+1})- {option_list[optionIndex]}", "s_color"))
    print(ConsolColor.PreSetUpColoredTextLine("Type the numbers of the options you need separated by commas (e.g., 1,3,5) or type all if you need all. If you want to leave press enter.:", "s_color"))
    
    try:
        user_input: str = input(ConsolColor.PreSetUpColoredTextLine("?.: ", "s_color")).strip().lower()

        if user_input.lower() == "all":
            print(ConsolColor.PreSetUpColoredTextLine(f"Weather parameters is selected. ({user_input})", "success"))
            return option_list
        
        if user_input == "":
            raise ValueError("Parameters is empty.")
    except ValueError as ve:
        print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
        return None

    else:
        try:
            selected_options: list[str] = []
            selected_indices: list[int] = [int(x.strip()) for x in user_input.split(",")]
            for index in selected_indices:
                if 1 <= index <= len(option_list):
                    selected_options.append(option_list[index - 1])
                else:
                    raise ValueError("Invalid input. Please enter valid option numbers separated by commas, 'all', or press enter to leave:")
        except ValueError as ve:
            print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
            return None
        
        else:
            print(ConsolColor.PreSetUpColoredTextLine(f"Successful Weather parameters selection. ({user_input})", "success"))
            return selected_options

    finally:
        print(ConsolColor.PreSetUpColoredTextLine("Weather parameters input attempt completed.", "info"))

def ask_for_logging_way() -> list[str] | None:
    option_list: list[str] = ["pdf","json"]
    print(ConsolColor.PreSetUpColoredTextLine("What do you need from the list for logging:", "s_color"))
    for optionIndex in range(len(option_list)):
        print(ConsolColor.PreSetUpColoredTextLine(f"\t{optionIndex+1})- {option_list[optionIndex]}", "s_color"))
    print(ConsolColor.PreSetUpColoredTextLine("Type the numbers of the options you need separated by commas (e.g., 1,3,5) or type all if you need all. If you want to leave press enter.:", "s_color"))
    
    try:
        user_input: str = input(ConsolColor.PreSetUpColoredTextLine("?.: ", "s_color")).strip().lower()

        if user_input.lower() == "all":
            print(ConsolColor.PreSetUpColoredTextLine(f"Logging parameters is selected. ({user_input})", "success"))
            return option_list
        
        if user_input == "":
            raise ValueError("Parameters is empty.")
    except ValueError as ve:
        print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
        return None

    else:
        try:
            selected_options: list[str] = []
            selected_indices: list[int] = [int(x.strip()) for x in user_input.split(",")]
            for index in selected_indices:
                if 1 <= index <= len(option_list):
                    selected_options.append(option_list[index - 1])
                else:
                    raise ValueError("Invalid input. Please enter valid option numbers separated by commas, 'all', or press enter to leave:")
        except ValueError as ve:
            print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
            return None
        
        else:
            print(ConsolColor.PreSetUpColoredTextLine(f"Successful Logging parameters selection. ({user_input})", "success"))
            return selected_options

    finally:
        print(ConsolColor.PreSetUpColoredTextLine("Logging parameters input attempt completed.", "info"))

@timer
@try_tester
def load_environment_file(file_path: str = ".env"):
    print(ConsolColor.PreSetUpColoredTextLine(f"Loading environment file: {file_path}", "i_tips"))

    load_dotenv(file_path)

@timer
@try_tester
def load_env_variable(variable_name: str) -> str | None:
    print(ConsolColor.PreSetUpColoredTextLine(f"Loading environment variables: {variable_name}", "i_tips"))
    env_variable: str = str(os.getenv(variable_name))

    return env_variable

@timer
@try_tester
def create_json_log_file(data):
    print(ConsolColor.PreSetUpColoredTextLine(f"Creating .json file for logging.", "i_tips"))

    with open(f"{load_env_variable('OUT_PATH')}weather_data_response.json", "w") as file:
        file.write(str(data).replace('\'', '"'))

@timer
@try_tester
def create_pdf_report_file(data: dict):
    fields = {
        'tempmax': 'Max Temperature',
        'tempmin': 'Min Temperature',
        'temp': 'Temperature',
        'dew': 'Dew Point',
        'humidity': 'Humidity',
        'precip': 'Precipitation',
        'windgust': 'Wind Gust',
        'windspeed': 'Wind Speed',
        'cloudcover': 'Cloud Cover',
        'visibility': 'Visibility',
        'solarradiation': 'Solar Radiation',
        'solarenergy': 'Solar Energy',
        'uvindex': 'UV Index'
    }

    units = {
        "tempmax": "°C",
        "tempmin": "°C",
        "temp": "°C",
        "dew": "°C",
        "humidity": "%",
        "precip": "mm",
        "windgust": "km/h",
        "windspeed": "km/h",
        "cloudcover": "%",
        "visibility": "km",
        "solarradiation": "W/m²",
        "solarenergy": "MJ/m²"
    }
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=5)
    
    pdf.add_page()
    pdf.set_font("Courier", "B", 16)
    pdf.cell(0, 10, "Weather Report Summary", ln=True, align='C')

    pdf.set_font("Courier", size=10)
    pdf.cell(0, 10, f"Query Cost: {data.get('queryCost', 'N/A')}", ln=True)

    days_data = data.get("days", [])
    pdf.cell(0, 10, f"Total Days: {len(days_data)}", ln=True)
    pdf.cell(0, 10, f"Location: {data.get('address', 'N/A').replace(',', ' | ')}", ln=True)
    pdf.cell(0, 10, f"Timezone: {data.get('timezone', 'N/A').replace('/', ' | ')}", ln=True)
    pdf.ln(10)

    pdf.set_font("Courier", "B", 16)
    pdf.cell(0, 10, "Dataset Summary:", ln=True)
    pdf.set_font("Courier", size=9)

    pdf.set_font("Courier", size=10)
    pdf.cell(0, 10, f"The following data table show the complete data set minimum, average and maximum values.", ln=True)


    col_widths = [60, 40, 40, 40]
    table_width = sum(col_widths)

    page_width = pdf.w
    left_margin = pdf.l_margin
    right_margin = pdf.r_margin
    usable_width = page_width - left_margin - right_margin

    table_x = left_margin + (usable_width - table_width) / 2

    pdf.ln(10)
    pdf.set_font("Courier", "B", 16)
    pdf.cell(0, 10, "Summary Table", ln=True, align="C")
    pdf.ln(3)

    pdf.set_font("Courier", "B", 10)
    pdf.set_x(table_x)
    pdf.cell(col_widths[0], 8, "", border=1)
    pdf.cell(col_widths[1], 8, "AVG", border=1, align='C')
    pdf.cell(col_widths[2], 8, "MAX", border=1, align='C')
    pdf.cell(col_widths[3], 8, "MIN", border=1, ln=True, align='C')

    pdf.set_font("Courier", size=10)

    for field, label in fields.items():
        values = [day.get(field, None) for day in days_data if day.get(field) is not None]

        if not values:
            continue

        avg_val = sum(values) / len(values)
        max_val = max(values)
        min_val = min(values)
        unit = units.get(field, "")

        pdf.set_x(table_x)
        if label == "UV Index":
            pdf.cell(col_widths[0], 8, f"{label}", border=1)
        else:
            pdf.cell(col_widths[0], 8, f"{label} ({unit})", border=1)
        pdf.cell(col_widths[1], 8, f"{avg_val:.2f}", border=1)
        pdf.cell(col_widths[2], 8, f"{max_val}", border=1)
        pdf.cell(col_widths[3], 8, f"{min_val}", border=1, ln=True)

    pdf.ln(10)

    pdf.set_font("Courier", size=10)
    pdf.cell(0, 10, f"For a more detailed information about the data set you can find after this page.", ln=True)
    pdf.cell(0, 10, f"All pages contains only one data entry from the set with a analysis.", ln=True)

    for day in days_data:
        pdf.add_page()

        pdf.set_font("Courier", "B", 16)
        pdf.cell(0, 10, f"Summary table for {day.get('datetime', 'N/A')}", ln=True, align="C")
        pdf.ln(3)

        col_widths = [60, 40, 30]
        table_width = sum(col_widths)

        page_width = pdf.w
        left_margin = pdf.l_margin
        right_margin = pdf.r_margin
        usable_width = page_width - left_margin - right_margin

        table_x = left_margin + (usable_width - table_width) / 2

        pdf.set_font("Courier", "B", 10)
        pdf.set_x(table_x)
        pdf.cell(col_widths[0], 8, "Data point", border=1, align='C')
        pdf.cell(col_widths[1], 8, "Value", border=1, align='C')
        pdf.cell(col_widths[2], 8, "Unit", border=1, ln=True, align='C')

        pdf.set_font("Courier", size=10)

        for key, value in day.items():
            if key == "datetime":
                continue

            label = fields.get(key) or key.capitalize()
            unit = units.get(key, "")
            
            pdf.set_x(table_x)

            pdf.cell(col_widths[0], 8, label, border=1)
            pdf.cell(col_widths[1], 8, str(value), border=1)
            pdf.cell(col_widths[2], 8, unit, border=1, ln=True)

        # --- Summary ---
        pdf.ln(10)
        pdf.set_font("Courier", "B", 14)
        pdf.cell(0, 10, "Analysis:", ln=True)
        pdf.set_font("Courier", size=10)
        pdf.cell(0, 10, "Not yet implemented", ln=True)

    pdf.output(f"{load_env_variable('OUT_PATH')}weather_report.pdf")
    print("PDF report created successfully as 'weather_report.pdf'.")

@timer
@try_tester
def api_url(cordinates = ask_for_cordinate(), start_date = ask_for_date(), end_date = ask_for_date(), unit_group = ask_for_unitGroup(), weather_params = ask_for_weather_parameters()) -> str:
    
    parameters: list = [cordinates, start_date, end_date, unit_group, weather_params]
    for i in parameters:
        if i is None:
            raise ValueError("Wrong input type")

    weather_param: list[str] | str = weather_params if weather_params is not None else ""

    url: str = f"{load_env_variable("API_URL")}{cordinates}/{start_date}/{end_date}?key={load_env_variable("API_KEY")}&include=days&unitGroup={unit_group}&elements={','.join(weather_param)}"
    
    return url

@timer
@try_tester
def fetch_api():
    url: str = api_url()
    
    if url is None:
        raise ValueError("Wrong url content")

    print(ConsolColor.PreSetUpColoredTextLine(f"Asking the API for data.", "i_tips"))
    
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    return response.json()

def main():
    load_environment_file()

    if os.path.exists(f"{load_env_variable('OUT_PATH')}") or os.makedirs(f"{load_env_variable('OUT_PATH')}"):
        print(ConsolColor.PreSetUpColoredTextLine(f"Output directory is ready at: {load_env_variable('OUT_PATH')}", "success"))
    
    #else:
    #    print(ConsolColor.PreSetUpColoredTextLine(f"Failed to create output directory at: {load_env_variable('OUT_PATH')}", "danger"))
    #    os.makedirs(f"{load_env_variable('OUT_PATH')}")

    while True:
        match ask_for_logging_way():
            case ["pdf"]:
                create_pdf_report_file(fetch_api())
            case ["json"]:
                create_json_log_file(fetch_api())
            case ["pdf", "json"]:
                data = fetch_api()
                create_pdf_report_file(data)
                create_json_log_file(data)
            case _:
                print(ConsolColor.PreSetUpColoredTextLine("No logging way is selected. No logging will be done.", "warning"))


        can_go = input(ConsolColor.PreSetUpColoredTextLine("Do you want to fech more data from the API? (yes | no)\n?.:", "s_color")).strip().lower()

        if can_go == "no":
            break

main()