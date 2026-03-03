"""
Represents a geographic coordinate defined by longitude and latitude.

The `Coordinate` class provides a lightweight structure for storing and
manipulating geographic coordinates. It uses `__slots__` for memory efficiency
and exposes property-based accessors for both longitude and latitude. The class
is primarily used for constructing API query parameters and formatting
coordinate values consistently across the application.

Attributes
----------
longitude : int | float
    The east–west position of the coordinate.
latitude : int | float
    The north–south position of the coordinate.

Behavior
--------
- Stores longitude and latitude as numeric values (int or float).
- Provides property getters and setters for controlled access.
- Formats itself as a string in `"longitude,latitude"` format via `__str__`.

Example
-------
>>> c = Coordinate(19.1234, 47.5678)
>>> str(c)
'19.1234,47.5678'

Exports
-------
__all__ = ["Coordinate"]
    Makes the Coordinate class available for import.
"""


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