from lib.solutions.CHK.utils.common import Utils
import pytest


def test_input_generator():
    out = Utils.generate_constants(
        keys="ABCDEFG", price_range=range(10, 1000), append={"A": 50, "B": 1453}
    )

    print(out)
