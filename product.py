# A product manages its own information and stock 

import math
from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        if not isinstance(product_id, str) or not product_id.strip():
            raise ValueError("Product ID cannot be empty.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise ValueError("Price must be a number.")
        if not math.isfinite(price) or price < 0:
            raise ValueError("Price must be a finite, non-negative number.")
        self.__product_id = product_id.strip().upper()
        self.__name = name.strip()
        self.__price = float(price)
        self.update_stock(stock)

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity: int) -> None:
        """Replace the current stock with the supplied quantity."""
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")
        self.__stock = quantity

    def display_information(self) -> None:
        print(f"{self.__product_id:<12} {self.__name:<25} "
              f"${self.__price:>10.2f} {self.__stock:>8}")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
