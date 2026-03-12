"""
Generates a structured PDF weather report from API response data.

This module defines the `pdf_log_file` function, which transforms a weather API
response into a multi‑page PDF document. The report includes a high‑level
summary, aggregated statistics, and detailed per‑day tables. The function is
decorated with `timer` and `tryer`, providing execution‑time measurement and
safe error handling with colored console messages.

Function
--------
pdf_log_file(data: dict):
    Creates a PDF file named 'weather_report.pdf' in the directory specified by
    the OUT_PATH environment variable. The function expects a dictionary
    containing weather data in the structure returned by the API.

    The generated PDF includes:
    - A title page summarizing:
        - Query cost
        - Number of days in the dataset
        - Location and timezone
    - A dataset summary table showing average, maximum, and minimum values for
        key weather parameters such as temperature, humidity, wind speed, cloud
        cover, solar radiation, and more.
    - A dedicated page for each day in the dataset, containing:
        - A table of all available data points for that day
        - Units for each parameter
        - A placeholder section for future analytical commentary

    The function uses the FPDF library for layout and formatting, applying
    consistent fonts, column widths, and centered table positioning.

Behavior
--------
- If the dataset contains no values for a given field, that field is skipped.
- Units are automatically matched to each parameter.
- The output file is saved automatically, and a confirmation message is printed
    after successful creation.

Exports
-------
__all__ = ["pdf_log_file"]
    Makes the PDF generator available for import from this module.

"""


from ...classes import *
from ..env_loader import *
from ..wrappers import *

from fpdf import FPDF

@timer
@tryer
def pdf_log_file(project: Project):
    data = project.project_data
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
        pdf.cell(0, 10, f"Summary table for {day.get('Datetime', 'N/A')}", ln=True, align="C")
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
            if key == "Datetime":
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

    pdf.output(f"{Load_env_variable('OUT_PATH')}weather_report.pdf")
    print("PDF report created successfully as 'weather_report.pdf'.")

__all__ = ["pdf_log_file"]