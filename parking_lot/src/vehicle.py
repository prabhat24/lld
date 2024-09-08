from enum import Enum
from datetime import datetime as dt

class VehicleType(Enum):
    TWO_WHEELER = "TWO_WHEELER"
    FOUR_WHEELER = "FOUR_WHEELER"

class Vehicle():

    def __init__(self, reg_no, vtype):
        self.reg_no = reg_no
        self.vtype = vtype


class TicketManager:

    __instance: 'TicketManager' = None

    def __init__(self):
        if TicketManager.__instance:
            raise Exception("Singleton can be initialized once only")
        self.ticket_map: dict[int: Ticket] = dict()
        self.last_id = 0
        TicketManager.__instance = self

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            return cls()
        return cls.__instance

    def create_ticket(self, vehicle, parking_spot):
        ticket = Ticket(self.last_id, vehicle, parking_spot)
        self.ticket_map[ticket.id] = ticket
        self.last_id += 1
        return ticket

class Ticket():

    def __init__(self, id, vehicle, parking_spot):
        self.id = id
        self.vehicle = vehicle
        self.entry_time = dt.now()
        self.exit_time = None
        self.parking_spot = parking_spot
        self.ticket_status = TicketStatus.PARKED

    def make_exit(self):
        self.ticket_status = TicketStatus.VACATED
        self.exit_time = dt.now()
        return self.exit_time

    def print_ticket(self):
        return {
            "ticket_no": self.id,
            "vehicle_reg_no": self.vehicle.reg_no,
            "entry_time": self.entry_time,
            "parking_spot_id": self.parking_spot.spot_id, 
            "spot_type": self.parking_spot.__class__.__name__
        }

class TicketStatus:
    PARKED = "PARKED"
    VACATED = "VACATED"