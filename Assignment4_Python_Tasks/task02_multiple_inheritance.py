class Flyable:
    def fly(self):
        return "Duck can fly"


class Swimmable:
    def swim(self):
        return "Duck can swim"


class Duck(Flyable, Swimmable):
    pass


if __name__ == "__main__":
    duck = Duck()

    print(duck.fly())
    print(duck.swim())
