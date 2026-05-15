class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")


if __name__ == "__main__":
    student = Student("Alice", 20, "Computer Science")
    student.display_info()
