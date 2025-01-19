from typing import Optional
from random import randint


class Utils:

    @staticmethod
    def generate_constants(
        keys: str, price_range: range, append: Optional[dict] = None
    ) -> dict:
        """random sku key (character) - value (price) generator
        use append argument to apply pre-defined sku and its value"""

        _start = 10
        _end = max(price_range)
        generated_map = {k: randint(_start, _end) for k in keys}

        # mutate with intercepted custom vals
        generated_map.update(append) if append else None

        return generated_map


if "__main__" in __name__:
    out = Utils.generate_constants(
        keys="ABCDEFG", price_range=range(10, 1000), append={"A": 50, "B": 1453}
    )
    print(out)
