from ...classes import *
from ..env_loader import *
from ..wrappers import *

import pandas as pd

# A 'days' lista DataFrame-mé alakítása
@timer
@tryer
def csv_log_file(project: Project):
    df = pd.DataFrame(project.project_data['days'])

    df.to_csv(f"{Load_env_variable('OUT_PATH')}weather.csv", index=False)

__all__ = ["csv_log_file"]