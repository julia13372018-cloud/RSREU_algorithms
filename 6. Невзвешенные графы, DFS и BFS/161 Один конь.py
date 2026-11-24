import sys
from collections import deque

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        n, x1, y1, x2, y2 = map(int, data[:5])
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        dist = [[-1] * (n + 1) for _ in range(n + 1)]
        parent = [[None] * (n + 1) for _ in range(n + 1)]
        
        dist[x1][y1] = 0
        q = deque([(x1, y1)])
        
        while q:
            x, y = q.popleft()
            if (x, y) == (x2, y2):
                break
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 1 <= nx <= n and 1 <= ny <= n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    parent[nx][ny] = (x, y)
                    q.append((nx, ny))
                    
        print(dist[x2][y2])
        path = []
        curr = (x2, y2)
        while curr is not None:
            path.append(curr)
            curr = parent[curr[0]][curr[1]]
        for px, py in reversed(path):
            print(px, py)
