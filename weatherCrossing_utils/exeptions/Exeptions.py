"""
Defines a simple wrapper for raising value‑related exceptions.

This module provides the `WrongValueExeption` function, a lightweight helper
used throughout the project to signal invalid or unacceptable input values.
Instead of returning error codes or messages, the function immediately raises
a `ValueError` with the provided message, ensuring consistent error handling
across input‑validation modules and workflow components.

Function
--------
WrongValueExeption(message: str) -> None:
    Raises a `ValueError` containing the supplied message. This function does
    not return and is intended to be used in situations where user input or
    computed values fall outside acceptable ranges.

Exports
-------
__all__ = ["WrongValueExeption"]
    Makes the exception helper available for import.

"""


def WrongValueExeption(message: str) -> None:
    raise ValueError(message)

__all__ = ["WrongValueExeption"]