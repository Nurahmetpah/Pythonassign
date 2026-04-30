class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def restock(self, amount):
        self.quantity += amount
        print(f"Restocked {amount} {self.name}(s). New quantity: {self.quantity}")

    def sell(self, amount):
        if amount > self.quantity:
            print(f"Cannot sell {amount} {self.name}(s). Only {self.quantity} available.")
        else:
            self.quantity -= amount
            print(f"Sold {amount} {self.name}(s). New quantity: {self.quantity}")

if __name__ == "__main__":
    item = Item("Laptop", 1000, 10)
    print(f"Total value: {item.total_value()}")
    item.sell(3)
    item.restock(5)
    item.sell(15)
