import sys
sys.path.append(".")
from Person import Person

class Teacher(Person):

    def __init__(self):
        self.name = 'teacher name'

    def person_method(self):
        print('**Selected Teacher**')
      

    
        