class Person:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Person"


class Teacher(Person):
    def get_role(self):
        return "Teacher"


class Student(Person):
    def get_role(self):
        return "Student"


class School:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def show_people(self):
        for person in self.people:
            print(f"{person.name} is a {person.get_role()}")


if __name__ == "__main__":
    school = School("Astana School")
    school.add_person(Teacher("Alice"))
    school.add_person(Student("Bob"))

    school.show_people()
