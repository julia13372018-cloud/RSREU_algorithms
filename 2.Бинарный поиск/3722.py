import sys

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        a = int(input_data[0])
        b = int(input_data[1])
        c = int(input_data[2])
        d = int(input_data[3])
        
        left = -2000.0
        right = 2000.0
        f_left = a * (left**3) + b * (left**2) + c * left + d
        
        for _ in range(100):
            mid = (left + right) / 2
            f_mid = a * (mid**3) + b * (mid**2) + c * mid + d
            if (f_mid > 0 and f_left > 0) or (f_mid < 0 and f_left < 0):
                left = mid
            else:
                right = mid
        print(f"{left:.6f}")
