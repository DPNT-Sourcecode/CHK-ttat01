from lib.solutions.CHK.utils import Utils
from collections import namedtuple


class Constants:

    EXCLUDE: dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15}

    ITEMS: dict[str, int] = Utils.generate_constants(
        keys="EFGHIJKLMNOPQRSTUVWXYZ", price_range=range(10, 2000), append=EXCLUDE
    )

    Offer: type = namedtuple(
        "Offer",
        ["quantity", "discounted_price"],
    )

    OFFERS: dict[list[Offer]] = {
        "A": [Offer(3, 130)],
        "B": [Offer(2, 45)],
        "E": [
            Offer(3, (ITEMS.get("E", 0) * 0.8) * 3),
            Offer(5, (ITEMS.get("E", 0) * 0.5) * 5),
        ],
    }







