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

        return {k: randint(_start, _end) for k in keys}.update(append)

