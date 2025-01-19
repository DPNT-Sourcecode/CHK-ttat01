import sys
import os
from typing import TypeVar

sys.path.append(os.path.abspath("."))

from utils import Utils
from constants import Constants


T = TypeVar("T", bound="Supermarket")


class Supermarket:

    def __init__(self, *args, **kwargs) -> None:
        kw_args = ["items", "offers"]

    @classmethod
    def factory(cls: type) -> T:
        return cls()


# noinspection PyUnusedLocal
# skus = unicode string


# entrypoint
def checkout(skus: str) -> int:
    raise NotImplementedError()


if "__main__" in __name__:
    ...





