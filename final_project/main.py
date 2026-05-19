"""Menu-driven console interface for Online Store Simulation."""

from cart import Cart
from store import Store
from user import Customer, PremiumCustomer


def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def get_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a non-empty value.")


def get_int(prompt, minimum=1):
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def pause():
    input("\nPress Enter to continue...")


def create_customer():
    print_header("Customer Information")
    name = get_text("Enter your name: ")
    premium_answer = input("Are you a premium customer? (y/n): ").strip().lower()

    if premium_answer == "y":
        return PremiumCustomer(name)
    return Customer(name)


def show_products(store):
    print_header("Product Catalog")
    print("ID     | Name                    | Category       | Price    | Stock")
    print("-" * 60)
    for product in store.get_products():
        print(product)


def add_product_to_cart(store, cart):
    show_products(store)
    product_id = get_text("\nEnter product ID: ").upper()
    quantity = get_int("Enter quantity: ")

    try:
        product = store.find_product(product_id)
        cart.add_item(product, quantity)
        print(f"{quantity} item(s) added to cart.")
    except ValueError as error:
        print(f"Error: {error}")


def remove_product_from_cart(cart):
    if cart.is_empty():
        print("Your cart is empty.")
        return

    product_id = get_text("Enter product ID to remove: ").upper()
    try:
        cart.remove_item(product_id)
        print("Product removed from cart.")
    except ValueError as error:
        print(f"Error: {error}")


def show_cart(cart, store, customer):
    print_header("Shopping Cart")
    if cart.is_empty():
        print("Your cart is empty.")
        return

    print("ID     | Product                 | Qty | Subtotal")
    print("-" * 60)
    for product, quantity, subtotal in cart.get_lines(store.products):
        print(f"{product.product_id:<6} | {product.name:<23} | {quantity:>3} | ${subtotal:>7.2f}")

    subtotal = cart.calculate_subtotal(store.products)
    discount = store.calculate_discount(subtotal, customer)
    total = subtotal - discount

    print("-" * 60)
    print(f"Subtotal : ${subtotal:.2f}")
    print(f"Discount : ${discount:.2f}")
    print(f"Total    : ${total:.2f}")


def checkout(store, cart, customer):
    show_cart(cart, store, customer)
    if cart.is_empty():
        return

    answer = input("\nComplete checkout? (y/n): ").strip().lower()
    if answer != "y":
        print("Checkout cancelled.")
        return

    try:
        order = store.checkout(cart, customer)
        print(f"Order saved successfully. Order ID: {order['order_id']}")
        print(f"Amount paid: ${order['total']:.2f}")
    except ValueError as error:
        print(f"Checkout failed: {error}")


def main():
    store = Store()
    cart = Cart()
    customer = create_customer()

    while True:
        print_header("Online Store Simulation")
        print(f"Customer: {customer.name} ({customer.customer_type})")
        print("1. View product catalog")
        print("2. Add product to cart")
        print("3. Remove product from cart")
        print("4. View cart")
        print("5. Checkout")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_products(store)
            pause()
        elif choice == "2":
            add_product_to_cart(store, cart)
            pause()
        elif choice == "3":
            remove_product_from_cart(cart)
            pause()
        elif choice == "4":
            show_cart(cart, store, customer)
            pause()
        elif choice == "5":
            checkout(store, cart, customer)
            pause()
        elif choice == "0":
            print("Thank you for shopping with us.")
            break
        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()
