import sys
from Person import Person
sys.path.append(".")
from PersonTypes.Student import Student

class ProxyStudent(Person):

    def __init__(self):
        self.person = Student()

    def person_method(self):
        print("Hello there!, student")
        self.person.person_method()
       