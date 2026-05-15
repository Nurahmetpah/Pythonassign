from mypackage.calculator import add
from mypackage.greetings import say_hello


if __name__ == "__main__":
    print(say_hello("Alice"))
    print(f"Sum: {add(10, 5)}")
