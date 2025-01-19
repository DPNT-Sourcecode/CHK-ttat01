import sys

print(sys.path)

import pytest
from lib.solutions.HLO.hello_solution import hello


def test_hello_fn():
    assert hello("Arif") == "Hello, Arif!"

    with pytest.raises(Exception):
        hello(1)

    assert hello("Arif") != "Hello, World!"

