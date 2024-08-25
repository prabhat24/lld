from elevator_system import ElevatorSystem
from elevator_selection_stategy import OddEvenSelectionStategy
from movement_controller import Direction

elevator_system = ElevatorSystem.get_elevator_system()
elevator_system.initialize_elevator_system(22, 6)
elevator_system.set_elevator_selection_stategy(OddEvenSelectionStategy)

elevator_system.send_external_request(4, Direction.MOVING_UP)

print("===============")