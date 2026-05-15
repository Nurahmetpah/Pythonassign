class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal makes a sound"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


if __name__ == "__main__":
    animal = Animal("Generic animal")
    dog = Dog("Buddy")

    print(animal.speak())
    print(dog.speak())
