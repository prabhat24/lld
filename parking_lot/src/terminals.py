
from datetime import datetime as dt

from .vehicle import Vehicle, TicketManager
from .parking_spot_manager import ParkingSlotManagerFactory
from .space_finding_stategy import PARKING_SLOT_FINDING_STATEGY
from .parking_spot_manager import ParkingSlotManagerFactory

# class BillCalculator():

#     def __init__(self, ticket):
#         self.ticket = ticket

#     def calculate_bill(self):
#         self.ticket.


class EntryTerminal:

    def __init__(self, id: str):
        self.id = id

    def __generate_ticket(self, vehicle: 'Vehicle', parking_spot: 'ParkingSpot'):
        ticket = TicketManager.get_instance().create_ticket(vehicle, parking_spot)
        return ticket.print_ticket()

    def book_spot(self, vehicle: 'Vehicle', parking_spot_id):
        parking_spot_manager = ParkingSlotManagerFactory.get_manager(vehicle.vtype)
        print("20",parking_spot_manager)
        parking_spot = parking_spot_manager.get_parking_spot(parking_spot_id)
        parking_spot_manager.park_on_spot(parking_spot_id, vehicle)
        return self.__generate_ticket(vehicle, parking_spot)
        
    def find_spot(self, 
            vehicle_type, 
            finding_strategy=PARKING_SLOT_FINDING_STATEGY.NEAR_ELEVATOR):
        parking_spot_manager = ParkingSlotManagerFactory.get_manager(vehicle_type)
        print("37", parking_spot_manager)
        parking_spot = parking_spot_manager.find_slot(self.id, finding_strategy)
        if parking_spot:
            return {
                "id": parking_spot.spot_id,
                "spot_type": parking_spot.__class__.__name__
            }
        return None


class ExitTerminal:
    
    def __init__(self, id: str):
        self.id = id

    # def __calculate_bill():
    #    pass


    # def checkout(ticket: Ticket):
    #     parking_spot_manager = ParkingSlotManagerFactory.get_manager(ticket.vehicle.vehicle_type)
    #     parking_spot_manager.vacate_slot(ticket.parking_spot.id)
    #     ticket.make_exit()
    #     BillCalculator(ticket)

        
    def make_paymen():
        pass