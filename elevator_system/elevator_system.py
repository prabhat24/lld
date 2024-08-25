from requests.requests import InternalRequest, ExternalRequest
from elevator_manager import ElevatorManager
from request_processors import ExternalRequestProcessor, InternalRequestProcessor
from elevator_selection_stategy import ElevatorSelectionStategy

class ElevatorSystem:

    __elevator_system = None
    elevator_manager: ElevatorManager = None
    __elevator_selection_stategy: ElevatorSelectionStategy = None

    def __init__(self):
        if ElevatorSystem.__elevator_system:
            raise Exception("elevator system is already present")
        self.internal_request_processor = None
        self.external_request_processor = None
        self.__total_floors = None
        self.__total_elevators = None
        ElevatorSystem.__elevator_system = self
    
    @classmethod
    def get_elevator_system(cls):
        if not cls.__elevator_system:
            cls()
        return cls.__elevator_system

    def set_elevator_selection_stategy(self, stategy):
        self.__elevator_selection_stategy = stategy(self.__total_floors, self.__total_elevators)
        self.internal_request_processor = InternalRequestProcessor()
        self.external_request_processor = ExternalRequestProcessor(self.__elevator_selection_stategy)

    def initialize_elevator_system(self, total_floors: int, total_elevators: int):
        self.__total_elevators = total_elevators
        self.__total_floors = total_floors
        print(f"Initializing elevator system with  {total_floors} floors and {total_elevators} elevators!");
        elevator_manager = ElevatorManager.get_elevator_manager()
        elevator_manager.initialize_elevators(total_elevators)


    def send_internal_request(self, elevator_id, dest_floor):
        int_req = InternalRequest(elevator_id, dest_floor)
        self.internal_request_processor.process(int_req)

    def send_external_request(self, src_floor, direction):
        ext_req = ExternalRequest(direction, src_floor)
        self.external_request_processor.process(ext_req)


    