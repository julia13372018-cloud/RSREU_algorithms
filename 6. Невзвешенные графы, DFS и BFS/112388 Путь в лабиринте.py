import sys
from collections import deque

if __name__ == "__main__":
    it = iter(sys.stdin.read().split())
    n_str = next(it, None)
    if n_str is not None:
        n = int(n_str)
        m = int(next(it))
        grid = [[int(next(it)) for _ in range(m)] for _ in range(n)]
        dist = [[-1] * m for _ in range(n)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            if x == n - 1 and y == m - 1:
                break
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        print(dist[n - 1][m - 1])
