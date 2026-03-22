from ....classes import *
from ...wrappers import *
from ....exeptions import *

import questionary

def project_name_is_needed() -> bool | None:
    name_needed: str = questionary.select(
            "You want a project name:",
            choices=[
                "Yes",
                "No"
            ]
        ).ask().lower()

    if name_needed not in ["yes", "no"]:
        raise ValueError("Unit group must be metric or imperial.")
    
    match name_needed:
        case "yes":
            return True
        case "no":
            return False

@spacing
@tryer
def ask_for_project_name(project: Project):
    if not project.isGood:
        WrongValueExeption("The project is not good for process!")

    match project_name_is_needed():
        case True:
            name: str = input("Please give the project a name: ")

            project.project_name = f"{name}_"
        case False:
            project.project_name = f"{project.coordinate}_{project.startDate}_{project.endDate}_".replace(',', '_').replace('-', '')
        case None:
            project.project_name = ""

__all__ = ["ask_for_project_name"]