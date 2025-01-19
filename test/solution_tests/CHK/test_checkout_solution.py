import pytest
from lib.solutions.CHK.checkout_solution import checkout


def test_checkout():
    assert checkout("") == 0
