"""User classes used to demonstrate inheritance and polymorphism."""


class User:
    """Base user class."""

    customer_type = "Standard"

    def __init__(self, name):
        self.name = name.strip()
        if not self.name:
            raise ValueError("Customer name cannot be empty.")

    def get_discount_rate(self):
        return 0.0


class Customer(User):
    """Standard customer with no discount."""

    pass


class PremiumCustomer(User):
    """Premium customer receives a discount during checkout."""

    customer_type = "Premium"

    def get_discount_rate(self):
        return 0.10
