import sys

def dfs(v, matrix, color):
    color[v] = 1
    for u in range(len(matrix)):
        if matrix[v][u] == 1:
            if color[u] == 1:
                return True
            if color[u] == 0 and dfs(u, matrix, color):
                return True
    color[v] = 2
    return False

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        matrix = []
        idx = 1
        for _ in range(n):
            matrix.append([int(x) for x in data[idx:idx+n]])
            idx += n
        color = [0] * n
        has_cycle = False
        for i in range(n):
            if color[i] == 0:
                if dfs(i, matrix, color):
                    has_cycle = True
                    break
        print(1 if has_cycle else 0)
