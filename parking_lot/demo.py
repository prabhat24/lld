from src.parking_lot import ParkingFloor
from src.vehicle import Vehicle, VehicleType


import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
# system setup
parking_lot = ParkingFloor()
parking_lot.initialize_entrances(2)
parking_lot.initialize_exits(2)
parking_lot.initialize_parking_floor(no_of_two_wheeler_spots=10, no_of_four_wheeler_spots=20)



# go to gate 0 and park mercedes 
reg_no = ""
while(reg_no!="q"):
    reg_no = input("enter regno")
    vehicle = Vehicle(reg_no=reg_no, vtype=VehicleType.FOUR_WHEELER)
    entry_gate = parking_lot.get_entry_terminal(0)


    spot = entry_gate.find_spot(vehicle.vtype)
    print("find spot response", spot)

    if spot:
        ticket = entry_gate.book_spot(vehicle, spot["id"])
        print(ticket)
    print(parking_lot.display())

