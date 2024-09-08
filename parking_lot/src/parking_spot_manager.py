import heapq
from abc import ABC

from .parking_spot import ParkingSpot, TwoWheelerSpace, FourWheelerSpace
from .vehicle import VehicleType
from .space_finding_stategy import ParkingSlotFindingStategyFactory, PARKING_SLOT_FINDING_STATEGY, NoPreferenceFindStategy
from .heaps import ElevatorHeaps, EntranceHeaps

class ParkingSlotManagerFactory:

    def get_manager(vehicle_type: "VehicleType")-> 'ParkingSpotManager':
        if vehicle_type == VehicleType.TWO_WHEELER:
            print("here at 2 w")
            return TwoWheelerParkingSpotManager.get_instance()
        elif vehicle_type == VehicleType.FOUR_WHEELER:
            print("here at 4 w")
            return FourWheelerParkingSpotManager.get_instance()

class ParkingSpotManager(ABC):
    
    def __init__(self):
        self.parking_slots_map = {}
        self.last_id = 0
        self.vacant_spots = []
        self.entrance_heaps = ElevatorHeaps()
        self.elevator_heaps = ElevatorHeaps()

    def find_slot(self, entrance_id, stategy_enum):
        stategy = ParkingSlotFindingStategyFactory().get_stategy(stategy_enum, self)
        if stategy_enum is PARKING_SLOT_FINDING_STATEGY.NEAR_ELEVATOR:
            parking_spot = stategy.find_spot()
        else:
            parking_spot = stategy.find_spot(entrance_id)
        if parking_spot:
            return parking_spot
        stategy = NoPreferenceFindStategy(self)
        parking_spot = stategy.find_spot()
        if parking_spot:
            return parking_spot
        return None  


    def park(self, slot_id, vehicle):
        parking_slot: ParkingSpot = self.get_parking_spot(slot_id)
        parking_slot.park(vehicle)

    def add_slot(self, charge=None):
        print(self.spot_class)
        spot = self.spot_class(self.last_id + 1, charge)
        self.parking_slots_map[spot.spot_id] = spot
        self.last_id += 1
        self.vacant_spots.append(spot.spot_id)
        print(f"slot added at {spot.spot_id}")

    def remove_spot(self, spot_id):
        try:
            self.vacate_spot(spot_id)
            parking_slot: ParkingSpot = self.parking_slots_map.pop(spot_id)
        except KeyError as e:
            print("parking slot with id {spot_id} does not exist")
        print(f"slot {parking_slot.spot_id} removed")

    def get_parking_spot(self, spot_id)-> ParkingSpot:
        try:
            print(self.parking_slots_map)
            print("slot id", spot_id)
            return self.parking_slots_map[spot_id]
        except KeyError:
            raise Exception(f"parking slot with id {spot_id} does not exist")
    
    def park_on_spot(self, spot_id, vehicle):
        parking_slot = self.get_parking_spot(spot_id)
        parking_slot.park(vehicle)
        self.__make_spot_occupied(parking_slot)

    def vacate_spot(self, spot_id):
        parking_slot = self.get_parking_spot(spot_id)
        parking_slot.unpark()
        self.__make_spot_vacent()

    def __make_spot_occupied(self, parking_spot):
        self.vacant_spots.remove(parking_spot.spot_id)

    def __make_spot_vacent(self, parking_spot):
        self.vacant_spots.append(parking_spot.spot_id)
        self.entrance_heaps.push(parking_spot)
        self.elevator_heaps.push(parking_spot)

    def get_total_spots(self):
        return len(self.parking_slots_map)

    def get_empty_spots(self):
        return len(self.vacant_spots)


class FourWheelerParkingSpotManager(ParkingSpotManager):

    __instance : 'FourWheelerParkingSpotManager' = None

    def __init__(self):

        if FourWheelerParkingSpotManager.__instance:
            raise Exception("Singleton class is already initialized")
        super().__init__()
        self.spot_class = FourWheelerSpace 
        FourWheelerParkingSpotManager.__instance = self
    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls()
        return cls.__instance
    

class TwoWheelerParkingSpotManager(ParkingSpotManager):

    __instance : 'TwoWheelerParkingSpotManager' = None

    def __init__(self):
        if TwoWheelerParkingSpotManager.__instance:
            raise Exception("Singleton class is already initialized")
        super().__init__()
        self.spot_class = TwoWheelerSpace
        TwoWheelerParkingSpotManager.__instance = self


    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls()
        return cls.__instance