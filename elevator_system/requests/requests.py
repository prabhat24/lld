from abc import ABC, abstractmethod


class IESRequests(ABC):
    pass


class ExternalRequest(IESRequests):

    def __init__(self, direction, src_floor, zone=1):
        self.direction = direction
        self.src_floor = src_floor
        self.zone = zone

    def get_src_floor(self):
        return self.src_floor
    
    def get_direction(self):
        return self.direction

class InternalRequest(IESRequests):

    def __init__(self, elevator_id, dest_floor):
        self.elevator_id = elevator_id
        self.dest_floor = dest_floor

    def get_dest_floor(self):
        return self.dest_floor
    
    def get_elevator_id(self):
        return self.elevator_id