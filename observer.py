from abc import ABC, abstractmethod
from subject import AbSubject, ConcreteSubject

class AbObserver(ABC):
    '''
        base abstract observer class 
            - execute a method when it is notified
    '''    
    
    @abstractmethod
    def execute_when_notified(self, subject: ConcreteSubject) -> None:
        pass


class ConcreteObserverA(AbObserver):
    '''
        implement AbObserver
    '''
    
    def execute_when_notified(self, subject: ConcreteSubject) -> None:
        print('I\'m notified, and now I\'m going to do something useful.')
        if subject.state >= 5:
            print('I\'m lucky today')

class ConcreteObserverB(AbObserver):
    '''
        implement AbObserver
    '''
    
    def execute_when_notified(self, subject: ConcreteSubject) -> None:
        print('I\'m notified, and now I\'m going to do something useful.')
        if subject.state <= 6:
            print('Weather is bad today!')