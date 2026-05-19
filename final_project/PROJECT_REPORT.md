# Project Title

Online Store Simulation

## Problem Description

The project is a console-based online store that allows a customer to view products, add products to a cart, remove products from the cart, and complete checkout. The program solves a practical shopping problem by calculating totals, applying a premium customer discount, reducing stock, and saving orders to files.

## Features

- View product catalog
- Add products to a shopping cart
- Remove products from the shopping cart
- View subtotal, discount, and final total
- Checkout and save order data
- Reduce product stock after purchase
- Save and load data using JSON files

## Technologies Used

- Python 3
- Standard library modules: `json`, `datetime`, and `pathlib`
- JSON files for product and order storage
- `unittest` for testing

## Program Structure

```text
main.py              Console menu and user interaction
store.py             Store logic, checkout, JSON file handling
product.py           Product class
cart.py              Cart class
user.py              User, Customer, and PremiumCustomer classes
data/products.json   Saved product catalog
data/orders.json     Saved order history
tests/test_store.py  Unit tests
```

## Programming Concepts Used

- Variables, data types, arithmetic operations, and comparison operators
- User input and output through a console menu
- Conditional statements and loops
- Lists and dictionaries
- More than five custom functions with parameters and return values
- Object-oriented programming with constructors
- Inheritance: `Customer` and `PremiumCustomer` are user types
- Polymorphism: checkout calls `get_discount_rate()` differently for customer types
- JSON file handling
- Multiple Python modules
- Lambda function in product sorting
- Try-except error handling and input validation
- Unit testing with `unittest`

## Challenges Faced

One challenge was keeping the cart total correct while also checking product stock. Another challenge was saving changes to JSON files only after checkout succeeds, so product quantities do not change after a failed order.

## Screenshots / Example Run

```text
============================================================
                  Online Store Simulation
============================================================
Customer: Dana (Premium)
1. View product catalog
2. Add product to cart
3. Remove product from cart
4. View cart
5. Checkout
0. Exit
Choose an option: 2

Enter product ID: P001
Enter quantity: 2
2 item(s) added to cart.

Subtotal : $49.98
Discount : $5.00
Total    : $44.98
```

## Conclusion

The Online Store Simulation demonstrates the main Python programming concepts required for the final project. It is modular, menu-driven, uses object-oriented programming, handles invalid input, stores data in JSON files, and includes unit tests for important store behavior.
