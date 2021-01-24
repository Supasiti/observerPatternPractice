from abc import ABC, abstractmethod
from observer import AbObserver
from random import randrange

class AbSubject(ABC):
    '''
    base abstract subject class 
        - can subscribe to  
        - can unsubscribe to
        - can notify any new update 
    '''

    @abstractmethod
    def subscribe(self, observer: AbObserver) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: AbObserver) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(AbSubject):
    '''
        concrete implementation of AbSubject
    '''
    __state = 1
    __observers: list[AbObserver] = []

    def subscribe(self, observer: AbObserver) -> None:
        print('Subject: Subscribe observer to the list.')
        self.__observers.append(observer)

    def unsubscribe(self, observer: AbObserver) -> None:
        print('Subject: Unsubscibe %s from the list.' % observer.__str__())
        self.__observers.remove(observer)

    def notify(self) -> None:
        print('Subject: Notify all the observers in the list.')
        for observer in self.__observers:
            observer.execute_when_notified(self.__state)
      
    def some_business_logic(self):
        print("\nSubject: I'm doing something important.")
        self.__state = randrange(0, 10)
        print('    New state: %d' % self.__state)
        self.notify()