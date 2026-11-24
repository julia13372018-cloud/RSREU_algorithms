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
            for dx, dy in dirs:
                nx, ny = x, y
                while 0 <= nx + dx < n and 0 <= ny + dy < m and grid[nx + dx][ny + dy] != 1:
                    nx += dx
                    ny += dy
                    if grid[nx][ny] == 2:
                        print(dist[x][y] + 1)
                        sys.exit(0)
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
