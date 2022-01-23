import sys
from Person import Person
sys.path.append(".")
from PersonTypes.Teacher import Teacher

class ProxyTeacher(Person):

    def __init__(self):
        self.person = Teacher()

    def person_method(self):
        print("Hello there!, teacher")
        self.person.person_method()