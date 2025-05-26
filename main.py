from products import Product
from store import Store

def start(store: Store):
    """
    Interactive menu-driven session for a Store instance.
    """
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ")
        if choice == '1':
            products = store.get_all_products()
            if not products:
                print("No products available.")
            else:
                print("------")
                for index, item in enumerate(products, start=1):
                    print(f"{index}. {item.show()}")
                print("------")
        elif choice == '2':
            total = store.get_total_quantity()
            print(f"Total of {total} items in store")
        elif choice == '3':
            products = store.get_all_products()
            if not products:
                print("No products available.")
                continue
            print("------")
            for index, item in enumerate(products, start=1):
                print(f"{index}. {item.show()}")
            print("------")
            print("When you want to finish order, enter empty text.")

            shopping_list = []

            while True:
                product_number = get_int_or_exit("Which product # do you want? ")
                if product_number is None:
                    break

                amount = get_int_or_exit("What amount do you want? ")
                if amount is None:
                    break

                index = product_number - 1
                if index < 0 or index >= len(products):
                    print("⚠️  Invalid product number.")
                    continue
                shopping_list.append((products[index], amount))

            if shopping_list:
                try:
                    cost = store.order(shopping_list)
                    print(f"\nOrder cost: {cost} dollars.")
                except ValueError as e:
                    print(f"Error processing order: {e}")
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


def get_int_or_exit(prompt: str) -> int | None:
    """
    Prompt the user until they either enter a valid integer or
    a blank line which returns None.
    """
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return None
        try:
            return int(raw)
        except ValueError:
            print("⚠️  Please enter an integer or blank to order.")


def main():
    """
    Setup initial stock of inventory and launch interactive session
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    store = Store(product_list)
    start(store)

if __name__ == "__main__":
    main()

