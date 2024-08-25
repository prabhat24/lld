from enum import Enum
import heapq

class State(Enum):
    MOVING = "MOVING"
    IDLE = "IDLE"
    NOT_WORKING = "NOT_WORKING"

class Direction(Enum):
    MOVING_UP = "u"
    MOVING_DOWN = "d"
    STOPPED = "s"

class ElevatorState:

    def __init__(self):
        self.state = None
        self.current_floor = None
        self.current_to_move_direction = None

    def set_init_state(self):
        self.state = State.IDLE
        self.current_floor = 0
        self.current_to_move_direction = Direction.MOVING_UP

    def set_elevator_state(self, state: State):
        self.state = state
    
    def set_direction(self, direction: Direction):
        self.current_to_move_direction = direction

    def set_floor(self, floor: int):
        self.current_floor = floor

    def get_direction(self):
        return self.current_to_move_direction
    
    def get_state(self):
        return self.state
    
    def get_current_floor(self):
        return self.current_floor
    
class ElevatorController:

    def __init__(self):
        self.state = ElevatorState()
        self.state.set_init_state()
        self.movement_stategy = LookStategy(self.state)

    def set_movement_stategy(self, stategy):
        self.movement_stategy = stategy


    def run(self):
        """
        to test the elevator controller and nothing else
        """
        while  True:
            floors, dirs = self.take_input()
            for i in range(len(floors)):
                self.movement_stategy.queue_request(floors[i], dirs[i])
            print("min heap", self.movement_stategy.min_heap)
            print("max heap", self.movement_stategy.max_heap)
            print("request queue", self.movement_stategy.request_set)
            next_stop, direction = self.movement_stategy.get_next_stop()
            print(next_stop, end= ", ")
            self.state.set_floor(next_stop)
    
    @staticmethod
    def take_input():
        """just a helper method for run"""
        floors = input("floor: ")
        dirs = None
        if floors == 'n':
            floors = []
            dirs = []
            return floors, dirs 
        else:
            dirs = input("dir: ")
        floors = [ int(floor.strip()) for floor in floors.split(",") ]
        dirs = [ dir.strip().lower()  for dir in dirs.split(",") ]
        return floors, dirs
    
    def queue_request(self, floor: int, dir: Direction):
        self.movement_stategy.queue_request(floor, dir)


class LookStategy:

    def __init__(self, elevator_state):
        self.min_heap = []
        self.max_heap = []
        self.request_set = set()
        self.elevator_state = elevator_state

    def queue_request(self, floor: int, direction: Direction):

        # if moving up and floor 
        if self.elevator_state.get_direction() == Direction.MOVING_UP:
            #  direction is up && floor above current floor,
            print("here", self.elevator_state.get_current_floor(), floor)
            if Direction(direction) == Direction.MOVING_UP and floor >= self.elevator_state.get_current_floor():
                heapq.heappush(self.min_heap, floor)
            # if moving up and floor is below current floor
            elif Direction(direction) == Direction.MOVING_UP and floor < self.elevator_state.get_current_floor():
                self.request_set.add((floor, direction))
            elif Direction(direction) == Direction.MOVING_DOWN:
                heapq.heappush(self.max_heap, (-1 * floor))
        elif self.elevator_state.get_direction() == Direction.MOVING_DOWN:
            #  direction is up && floor above current floor,
            if Direction(direction) == Direction.MOVING_DOWN and floor <= self.elevator_state.get_current_floor():
                heapq.heappush(self.max_heap, (-1 * floor))
            # if moving up and floor is below current floor
            elif Direction(direction) == Direction.MOVING_DOWN and floor > self.elevator_state.get_current_floor():
                self.request_set.add((floor, direction))
            elif Direction(direction) == Direction.MOVING_UP:
                heapq.heappush(self.min_heap, floor)
     
    def get_next_stop(self):
        if self.elevator_state.get_direction() == Direction.MOVING_UP and len(self.min_heap) > 0:
            next_stop = heapq.heappop(self.min_heap)
            if len(self.min_heap) == 0:
                self.populate_max_heap()
                if len(self.max_heap) > 0:
                    self.elevator_state.set_direction(Direction.MOVING_DOWN)
        elif self.elevator_state.get_direction() == Direction.MOVING_DOWN and len(self.max_heap) > 0:
            next_stop = -1 * heapq.heappop(self.max_heap)
            if len(self.max_heap) == 0:
                self.populate_min_heap()
                if len(self.min_heap) > 0:
                    self.elevator_state.set_direction(Direction.MOVING_UP)
        return next_stop, self.elevator_state.get_direction()
                
    def populate_min_heap(self):
        for floor, direction in self.request_set:
            heapq.heappush(self.min_heap, floor)
        self.request_set = set()

    def populate_max_heap(self):
        for floor, Direction in self.request_set:
            heapq.heappush(self.max_heap, (-1 * floor))
        self.request_set = set()

if __name__ == "__main__":
    elevator_controller = ElevatorController()
    elevator_controller.run()