import sys
import os
from typing import TypeVar, Any

sys.path.append(os.path.abspath("."))

from utils import Utils
from constants import Constants
from frozendict import frozendict


class ImproperlyConfigured(Exception):
    pass


T = TypeVar("T", bound="Supermarket")


class Supermarket:

    def __init__(self, *args, **kwargs) -> None:
        kw_args = ["items", "offers"]

        for kw in kwargs:
            setattr(self, kw, frozendict(**kwargs.get(kw, {})))

        if not all(getattr(self, kw, None) for kw in kwargs):
            raise ImproperlyConfigured("Please pass all required keyword arguemnts")

    @classmethod
    def factory(cls: type) -> T:
        return cls(items=Constants.ITEMS, offers=Constants.OFFERS)


    def _validate_input(self, value: str, cls: Any) -> int:
        if not isinstance(value, cls):
            return -1
        return 0
        
    def _sanitize_input():
        ...
        
    

# entrypoint
def checkout(skus: str) -> int:
    raise NotImplementedError()


if "__main__" in __name__:
    # s = Supermarket.factory()
    # print(s.items)
    # print(s.offers)


