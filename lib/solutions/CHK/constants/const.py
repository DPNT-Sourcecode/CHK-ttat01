from lib.solutions.CHK.utils import Utils


class Constants:

    ITEMS: dict[str, int] = Utils.generate_constants(
        keys="EFGHIJKLMNOPQRSTUVWXYZ", price_range=range(10, 2000),
        append=
    )
