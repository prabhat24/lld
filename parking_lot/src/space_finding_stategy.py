from abc import ABC, abstractmethod
from enum import Enum

class PARKING_SLOT_FINDING_STATEGY(Enum):

    NEAR_ELEVATOR = "NEAR_ELEVATOR"
    NEAR_ENTRANCE = "NEAR_ENTRANCE"

class ParkingSlotFindingStategyFactory:


    def get_stategy(self, stategy, psm)-> 'ParkingSlotFindingStategy':
        if stategy == PARKING_SLOT_FINDING_STATEGY.NEAR_ELEVATOR:
            return NearElevatorSlotFindingStategy(psm)
        elif stategy == PARKING_SLOT_FINDING_STATEGY.NEAR_ENTRANCE:
            return NearEntranceSlotFindingStrategy(psm)
        

class ParkingSlotFindingStategy:

    @abstractmethod
    def find_spot(self, *args, **kwargs):
        pass


class NearElevatorSlotFindingStategy:

    def __init__(self, psm):
        self.psm = psm
        self.elevator_heaps = self.psm.elevator_heaps

    def find_spot(self):
        for elevator_id, heap in self.elevator_heaps.get_heaps().items():
            if heap:
                while len(heap):
                    _, parking_spot =  self.elevator_heaps.pop(elevator_id)
                    if parking_spot.is_vacent:
                        return parking_spot
        return None
    
class NearEntranceSlotFindingStrategy:

    def __init__(self, psm):
        self.psm = psm
        self.entrance_heaps = self.psm.entrance_heaps

    def find_spot(self, entrance_id):
        min_heap = self.entrance_heaps.get(entrance_id)
        if min_heap:
            _, parking_spot = self.entrance_heaps.pop(entrance_id)
            if parking_spot.is_vacent:
                return parking_spot
        return None
    
class NoPreferenceFindStategy:

    def __init__(self, psm):
        self.psm = psm

    def find_spot(self):
        if self.psm.vacant_spots:
            spot_id = self.psm.vacant_spots[-1]
            return self.psm.get_parking_spot(spot_id)
        return None