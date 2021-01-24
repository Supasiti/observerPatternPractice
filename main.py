from observer import ConcreteObserverA, ConcreteObserverB
from subject import ConcreteSubject


if __name__ == '__main__':
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.subscribe(observer_a)
    subject.subscribe(observer_b)

    # subject's state changes
    subject.some_business_logic()
    subject.some_business_logic()

    # unsubcibe B from subject
    subject.unsubscribe(observer_b)

    # subject's state changes
    subject.some_business_logic()
    subject.some_business_logic()

    