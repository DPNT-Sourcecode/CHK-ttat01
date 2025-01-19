# noinspection PyShadowingBuiltins,PyUnusedLocal


class OutOfRange(Exception):
    pass


class SumInt:

    VALID_RANGE = range(0, 101)

    def __init__(self, *, x: int, y: int) -> None:

        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Please enter instance of int")

        if x not in self.VALID_RANGE or y not in self.VALID_RANGE:
            raise OutOfRange("Please insert integers in a range of 0-100")

        self._x: int = x
        self._y: int = y

    def calculate_self(self) -> int:
        return self._x + self._y


def compute(x: int, y: int) -> int:
    """entrypoint"""
    _sum: SumInt = SumInt(x=x, y=y)
    return _sum.calculate_self()


if "__main__" in __name__:
    print(compute(101, 12))
