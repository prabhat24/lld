import random
from abc import ABC, abstractmethod

class ElevatorSelectionStategy(ABC):
    
    @abstractmethod
    def select_elevator(self):
        pass


class OddEvenSelectionStategy(ElevatorSelectionStategy):
    
    def __init__(self, floors: int, elevators: int):
        self.floor = floors
        self.elevators = elevators

    def select_elevator(self, src_floor):
        if src_floor % 2:
            # odd
            odd_elevators = [i for i in range(0, self.elevators) if i%2==1]
            return odd_elevators[random.randint(0, len(odd_elevators)-1)]
        else:
            # event
            event_elevators =  [i for i in range(0, self.elevators) if i%2==0]
            return event_elevators[random.randint(0, len(event_elevators)-1)]
        

class ZoneSelectionStategy:

    def __init__(self, floors: int, elevators: int):
        self.floor = floors
        self.elevators = elevators

    
    def select_elevator(self, floor):
        return 2