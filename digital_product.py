"""A product delivered digitally, without physical shipping."""

import math

from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, download_size: float):
        super().__init__(product_id, name, price, stock)
        if (isinstance(download_size, bool)
                or not isinstance(download_size, (int, float))
                or not math.isfinite(download_size) or download_size < 0):
            raise ValueError("Download size must be a finite, non-negative number in MB.")
        self.__download_size = float(download_size)

    @property
    def download_size(self) -> float:
        return self.__download_size

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally through a download."

    def display_information(self) -> None:
        super().display_information()
        print(f"  Digital | Download size: {self.download_size:g} MB")
        print(f"  {self.get_fulfilment_info()}")
