class Coordinate:
    __slots__ = ["_x", "_y"]

    type coordinateType = int | float

    def __init__(self, longitude: coordinateType, latitude: coordinateType) -> None:
        self._x: Coordinate.coordinateType = longitude
        self._y: Coordinate.coordinateType = latitude

    @property
    def longitude(self) -> coordinateType:
        return self._x

    @longitude.setter
    def longitude(self, value: coordinateType):
        self._x = value

    @property
    def latitude(self) -> coordinateType:
        return self._y

    @latitude.setter
    def latitude(self, value: coordinateType):
        self._y = value

    def __str__(self) -> str:
        return f"{self._x},{self._y}"

__all__ = ["Coordinate"]