from lib.solutions.CHK.constants.const import Constants
import pytest


def test_constant_gerenator():
    assert type(Constants.ITEMS) == dict
