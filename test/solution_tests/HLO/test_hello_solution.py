import pytest
from lib.solutions.HLO.hello_solution import hello


def test_hello_fn():
    assert hello("arif") == "Hello, Arif"
    assert hello(1) == Exception
    assert hello("arif") != "Hello, World"

