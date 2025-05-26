from products import Product

class Store:
    def __init__(self, items=None):
        """
        Initialize the Store with a list of products (optional)
        """
        if items is None:
            items = []
        # Validate that all items belong to Product class
        for item in items:
            if not isinstance(item, Product):
                raise ValueError("All items must belong to the Product class.")
        self.items = list(items)


    def add_product(self, item: Product):
        """
        Add a Product to the store.
        """
        if not isinstance(item, Product):
            raise ValueError("Can only add Product instances.")
        self.items.append(item)


    def remove_product(self, item: Product):
        """
        Remove a Product from the store.
        """
        try:
            self.items.remove(item)
        except ValueError:
            raise ValueError("Product not found in the store.")


    def get_total_quantity(self) -> int:
        """
        Return the total quantity of all products in the store.
        """
        return sum(items.get_quantity() for items in self.items)


    def get_all_products(self) -> list:
        """
        Return a list of all active products in the store.
        """
        return [items for items in self.items if items.is_active()]


    def order(self, shopping_list: list) -> float:
        """
        Gets a list of items (Product class) and requested quantity.
        Returns the total price of the order.
        """
        total_price = 0.0
        for item, quantity in shopping_list:
            if item not in self.items:
                raise ValueError(f"{item.name} not on stock.")
            total_price += item.buy(quantity)
        return total_price


def main():
        product_list = [Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        ]
        best_buy = Store(product_list)
        products = best_buy.get_all_products()
        print(best_buy.get_total_quantity())
        print(best_buy.order([(products[0], 1), (products[1], 2)]))

if __name__ == "__main__":
    main()

