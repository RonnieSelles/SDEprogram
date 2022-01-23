import sys
sys.path.append(".")
from Factories.PersonFactory import PersonFactory

class Application:
    choice = input("Are you a student or a teacher?\n")
    person = PersonFactory.generate_person(choice)
    person.person_method()