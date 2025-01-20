from lib.solutions.CHK.utils import Utils
from collections import namedtuple


class Constants:

    Offer: type = namedtuple(
        "Offer",
        ["quantity", "discounted_price"],
    )

    Deal: type = namedtuple("Deal", ["quantity", "sku_for_free", "count_of_free_sku"])

    Group: type = namedtuple("Group", ["items", "count", "price"])

    EXCLUDE: dict[str, int] = {
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

    ITEMS: dict[str, int] = Utils.generate_constants(
        keys="GHIJKLMNOPQRSTUVWXYZ", price_range=range(10, 2000), append=EXCLUDE
    )

    OFFERS: dict[list[Offer]] = {
        "A": [Offer(3, 130), Offer(5, 200)],
        "B": [Offer(2, 45)],
        "H": [Offer(5, 45), Offer(10, 80)],
        "K": [Offer(2, 150)],
        "P": [Offer(5, 200)],
        "Q": [Offer(3, 80)],
        "V": [Offer(2, 90), Offer(3, 130)],
    }

    DEALS: dict[list[Deal]] = {
        "E": [Deal(quantity=2, sku_for_free="B", count_of_free_sku=1)],
        "F": [Deal(quantity=2, sku_for_free="F", count_of_free_sku=1)],
        "N": [Deal(quantity=3, sku_for_free="M", count_of_free_sku=1)],
        "R": [Deal(quantity=3, sku_for_free="Q", count_of_free_sku=1)],
        "U": [Deal(quantity=3, sku_for_free="U", count_of_free_sku=1)],
    }

    GROUP_ITEMS: tuple

