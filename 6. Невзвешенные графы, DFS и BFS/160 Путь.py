import sys
from collections import deque

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        matrix = []
        idx = 1
        for _ in range(n):
            matrix.append([int(x) for x in data[idx:idx+n]])
            idx += n
        start = int(data[idx]) - 1
        end = int(data[idx+1]) - 1
        
        dist = [-1] * n
        parent = [-1] * n
        dist[start] = 0
        q = deque([start])
        
        while q:
            v = q.popleft()
            for u in range(n):
                if matrix[v][u] == 1 and dist[u] == -1:
                    dist[u] = dist[v] + 1
                    parent[u] = v
                    q.append(u)
                    
        if dist[end] == -1:
            print(-1)
        elif dist[end] == 0:
            print(0)
        else:
            print(dist[end])
            path = []
            curr = end
            while curr is not None and curr != -1:
                path.append(curr + 1)
                curr = parent[curr]
            path.reverse()
            print(*path)
