import sys
import heapq

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        fish = [int(x) for x in input_data[1:n+1]]
        
        heap = []
        for i in range(n):
            period = max(1000 - fish[i], 1)
            heapq.heappush(heap, (period, i, fish[i]))
            
        pos = 0
        igor_time = 0
        while heap:
            t, idx, f = heapq.heappop(heap)
            travel = abs(pos - idx)
            if igor_time + travel > t:
                print(t)
                break
            igor_time = max(igor_time + travel, t)
            pos = idx
            new_f = f + 1
            new_p = max(1000 - new_f, 1)
            heapq.heappush(heap, (t + new_p, idx, new_f))
