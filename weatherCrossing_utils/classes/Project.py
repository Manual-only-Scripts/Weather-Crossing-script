from ..classes import Coordinate, Date

class Project:
    __slots__ = ["_coordinates", "_startDate", "_endDate", "_isGood", "_unitGroup", "_weatherParams", "_url", "_data"]

    def __init__(self, good: bool = True):
        self._isGood: bool = good
        self._coordinates: Coordinate
        self._startDate: Date
        self._endDate: Date
        self._unitGroup: str
        self._weatherParams: list

        self._url: str

        self.data: dict

    #region
    @property
    def coordinate(self) -> Coordinate:
        return self._coordinates

    @coordinate.setter
    def coordinate(self, values: Coordinate):
        self._coordinates = values

    @property
    def startDate(self) -> Date:
        return self._startDate

    @startDate.setter
    def startDate(self, value: Date):
        self._startDate = value

    @property
    def endDate(self) -> Date:
        return self._endDate

    @endDate.setter
    def endDate(self, value: Date):
        self._endDate = value

    @property
    def isGood(self) -> bool:
        return self._isGood

    @isGood.setter
    def isGood(self, value: bool):
        self._isGood = value

    def isGoodSwitch(self):
        self._isGood = not self._isGood

    @property
    def unitGroup(self) -> str:
        return self._unitGroup

    @unitGroup.setter
    def unitGroup(self, value: str):
        self._unitGroup = value

    @property
    def weatherParams(self):
        return self._weatherParams

    @weatherParams.setter
    def weatherParams(self, value: list):
        self._weatherParams = value

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str):
        self._url = value
    
    @property
    def project_data(self) -> dict:
        return self._data

    @project_data.setter
    def project_data(self, value: dict):
        self._data = value
    #endregion

    def __repr__(self) -> str:
        return f"Project.:\n\t-{self._isGood}\n\t-{self._coordinates}\n\t-{self._startDate}\n\t-{self._endDate}\n\t-{self._unitGroup}\n\t-{self._weatherParams}\n\t-{self._url}\n\t-{self._data}"#\n\t-{self.}

__all__ = ["Project"]