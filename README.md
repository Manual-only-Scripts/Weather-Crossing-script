# Weather Crossing Script

A modular, console‑driven Python tool for fetching, validating, and logging weather data using the Visual Crossing Weather API. The project focuses on clean architecture, reusable components, strong input validation, and color‑coded console feedback for a smooth user experience.

---

## 🌦️ Overview

Weather Crossing Script is a command‑line application that guides the user through selecting coordinates, date ranges, unit systems, and weather parameters, then automatically builds a valid API request URL and fetches weather data. The script supports multiple output formats, environment‑based configuration, and structured error handling.

The project is built with:

- Python 3.12+
- Requests for API communication
- python‑dotenv for environment variable loading
- Colorama for colored console output
- Custom decorators for timing and error handling
- A modular folder structure for clarity and maintainability

---

## ✨ Features

- **Interactive input system**
  - Coordinates (longitude & latitude)
  - Date selection with calendar‑based validation
  - Unit group selection (metric / imperial)
  - Weather parameter selection (single, multiple, or all)

- **Automatic URL generation**
  - Uses environment variables (`API_URL`, `API_KEY`)
  - Ensures all inputs are valid before constructing the request

- **API request handling**
  - Fetches weather data from Visual Crossing
  - Validates HTTP response
  - Returns parsed JSON

- **Color‑coded console output**
  - Tips, warnings, errors, success messages
  - Fully customizable RGB or preset color themes

- **Modular architecture**
  - Easy to extend
  - Clear separation of concerns
  - Reusable utility classes

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/LemonShark20706/Weather-Crossing-script.git
cd Weather-Crossing-script
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a .env file in the project root:

```bash
API_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/
API_KEY=YOUR_API_KEY_HERE
OUT_PATH=./output/
```

## 🚀 Usage

Run the main script or any module that triggers the workflow:

```bash
python main.py
```

The program will guide you through:

- Entering coordinates
- Selecting start and end dates
- Choosing unit group
- Selecting weather parameters
- Generating the API URL
- Fetching and returning weather data

All steps include color‑coded feedback and validation.

## 🧩 Core Components

### Input System

Handles user input with validation and error handling.

### URL Generator

Builds a complete API request URL using validated inputs and environment variables.

### API Fetcher

Sends the request, checks the response, and returns JSON data.

### Logging System

Supports JSON output and is extendable for PDF or other formats.

### Decorators

- @timer — measures execution time
- @tryer — wraps functions in a safe error‑handling layer

## 🖌 Console Coloring

The ConsolColor class provides:

- Custom RGB coloring
- Predefined semantic color themes
- Start/end color wrappers

Used throughout the project for clarity and UX.

## 🛠 Planned Features

- PDF report generation
- CLI flags for non‑interactive mode
- Weather data visualization
- Async API calls
- Unit tests

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.
Feel free to open issues or submit pull requests.

## 📜 License

This project is released under the MIT License.
