"""Product model for the online store."""


class Product:
    """Represents one product in the catalog."""

    def __init__(self, product_id, name, category, price, quantity):
        self._product_id = product_id
        self._name = name
        self._category = category
        self.price = price
        self.quantity = quantity

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = round(value, 2)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        value = int(value)
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value

    def reduce_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["product_id"],
            data["name"],
            data["category"],
            data["price"],
            data["quantity"],
        )

    def __str__(self):
        return (
            f"{self.product_id:<6} | {self.name:<23} | {self.category:<14} | "
            f"${self.price:>6.2f} | {self.quantity:>5}"
        )
