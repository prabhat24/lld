from elevator import Elevator

class ElevatorManager():

    __elevator_manager = None

    def __init__(self):
        if ElevatorManager.__elevator_manager:
            raise Exception("cannot initialize elevator manager as its singleton")
        ElevatorManager.__elevator_map : dict = {}
        ElevatorManager.__elevator_manager = self

    @classmethod
    def get_elevator_manager(cls):
        if not cls.__elevator_manager:
            cls()
        return cls.__elevator_manager

    def get_elevator(self, elevator_id)-> Elevator:
        try:
            return self.__elevator_map[elevator_id]
        except KeyError as e:
            raise Exception(f"cannot find the elevator")

    def initialize_elevators(self, no_of_elevators):
        for i in range(0, no_of_elevators):
            self.__elevator_map[i] = Elevator(i)

    

    
