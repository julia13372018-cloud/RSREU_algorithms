import sys

def dfs(v, adj, visited):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            dfs(u, adj, visited)

if __name__ == "__main__":
    it = iter(sys.stdin.read().split())
    n_str = next(it, None)
    if n_str is not None:
        n = int(n_str)
        adj = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            box = int(next(it))
            adj[i].append(box)
            adj[box].append(i)
        visited = [False] * (n + 1)
        components = 0
        for i in range(1, n + 1):
            if not visited[i]:
                components += 1
                dfs(i, adj, visited)
        print(components)
