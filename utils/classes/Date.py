class Date:
    __slots__ = ["_year", "_month", "_day"]

    def __init__(self, year: int, month: int, day: int) -> None:
        self._year: int = year
        self._month: int = month
        self._day: int = day

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value: int):
        self._month = value

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value: int):
        self._day = value

    def __str__(self) -> str:
        return f"{self._year}-{self._month}-{self._day}"

__all__ = ["Date"]