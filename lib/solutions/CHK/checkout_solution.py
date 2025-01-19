import sys
import os
from typing import TypeVar, Any

sys.path.append(os.path.abspath("."))

from lib.solutions.CHK.utils import Utils
from lib.solutions.CHK.constants import Constants
from frozendict import frozendict


class ImproperlyConfigured(Exception):
    pass


T = TypeVar("T", bound="Supermarket")


class Supermarket:

    # for ide's type hint
    items: dict
    offers: dict
    deals: dict

    def __init__(self, *args, **kwargs) -> None:
        kw_args = ["items", "offers", "deals"]

        for kw in kwargs:
            setattr(self, kw, frozendict(**kwargs.get(kw, {})))

        if not all(getattr(self, kw, None) for kw in kwargs):
            raise ImproperlyConfigured("Please pass all required keyword arguemnts")

    @classmethod
    def factory(cls: type) -> T:
        return cls(
            items=Constants.ITEMS, offers=Constants.OFFERS, deals=Constants.DEALS
        )

    def validate_input(self, value: str, cls: Any) -> int:
        """
        validate for its type and if all basket items exist in the supermarket's databse
        """
        if not isinstance(value, cls) or not Utils.item_exists(value, self.items):
            return -1
        return 0

    def sanitize_input(self, string: str) -> str:
        """sanitize string input - uppercase + strip whitespaces"""
        return string.upper().strip()

    def count_items_in_basket(self, skus: str) -> dict[str, int]:
        """calculate how many items present in basket"""

        is_checked = []
        items_in_basket = {}

        for char in skus:
            if char not in is_checked:
                items_in_basket[char] = skus.count(char)
                is_checked.append(char)

        return items_in_basket

    def calc_price(self, basket: dict[str, int]) -> int:
        price = 0

        for sku, count in basket.items():

            # from high to small
            sorted_offers = sorted(
                self.offers.get(sku, []), key=lambda _: _[0], reverse=True
            )

            # minimum basket item required for an offer
            min_required_offer: int = min(
                self.offers.get(sku, []), key=lambda _: _[0], default=count + 1
            )

            if sku not in self.offers and count < min_required_offer:
                price += count * self.items.get(sku, 0)

            else:

                for c, value in sorted_offers:

                    if c > count:
                        continue

                    integer, count = divmod(count, c)
                    price += integer * value

                if count != 0:  # some items left for regular pricing
                    price += count * self.items.get(sku, 0)

        return price

    def detect_deals(self, skus: str) -> dict:
        dealed_items = filter(
            function=lambda sku: sku in self.deals, iterable=set(skus)
        )

        for sku in dealed_items:
            ...


# entrypoint
def checkout(skus: str) -> int:

    supermarket: Supermarket = Supermarket.factory()

    if supermarket.validate_input(value=skus, cls=str) == -1:
        return -1

    skus: str = supermarket.sanitize_input(string=skus)

    items_in_basket: dict[str, int] = supermarket.count_items_in_basket(skus=skus)

    final_price = supermarket.calc_price(basket=items_in_basket)

    return final_price


if "__main__" in __name__:
    p = checkout("a")  # empty basket
    print(p)




