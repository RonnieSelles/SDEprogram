import sys
sys.path.append(".")
from Person import Person

class Student(Person):

    def __init__(self):
        self.name = 'student name'

    def person_method(self):
        print('**Selected Student**')