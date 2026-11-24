import sys
import heapq

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        A = [int(x) for x in input_data[1:n+1]]
        heapq.heapify(A)
        
        total_cost = 0
        while len(A) > 1:
            first = heapq.heappop(A)
            second = heapq.heappop(A)
            new_val = first + second
            total_cost += new_val * 0.05
            heapq.heappush(A, new_val)
            
        print(f"{total_cost:.2f}")
