from typing import Optional


class Utils:

    @staticmethod
    def generate_constants(
        keys: str, price_range: range, append: Optional[dict] = None
    ) -> dict:
        """random sku key (character) - value (price) generator
        use append argument to apply pre-defined sku and its value"""
