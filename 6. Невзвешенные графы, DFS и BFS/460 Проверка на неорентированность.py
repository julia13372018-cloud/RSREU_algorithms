import sys

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if data:
        n = int(data[0])
        matrix = []
        idx = 1
        for _ in range(n):
            matrix.append([int(x) for x in data[idx:idx+n]])
            idx += n
        
        ok = True
        for i in range(n):
            if matrix[i][i] != 0:
                ok = False
            for j in range(n):
                if matrix[i][j] != matrix[j][i]:
                    ok = False
        print("YES" if ok else "NO")
