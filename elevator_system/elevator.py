from movement_controller import ElevatorController, Direction, ElevatorState

class Elevator:

    def __init__(self, id):

        self.id = id
        self.movement_controller = ElevatorController()


    def get_elevator_state(self)-> ElevatorState:
        return self.movement_controller.state

    def move(self, floor: int, dir: Direction):
        self.movement_controller.queue_request(floor, dir)

