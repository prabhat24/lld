from abc import ABC

INT_MAX = 1 << 63 - 1

class ParkingSpot(ABC):
    
    slot_type = None

    def __init__(self, id):
        self.spot_id: str =  f"{self.slot_type}-{id}"
        self.vehicle: 'Vehicle' = None
        self.is_vacent = True
        self.charge = None

    def park(self, vehicle: 'Vehicle'):
        if not self.is_vacent:
            raise Exception(f"Spot {self.spot_id} is not empty")
        self.vehicle = vehicle
        self.is_vacent = False

    def unpark(self):
        self.is_vacent = True
        self.vehicle = None


class TwoWheelerSpace(ParkingSpot):

    slot_type = "2W"

    def __init__(self, id, charge, distance_from_elevator=None, distance_from_entrance=None):
        super().__init__(id)
        self.charge = charge
        self.distance_from_elevator = distance_from_elevator
        self.distance_from_entrance = distance_from_entrance

class FourWheelerSpace(ParkingSpot):

    slot_type = "4W"

    def __init__(self, id, charge, distance_from_elevator=None, distance_from_entrance=None):
        super().__init__(id)
        self.charge = charge
        self.distance_from_elevator = distance_from_elevator
        self.distance_from_entrance = distance_from_entrance
        
        