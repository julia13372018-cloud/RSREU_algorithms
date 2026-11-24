import sys

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        m = int(data[1])
        adj = [[] for _ in range(n + 1)]
        idx = 2
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            idx += 2
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * (n + 1)
        components = []
        for i in range(1, n + 1):
            if not visited[i]:
                comp = []
                stack = [i]
                visited[i] = True
                while stack:
                    v = stack.pop()
                    comp.append(v)
                    for u in adj[v]:
                        if not visited[u]:
                            visited[u] = True
                            stack.append(u)
                components.append(comp)
                
        out = [str(len(components))]
        for comp in components:
            out.append(str(len(comp)))
            out.append(" ".join(map(str, comp)))
        sys.stdout.write("\n".join(out) + "\n")
