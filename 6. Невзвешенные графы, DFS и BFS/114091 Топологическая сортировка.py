import sys

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        m = int(data[1])
        edges = []
        idx = 2
        for _ in range(m):
            edges.append((int(data[idx]), int(data[idx+1])))
            idx += 2
        perm = [int(x) for x in data[idx:idx+n]]
        
        pos = [0] * (n + 1)
        for i, v in enumerate(perm):
            pos[v] = i
            
        ok = True
        for u, v in edges:
            if pos[u] >= pos[v]:
                ok = False
                break
        print("YES" if ok else "NO")
