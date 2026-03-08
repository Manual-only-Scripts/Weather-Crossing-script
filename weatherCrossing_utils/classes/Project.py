from ..classes import *

class Project:
    __slots__ = ["_coordinates", "_startDate", "_endDate", "_isGood", "_loggingFile", "_unitGroup"]

    def __init__(self, good: bool = True):
        self._isGood: bool = good
        self._coordinates: Coordinate
        self._startDate: Date
        self._endDate: Date
        self._loggingFile: str
        self._unitGroup: str
        self._weatherParams: str

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
        return self._startDate

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
    def loggingFile(self) -> str:
        return self._loggingFile

    @loggingFile.setter
    def loggingDile(self, value: str):
        self._loggingFile = value

    @property
    def unitGroup(self) -> str:
        return self._unitGroup

    @unitGroup.setter
    def unitGroup(self, value: str):
        self._unitGroup = value

    @property
    def weatherParams(self):
        return self._weatherParams

__all__ = ["Project"]