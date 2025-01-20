from lib.solutions.CHK.utils import Utils
from collections import namedtuple


class Constants:

    Offer: type = namedtuple(
        "Offer",
        ["quantity", "discounted_price"],
    )

    Deal: type = namedtuple("Deal", ["quantity", "sku_for_free", "count_of_free_sku"])

    EXCLUDE: dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}

    ITEMS: dict[str, int] = Utils.generate_constants(
        keys="GHIJKLMNOPQRSTUVWXYZ", price_range=range(10, 2000), append=EXCLUDE
    )

    OFFERS: dict[list[Offer]] = {
        "A": [Offer(3, 130), Offer(5, 200)],
        "B": [Offer(2, 45)],
    }

    DEALS: dict[list[Deal]] = {
        "E": [Deal(quantity=2, sku_for_free="B", count_of_free_sku=1)],
        "F": [Deal(quantity=2, sku_for_free="F", count_of_free_sku=1)],
    }
