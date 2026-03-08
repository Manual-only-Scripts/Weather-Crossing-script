"""
Package initializer for the application's utility layer. This module imports
and exposes commonly used classes, input handlers, environment loaders,
logging utilities, API helpers, and the main execution workflow so they become
readily available when the package is imported.

Loaded Components
-----------------
- Console utilities:
    Provides colored console output formatting for user interaction.

- Core data classes:
    Coordinate, Date, and other structured data types used throughout the
    application.

- Input handlers:
    Simple and complex input prompts for coordinates, dates, unit groups,
    logging extensions, and weather‑related parameters.

- Environment management:
    Functions for loading .env files and retrieving environment variables.

- Logging utilities:
    JSON and PDF log file generators for storing fetched API data.

- API helpers:
    URL generation and API‑fetching logic used to retrieve external data.

- Main process:
    The central workflow controller that coordinates environment setup,
    user interaction, API calls, and logging.

Behavior
--------
When this package is imported, all utilities become available and a console
message is printed indicating that the utility modules have been successfully
loaded.

"""

from .classes import *

from .process.wrappers import *

from .process.inputs import *

from .process.env_loader import *

from .process.loggers.JSON_log_file import *
from .process.loggers.PDF_log_file import *

from .process.api.URL_generator import *
from .process.api.FETCH_api import *

from .Main_process import *

print(ConsolColor.PreSetUpColoredTextLine(f"{'\n'*5}The utils have been loaded.{'\n'*5}".upper(), "success"))