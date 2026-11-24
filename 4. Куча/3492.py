import sys
import heapq

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        heap = []
        idx = 0
        total_len = len(input_data)
        while idx < total_len:
            cmd = input_data[idx]
            if cmd == "CLEAR":
                heap = []
                idx += 1
            elif cmd == "ADD":
                val = int(input_data[idx+1])
                heapq.heappush(heap, -val)
                idx += 2
            elif cmd == "EXTRACT":
                if not heap:
                    print("CANNOT")
                else:
                    print(-heapq.heappop(heap))
                idx += 1
