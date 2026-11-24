import sys

def dfs(v, adj, visited):
    visited[v] = True
    count = 1
    for u in adj[v]:
        if not visited[u]:
            count += dfs(u, adj, visited)
    return count

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        m = int(data[1])
        if m != n - 1:
            print("NO")
        else:
            adj = [[] for _ in range(n + 1)]
            idx = 2
            for _ in range(m):
                u = int(data[idx])
                v = int(data[idx+1])
                idx += 2
                adj[u].append(v)
                adj[v].append(u)
            visited = [False] * (n + 1)
            if dfs(1, adj, visited) == n:
                print("YES")
            else:
                print("NO")
