from .classes.ConsolColor import *
from .classes.Coordinate import *
from .classes.Date import *

from .process.wrappers import *

from .process.inputs.simple.Ask_Coordinate import *
from .process.inputs.simple.Ask_Date import *
from .process.inputs.simple.Ask_UnitGroup import *

from .process.inputs.complex.Ask_Logging_Extention import *
from .process.inputs.complex.Ask_Weather_Parameters import *

from .process.env_loader.Load_ENV_file import *
from .process.env_loader.Load_ENV_variable import *

from .process.loggers.JSON_log_file import *
from .process.loggers.PDF_log_file import *

from .process.api.URL_generator import *
from .process.api.FETCH_api import *

from .Main_process import *

print(ConsolColor.PreSetUpColoredTextLine(f"{'\n'*5}The utils have been loaded.{'\n'*5}".upper(), "success"))