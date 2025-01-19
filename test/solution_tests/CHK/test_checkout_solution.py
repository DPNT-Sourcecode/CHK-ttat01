import pytest
from lib.solutions.CHK.checkout_solution import checkout


def test_checkout():
    assert checkout("") == 0  # empty basket
    assert checkout("AAABBB") == 205
    assert checkout(1111) == -1
    assert checkout("-10234885327") == -1

