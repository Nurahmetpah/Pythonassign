"""Store operations and JSON file handling."""

import json
from datetime import datetime
from pathlib import Path

from product import Product


DEFAULT_PRODUCTS = [
    {"product_id": "P001", "name": "Wireless Mouse", "category": "Electronics", "price": 24.99, "quantity": 20},
    {"product_id": "P002", "name": "Keyboard", "category": "Electronics", "price": 49.99, "quantity": 15},
    {"product_id": "P003", "name": "Notebook", "category": "Stationery", "price": 5.50, "quantity": 40},
    {"product_id": "P004", "name": "Backpack", "category": "Accessories", "price": 34.99, "quantity": 12},
    {"product_id": "P005", "name": "Water Bottle", "category": "Lifestyle", "price": 12.00, "quantity": 25},
    {"product_id": "P006", "name": "Python Book", "category": "Books", "price": 29.95, "quantity": 10},
]


class Store:
    """Main class that loads products, processes orders, and saves data."""

    def __init__(self, data_directory="data", auto_save=True):
        self.data_directory = Path(data_directory)
        self.products_file = self.data_directory / "products.json"
        self.orders_file = self.data_directory / "orders.json"
        self.auto_save = auto_save
        self.products = {}
        self.orders = []
        self.load_data()

    def load_data(self):
        self.data_directory.mkdir(exist_ok=True)
        product_data = self._load_json(self.products_file, DEFAULT_PRODUCTS)
        self.orders = self._load_json(self.orders_file, [])
        self.products = {
            item["product_id"]: Product.from_dict(item)
            for item in product_data
        }

    def _load_json(self, file_path, default_value):
        try:
            if not file_path.exists():
                if self.auto_save:
                    self._save_json(file_path, default_value)
                return default_value

            with file_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (OSError, json.JSONDecodeError):
            print(f"Could not read {file_path.name}. Default data will be used.")
            return default_value

    def _save_json(self, file_path, data):
        if not self.auto_save:
            return

        try:
            with file_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except OSError as error:
            print(f"Could not save {file_path.name}: {error}")

    def save_products(self):
        product_data = [product.to_dict() for product in self.products.values()]
        self._save_json(self.products_file, product_data)

    def save_orders(self):
        self._save_json(self.orders_file, self.orders)

    def get_products(self):
        # Lambda is used here as the required advanced Python concept.
        return sorted(self.products.values(), key=lambda product: product.product_id)

    def find_product(self, product_id):
        product = self.products.get(product_id)
        if product is None:
            raise ValueError("Product not found.")
        return product

    def calculate_discount(self, subtotal, customer):
        return round(subtotal * customer.get_discount_rate(), 2)

    def checkout(self, cart, customer):
        if cart.is_empty():
            raise ValueError("Cart is empty.")

        lines = cart.get_lines(self.products)
        for product, quantity, _ in lines:
            if product.quantity <= 0 or quantity > product.quantity:
                raise ValueError(f"Not enough stock for {product.name}.")

        subtotal = cart.calculate_subtotal(self.products)
        discount = self.calculate_discount(subtotal, customer)
        total = round(subtotal - discount, 2)

        for product, quantity, _ in lines:
            product.reduce_stock(quantity)

        order = {
            "order_id": self._create_order_id(),
            "customer_name": customer.name,
            "customer_type": customer.customer_type,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": [
                {
                    "product_id": product.product_id,
                    "name": product.name,
                    "quantity": quantity,
                    "subtotal": subtotal,
                }
                for product, quantity, subtotal in lines
            ],
            "subtotal": subtotal,
            "discount": discount,
            "total": total,
        }

        self.orders.append(order)
        cart.clear()
        self.save_products()
        self.save_orders()
        return order

    def _create_order_id(self):
        return "ORD" + datetime.now().strftime("%Y%m%d%H%M%S")
