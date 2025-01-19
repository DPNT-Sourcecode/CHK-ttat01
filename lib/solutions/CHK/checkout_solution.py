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

        for kw in kwargs:
            setattr(self, kw, kwargs.get(kw, {}))
            
        if not all(getattr(self, kw) for kw in kwargs)

    @classmethod
    def factory(cls: type) -> T:
        return cls(items=Constants.ITEMS, offers=Constants.OFFERS)


# noinspection PyUnusedLocal
# skus = unicode string


# entrypoint
def checkout(skus: str) -> int:
    raise NotImplementedError()


if "__main__" in __name__:
    ...
