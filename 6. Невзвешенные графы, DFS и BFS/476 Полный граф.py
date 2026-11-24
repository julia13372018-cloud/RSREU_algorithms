import sys

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        m = int(data[1])
        edges = set()
        idx = 2
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            idx += 2
            if u != v:
                edges.add((min(u, v), max(u, v)))
                
        if len(edges) == n * (n - 1) // 2:
            print("YES")
        else:
            print("NO")
