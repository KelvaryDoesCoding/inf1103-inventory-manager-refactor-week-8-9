# Console menu for the inventory system

from pathlib import Path

from file_handling import load_inventory, save_inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct


DATA_FILE = Path(__file__).resolve().with_name("inventory.json")


def main() -> None:
    try:
        inventory = load_inventory(DATA_FILE)
    except (OSError, ValueError, KeyError, TypeError, OverflowError) as error:
        print(f"Cannot load inventory: {error}")
        print("Please fix the inventory file and restart the program.")
        return

    while True:
        print("\nInventory Management System")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search for a product")
        print("5. Save inventory")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                inventory.display_all()
            elif choice == "2":
                product_type = input("Product type (1 = physical, 2 = digital): ").strip()
                if product_type not in ("1", "2"):
                    raise ValueError("Choose 1 for physical or 2 for digital.")
                product_id = inventory.generate_product_id()
                print(f"Product ID: {product_id}")
                name = input("Product name: ")
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                if product_type == "1":
                    weight = float(input("Weight (kg): "))
                    product = PhysicalProduct(product_id, name, price, stock, weight)
                else:
                    download_size = float(input("Download size (MB): "))
                    product = DigitalProduct(product_id, name, price, stock, download_size)
                inventory.add_product(product)
                print("Product added successfully!")
            elif choice == "3":
                product_id = input("Product ID: ")
                quantity = int(input("New stock quantity: "))
                inventory.update_stock(product_id, quantity)
                print("Stock updated successfully!")
            elif choice == "4":
                product = inventory.search_product(input("Product ID: "))
                if product is None:
                    print("Product not found.")
                else:
                    product.display_information()
            elif choice == "5":
                save_inventory(inventory, DATA_FILE)
                print("Inventory saved.")
            elif choice == "6":
                print("Saving inventory before exit...")
                save_inventory(inventory, DATA_FILE)
                print("Thank you for using Inventory Management System.")
                break
            else:
                print("Please enter a choice from 1 to 6.")
        except (ValueError, OSError, OverflowError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed. Unsaved changes were not saved.")
