import sys
import heapq
from collections import deque

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        k = int(input_data[1])
        p = int(input_data[2])
        requests = [int(x) for x in input_data[3:3+p]]
        
        car_positions = {i: deque() for i in range(1, n + 1)}
        for idx, car in enumerate(requests):
            car_positions[car].append(idx)
            
        floor = set()
        heap = []
        operations = 0
        inf_prio = 1000000
        
        for i, car in enumerate(requests):
            car_positions[car].popleft()
            
            if car in floor:
                if car_positions[car]:
                    next_idx = car_positions[car][0]
                else:
                    inf_prio += 1
                    next_idx = inf_prio
                heapq.heappush(heap, (-next_idx, car))
                continue
                
            if len(floor) < k:
                floor.add(car)
                operations += 1
            else:
                while heap:
                    neg_prio, removed_car = heapq.heappop(heap)
                    if removed_car in floor:
                        if car_positions[removed_car]:
                            actual_next = car_positions[removed_car][0]
                            if -neg_prio == actual_next:
                                floor.remove(removed_car)
                                break
                        else:
                            if -neg_prio > 1000000:
                                floor.remove(removed_car)
                                break
                floor.add(car)
                operations += 1
                
            if car_positions[car]:
                next_idx = car_positions[car][0]
            else:
                inf_prio += 1
                next_idx = inf_prio
            heapq.heappush(heap, (-next_idx, car))
            
        print(operations)
