from ...classes import *
from ..env_loader import *
from ..wrappers import *

import pandas as pd

@spacing
@timer
@tryer
def xlsx_log_file(project: Project):
    days = project.project_data['days']
    df = pd.DataFrame(days)

    out_path = f"{Load_env_variable('OUT_PATH')}{project.project_name}weather.xlsx"

    with pd.ExcelWriter(out_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name="Summary", index=False)

        for day in days:
            date = day["datetime"]
            day_df = pd.DataFrame([day])
            safe_name = date[:31]
            day_df.to_excel(writer, sheet_name=safe_name, index=False)

    return f"Excel file created at: {out_path}"
