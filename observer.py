from abc import ABC, abstractmethod

class AbObserver(ABC):
    '''
        base abstract observer class 
            - execute a method when it is notified
    '''    
    
    @abstractmethod
    def execute_when_notified(self, state: int) -> None:
        pass

    @abstractmethod
    def __str__(self):
        pass

class ConcreteObserverA(AbObserver):
    '''
        implement AbObserver
    '''
    
    def execute_when_notified(self, state) -> None:
        print('Observer A: I\'m notified')
        if state >= 5:
            print('Observer A: I\'m lucky today')

    def __str__(self):
        return 'Observer A'

class ConcreteObserverB(AbObserver):
    '''
        implement AbObserver
    '''
    
    def execute_when_notified(self, state) -> None:
        print('Observer B: I\'m notified.')
        if state <= 6:
            print('Observer B: Weather is bad today!')
    
    def __str__(self):
        return 'Observer B'