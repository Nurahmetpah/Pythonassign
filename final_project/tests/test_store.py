"""Unit tests for Online Store Simulation."""

import unittest

from cart import Cart
from store import Store
from user import Customer, PremiumCustomer


class OnlineStoreTestCase(unittest.TestCase):
    def create_store(self):
        return Store(auto_save=False)

    def test_add_item_and_calculate_subtotal(self):
        store = self.create_store()
        cart = Cart()
        product = store.find_product("P001")

        cart.add_item(product, 2)

        self.assertEqual(cart.items["P001"], 2)
        self.assertEqual(cart.calculate_subtotal(store.products), 49.98)

    def test_checkout_reduces_stock_and_saves_order(self):
        store = self.create_store()
        cart = Cart()
        customer = Customer("Aruzhan")

        cart.add_item(store.find_product("P001"), 1)
        order = store.checkout(cart, customer)

        self.assertEqual(order["total"], 24.99)
        self.assertEqual(store.find_product("P001").quantity, 19)
        self.assertEqual(len(store.orders), 1)
        self.assertTrue(cart.is_empty())

    def test_premium_customer_receives_discount(self):
        store = self.create_store()
        cart = Cart()
        customer = PremiumCustomer("Dias")

        cart.add_item(store.find_product("P002"), 1)
        order = store.checkout(cart, customer)

        self.assertEqual(order["discount"], 5.00)
        self.assertEqual(order["total"], 44.99)


if __name__ == "__main__":
    unittest.main()
