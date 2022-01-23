import sys
sys.path.append(".")
from Proxys.ProxyTeacher import ProxyTeacher
from Proxys.ProxyStudent import ProxyStudent
from Observer import ConcreteSubject
from Observer import ConcreteObserverA
from Observer import ConcreteObserverB
class PersonFactory: 

    @staticmethod
    def generate_person(person_type):
        subject = ConcreteSubject()
        
        if person_type == "student":
            observer_a = ConcreteObserverA()
            subject.attach(observer_a)
            subject.some_business_logic()
            return ProxyStudent()

        if person_type == "teacher":
            observer_b = ConcreteObserverB()
            subject.attach(observer_b)
            subject.some_business_logic()
            return ProxyTeacher() 

        print("Not a person type")
        return -1