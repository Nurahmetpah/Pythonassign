"""Shopping cart module."""


class Cart:
    """Stores selected product IDs and quantities."""

    def __init__(self):
        self.items = {}

    def is_empty(self):
        return len(self.items) == 0

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if product.quantity <= 0:
            raise ValueError("Product is out of stock.")

        current_quantity = self.items.get(product.product_id, 0)
        new_quantity = current_quantity + quantity
        if new_quantity > product.quantity:
            raise ValueError("Requested quantity is greater than available stock.")

        self.items[product.product_id] = new_quantity

    def remove_item(self, product_id):
        if product_id not in self.items:
            raise ValueError("Product is not in the cart.")
        del self.items[product_id]

    def get_lines(self, products):
        lines = []
        for product_id, quantity in self.items.items():
            product = products[product_id]
            subtotal = round(product.price * quantity, 2)
            lines.append((product, quantity, subtotal))
        return lines

    def calculate_subtotal(self, products):
        return round(sum(line[2] for line in self.get_lines(products)), 2)

    def clear(self):
        self.items.clear()
