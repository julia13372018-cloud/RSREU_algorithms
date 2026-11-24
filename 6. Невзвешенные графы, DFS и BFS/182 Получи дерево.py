import sys

def dfs(v, adj, visited, edges):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            edges.append((v, u))
            dfs(u, adj, visited, edges)

if __name__ == "__main__":
    it = iter(sys.stdin.read().split())
    n_str = next(it, None)
    if n_str is not None:
        n = int(n_str)
        m = int(next(it))
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * (n + 1)
        edges = []
        dfs(1, adj, visited, edges)
        for u, v in edges:
            print(u, v)
