import sys

sys.setrecursionlimit(10000)

def dfs(v, matrix, visited):
    visited[v] = True
    count = 1
    for i in range(len(matrix)):
        if matrix[v][i] == 1 and not visited[i]:
            count += dfs(i, matrix, visited)
    return count

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        s = int(data[1]) - 1
        matrix = []
        idx = 2
        for _ in range(n):
            matrix.append([int(x) for x in data[idx:idx+n]])
            idx += n
        visited = [False] * n
        print(dfs(s, matrix, visited))
