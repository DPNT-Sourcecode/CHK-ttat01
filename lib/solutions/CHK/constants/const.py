from lib.solutions.CHK.utils import Utils


class Constants:

    EXCLUDE: dict[str, int] = {"A": 50, "B": 30, "C": 20, "D": 15}

    ITEMS: dict[str, int] = Utils.generate_constants(
        keys="EFGHIJKLMNOPQRSTUVWXYZ", price_range=range(10, 2000), append=EXCLUDE
    )

