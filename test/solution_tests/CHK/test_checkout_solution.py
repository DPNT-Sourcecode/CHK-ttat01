import pytest
from lib.solutions.CHK.checkout_solution import checkout


def test_checkout():
    assert checkout("") == 0  # empty basket
    assert checkout("AAABBB") == 205
    assert checkout(1111) == -1
    assert checkout("-10234885327") == -1
    assert checkout("EEAAABBB") == 255  # 80 + 150 + 60
    assert checkout("AAAAA") == 200
    assert checkout("FFF") == 20
    assert checkout("STXW") == 65
