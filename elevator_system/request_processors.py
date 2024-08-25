from requests.requests import InternalRequest, ExternalRequest
from elevator_manager import ElevatorManager
from elevator import Elevator
from elevator_selection_stategy import ElevatorSelectionStategy

class InternalRequestProcessor():

    def __init__(self):
        pass

    def process(self, int_req: InternalRequest):
        elevator: Elevator = ElevatorManager.get_elevator_manager().get_elevator(int_req.get_elevator_id())
        current_floor = elevator.get_elevator_state().get_current_floor()
        if int_req.dest_floor >= current_floor:
            elevator.move(int_req.get_dest_floor(), "u")
        else:
            elevator.move(int_req.get_dest_floor(), "d")

class ExternalRequestProcessor():

    def __init__(self, elevator_selector):
        self.elevator_selector: ElevatorSelectionStategy = elevator_selector

    def process(self, ext_req: ExternalRequest):
        elevator_id = self.elevator_selector.select_elevator(ext_req.get_src_floor())
        print("dfas")
        print(f"selected elevator id by {self.elevator_selector.__class__.__name__} is {elevator_id}")
        elevator: Elevator = ElevatorManager.get_elevator_manager().get_elevator(elevator_id)
        elevator.move(ext_req.get_src_floor(), ext_req.direction)