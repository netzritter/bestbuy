class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name can't be empty.")
        if price < 0:
            raise ValueError("Price can't be negative.")
        if quantity < 0:
            raise ValueError("Quantity can't be negative.")

        # Initialize instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity


    def set_quantity(self, quantity: int):
        """Set quantity. Deactivate product if quantity reaches zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """Check if the product is active."""
        return self.active


    def activate(self):
        """Activate the product."""
        self.active = True


    def deactivate(self):
        """Deactivate the product."""
        self.active = False


    def show(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity: int) -> float:
        """Purchase process: Returns the total price, updates quantity,
        and deactivates if warehouse is empty."""
        if not self.active:
            raise ValueError(f"Product '{self.name}' is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError(
                f"The requested {quantity} of '{self.name}' is not on stock (available {self.quantity})."
            )

        total_price = self.price * quantity
        # Update stock
        self.set_quantity(self.quantity - quantity)
        return total_price


