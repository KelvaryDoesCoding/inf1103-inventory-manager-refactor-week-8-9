# Convert between saved JSON records and inventory objects

import json
from pathlib import Path

from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


def load_inventory(filename: Path) -> Inventory:
    inventory = Inventory()
    if not filename.exists():
        return inventory
    with filename.open("r", encoding="utf-8") as file:
        records = json.load(file)
    if not isinstance(records, list):
        raise ValueError("Inventory file must contain a list of products.")
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Each saved product must be a JSON object.")
        common = (record["id"] if "id" in record else record["product_id"],
                  record["name"], record["price"], record["stock"])
        if record.get("type") == "physical":
            product = PhysicalProduct(*common, record["weight"])
        elif record.get("type") == "digital":
            product = DigitalProduct(*common, record["download_size"])
        else:
            raise ValueError("Each product must have type 'physical' or 'digital'.")
        inventory.add_product(product)
    return inventory


def save_inventory(inventory: Inventory, filename: Path) -> None:
    records = []
    for product in inventory.products:
        record = {"id": product.product_id, "name": product.name,
                  "price": product.price, "stock": product.stock}
        if isinstance(product, PhysicalProduct):
            record.update(type="physical", weight=product.weight)
        elif isinstance(product, DigitalProduct):
            record.update(type="digital", download_size=product.download_size)
        else:
            raise ValueError(f"Unsupported product type: {type(product).__name__}")
        records.append(record)
    # Write completely before replacing the previous saved file.
    temporary_file = filename.with_suffix(filename.suffix + ".tmp")
    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4, allow_nan=False)
    temporary_file.replace(filename)
