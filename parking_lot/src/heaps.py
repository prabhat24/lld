import heapq

class heaps:
    def __init__(self):
        self.__heaps = {}

    def get_heaps(self):
        return self.__heaps
        

class ElevatorHeaps(heaps):
    
    def push(self, parking_spot):
        if parking_spot.distance_from_elevator:
            for elevaor_id, distance_from_elevator in parking_spot.distance_from_elevator.items():
                heap = self.__heaps[elevaor_id]
                heapq.heappush(heap, distance_from_elevator)

    def pop(self, elevator_id):
        heap = self.__heap.get(elevator_id)
        if heap:
            return heapq.heappop(heap)
        return None


class EntranceHeaps(heaps):

    def push(self, parking_spot):
        if parking_spot.distance_from_entrance:
            for elevaor_id, distance_from_entrance in parking_spot.distance_from_entrance.items():
                heap = self.__heaps[elevaor_id]
                heapq.heappush(heap, (distance_from_entrance, parking_spot))

    def pop(self, entrance_id):
        heap = self.__heap.get(entrance_id)
        if heap:
            return heapq.heappop(heap)
        return None
    