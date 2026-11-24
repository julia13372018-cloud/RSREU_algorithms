import sys

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        events = []
        idx = 1
        for _ in range(n):
            t = int(input_data[idx])
            l = int(input_data[idx+1])
            events.append((t, 1))
            events.append((t + l, -1))
            idx += 2
        events.sort(key=lambda x: (x[0], x[1]))
        
        max_apps = 0
        current = 0
        for time, type_ev in events:
            current += type_ev
            if current > max_apps:
                max_apps = current
        print(max_apps)
