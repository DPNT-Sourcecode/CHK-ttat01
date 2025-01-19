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

    
    # for ide's type hint
    items: dict
    offers: dict
    
    def __init__(self, *args, **kwargs) -> None:
        kw_args = ["items", "offers"]

        for kw in kwargs:
            setattr(self, kw, frozendict(**kwargs.get(kw, {})))

        if not all(getattr(self, kw, None) for kw in kwargs):
            raise ImproperlyConfigured("Please pass all required keyword arguemnts")

    @classmethod
    def factory(cls: type) -> T:
        return cls(items=Constants.ITEMS, offers=Constants.OFFERS)


    def validate_input(self, value: str, cls: Any) -> int:
        if not isinstance(value, cls) or not Utils.item_exists(value, self.items):
            return -1
        return 0
        
    def sanitize_input(self, string: str):
        return string.upper().strip()
    
        
    

# entrypoint
def checkout(skus: str) -> int:
    
    supermarket: Supermarket = Supermarket.factory()
    
    skus: str = supermarket.sanitize_input()


if "__main__" in __name__:
    # s = Supermarket.factory()
    # print(s.items)
    # print(s.offers)



