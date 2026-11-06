"""A product that has a weight and requires shipping."""

import math

from can_be_shipped import CanBeShipped
from product import Product


class PhysicalProduct(Product, CanBeShipped):
    # One product superclass plus an interface-style ABC.
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        if (isinstance(weight, bool) or not isinstance(weight, (int, float))
                or not math.isfinite(weight) or weight < 0):
            raise ValueError("Weight must be a finite, non-negative number in kg.")
        self.__weight = float(weight)

    @property
    def weight(self) -> float:
        return self.__weight

    def calculate_shipping_cost(self) -> float:
        """Shipping costs $5 per kilogram, rounded to cents."""
        cost = self.__weight * 5.0
        if not math.isfinite(cost):
            raise ValueError("Weight is too large to calculate shipping.")
        return round(cost, 2)

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."

    def display_information(self) -> None:
        super().display_information()
        print(f"  Physical | Weight: {self.weight:g} kg | "
              f"Shipping: ${self.calculate_shipping_cost():.2f}")
        print(f"  {self.get_fulfilment_info()}")
