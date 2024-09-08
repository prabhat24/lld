from .terminals import EntryTerminal, ExitTerminal
from .parking_spot_manager import TwoWheelerParkingSpotManager, FourWheelerParkingSpotManager


class DisplayBoard():
    def display(parking_floor):
        return {
            "2 wheeler empty/total": f"{parking_floor.two_wheeler_psm.get_empty_spots()}/{parking_floor.two_wheeler_psm.get_total_spots()}",
            "4 wheeler empty/total": f"{parking_floor.four_wheeler_psm.get_empty_spots()}/{parking_floor.four_wheeler_psm.get_total_spots()}"
        }

class ParkingFloor():

    display_stategy = DisplayBoard

    def __init__(self):
        self.entrances: dict[int: EntryTerminal] = dict()
        self.exits: dict[int: ExitTerminal] = dict()
        self.two_wheeler_psm = TwoWheelerParkingSpotManager.get_instance()
        self.four_wheeler_psm = FourWheelerParkingSpotManager.get_instance()
        print("pf0, 2", self.two_wheeler_psm)
        print("pf0, 4", self.four_wheeler_psm)

    def initialize_entrances(self, no_of_entrances):
        for i in range(no_of_entrances):
            entry_terminal = EntryTerminal(i)
            self.entrances[i] = entry_terminal

    def initialize_exits(self, no_of_exits):
        for i in range(no_of_exits):
            exit_terminal = ExitTerminal(i)
            self.exits[i] = exit_terminal

    def initialize_parking_floor(self, no_of_two_wheeler_spots, no_of_four_wheeler_spots):

        for i in range(no_of_two_wheeler_spots):
            self.two_wheeler_psm.add_slot(charge=2)
        print("pf1", self.two_wheeler_psm)
        for j in range(no_of_four_wheeler_spots):
            self.four_wheeler_psm.add_slot(charge=5)
        print("pf1", self.four_wheeler_psm)
    def display(self):
        return self.display_stategy.display(self)

    def get_entry_terminal(self, id)-> EntryTerminal:
        return self.entrances.get(id)

    def get_exit_terminal(self, id)-> ExitTerminal:
        return self.exits.get(id)