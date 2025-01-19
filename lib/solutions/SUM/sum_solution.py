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

        self.x: int = x
        self.y: int = y


def compute(x, y):
    valid_rage = range(0, 101)

    if x not in valid_rage or y not in valid_rage:
        raise ...


