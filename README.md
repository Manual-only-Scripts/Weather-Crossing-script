# Weather Crossing Script

A modular, console-driven Python tool for fetching, validating, and logging weather data using the Visual Crossing Weather API. The project focuses on clean architecture, reusable components, strong input validation, and color-coded console feedback for a smooth user experience.

---

## 🌦️ Overview

Weather Crossing Script is a command-line application that guides the user through selecting coordinates, date ranges, unit systems, and weather parameters to automatically build a valid API request URL and fetch weather data. The script supports multiple output formats (JSON, CSV, XLSX, PDF), environment-based configuration, and structured error handling.

This project is built with:

-   Python 3.12+
-   Requests for API communication
-   python-dotenv for environment variable management
-   pandas for data handling (CSV/XLSX)
-   FPDF for PDF generation
-   Colorama for colored console output
-   Custom decorators for timing and error handling

---

## ✨ Features

-   **Interactive Input System**: Guides users through providing:
    -   Coordinates (longitude & latitude)
    -   Date ranges with calendar-based validation
    -   Unit group selection (metric / imperial)
    -   Weather parameter selection (single, multiple, or all)
-   **Automatic URL Generation**: Constructs a valid Visual Crossing Weather API request URL from user inputs and environment variables.
-   **API Request Handling**: Fetches weather data, validates the HTTP response, and parses the JSON payload.
-   **Multi-Format Logging**: Saves fetched data in various formats:
    -   JSON
    -   CSV
    -   XLSX
    -   PDF
-   **Color-Coded Console Output**: Provides clear, color-coded feedback for tips, warnings, errors, and success messages, improving the user experience.
-   **Modular Architecture**: Features a clear separation of concerns, making the codebase easy to read, maintain, and extend.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/manual-only-scripts/weather-crossing-script.git
cd weather-crossing-script
```

### 2. Create and activate a virtual environment

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root of the project and add your API credentials and output path:

```env
API_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/
API_KEY=YOUR_API_KEY_HERE
OUT_PATH=./output/
```

Replace `YOUR_API_KEY_HERE` with your actual Visual Crossing Weather API key.

---

## 🚀 Usage

To start the application, run the `main.py` script from your terminal:

```bash
python main.py
```

The program will then guide you through the following steps:
1.  Entering coordinates for the location.
2.  Selecting a start and end date for the weather history.
3.  Choosing a unit group (`metric` or `imperial`).
4.  Selecting the specific weather parameters you want to retrieve.
5.  Choosing the output format(s) for the data (JSON, PDF, CSV, XLSX).

The script validates each input, fetches the data, and saves the results to the directory specified by `OUT_PATH` in your `.env` file. After each successful operation, you will be asked if you want to fetch more data.

---

## 🧩 Core Components

### Input System (`weatherCrossing_utils/processes/inputs/`)

Handles all user input with comprehensive validation and clear error handling. It's divided into `simple` inputs (like dates and coordinates) and `complex` inputs (like multi-select parameter lists).

### URL Generator (`weatherCrossing_utils/processes/api/URL_generator.py`)

Assembles a complete and valid API request URL using the validated user inputs and environment variables (`API_URL`, `API_KEY`).

### API Fetcher (`weatherCrossing_utils/processes/api/FETCH_api.py`)

Sends the generated URL to the Visual Crossing API, checks the HTTP response for success, and returns the parsed JSON data.

### Logging System (`weatherCrossing_utils/processes/loggers/`)

Provides functionality to save the fetched data into various formats. Each format is handled by its own module:
-   `JSON_log_file.py`: Saves the raw JSON response.
-   `CSV_log_file.py`: Exports daily data to a CSV file.
-   `XLSX_log_file.py`: Exports daily data to an XLSX spreadsheet.
-   `PDF_log_file.py`: Generates a detailed PDF report with summary tables and daily breakdowns.

### Decorators (`weatherCrossing_utils/processes/wrappers.py`)

-   `@timer`: Measures and prints the execution time of a function.
-   `@tryer`: Wraps functions in a try-except block to provide robust error handling and user-friendly console messages for operations.

### Console Coloring (`weatherCrossing_utils/classes/ConsolColor.py`)

A utility class that provides static methods for applying color to console text. It uses predefined semantic color themes (e.g., success, warning, danger) to ensure consistent and clear communication with the user.

---

## 🤝 Contributing

Issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/manual-only-scripts/weather-crossing-script/issues).

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
