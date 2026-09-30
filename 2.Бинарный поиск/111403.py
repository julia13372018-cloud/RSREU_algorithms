import sys
import math

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        c = float(input_data[0])
        left = 0.0
        right = 100000.0
        for _ in range(100):
            mid = (left + right) / 2
            if mid * mid + math.sqrt(mid) < c:
                left = mid
            else:
                right = mid
        print(f"{left:.6f}")
