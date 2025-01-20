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
        kw_args = ["items", "offers", "deals", "group"]

        for kw in kwargs:
            setattr(self, kw, frozendict(**kwargs.get(kw, {})))

        if not all(getattr(self, kw, None) for kw in kwargs):
            raise ImproperlyConfigured("Please pass all required keyword arguemnts")

    @classmethod
    def factory(cls: type) -> T:
        return cls(
            items=Constants.ITEMS,
            offers=Constants.OFFERS,
            deals=Constants.DEALS,
            group=Constants.GROUP_ITEMS,
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

    def detect_deals(self, items_in_basket: dict) -> dict:
        """function detecting deals"""
        to_reduce: dict = {}

        for sku, deals in self.deals.items():

            if sku not in items_in_basket:
                continue

            items_count_in_basket = items_in_basket.get(sku, 0)

            for deal in deals:
                if sku == deal.sku_for_free:
                    to_reduce[sku] = (
                        items_count_in_basket
                        // (deal.quantity + deal.count_of_free_sku)
                    ) * deal.count_of_free_sku

                else:

                    to_reduce[deal.sku_for_free] = (
                        items_count_in_basket // deal.quantity
                    ) * deal.count_of_free_sku
        return to_reduce

    def group_discount(self, items_in_basket: dict) -> int:
        total = 0
        ...
        return total


# entrypoint
def checkout(skus: str) -> int:

    supermarket: Supermarket = Supermarket.factory()

    if supermarket.validate_input(value=skus, cls=str) == -1:
        return -1

    skus: str = supermarket.sanitize_input(string=skus)

    items_in_basket: dict[str, int] = supermarket.count_items_in_basket(skus=skus)

    final_price = supermarket.calc_price(basket=items_in_basket)

    to_reduce = supermarket.detect_deals(items_in_basket=items_in_basket)

    items_in_basket: dict[str, int] = supermarket.count_items_in_basket(
        skus="".join(
            [
                k * v
                for k, v in {
                    k: v - to_reduce.get(k, 0) for k, v in items_in_basket.items()
                }.items()
            ]
        )
    )

    final_price = supermarket.calc_price(basket=items_in_basket)

    return final_price


if "__main__" in __name__:
    # p = checkout("a")  # empty basket
    # print(p)

    string = """
    A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |            """

    for i in string.split():
        if len(str(i)) < 2 and 64 < ord(str(i)) < 91:
            print('"', end="")
            print(i, end="")
            print('"', end=": ")

        if len(str(i)) <= 2 and str(i).isdigit() and int(i) < 100:
            print(str(i), end=", ")
        {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
            "F": 10,
            "G": 20,
            "H": 10,
            "I": 35,
            "J": 60,
            "K": 80,
            "L": 90,
            "M": 15,
            "N": 40,
            "O": 10,
            "P": 50,
            "Q": 30,
            "R": 50,
            "S": 30,
            "T": 20,
            "U": 40,
            "V": 50,
            "W": 20,
            "X": 90,
            "Y": 10,
            "Z": 50,
        }

