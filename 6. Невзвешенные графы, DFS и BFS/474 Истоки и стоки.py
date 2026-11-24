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
            
        sources = []
        sinks = []
        for i in range(n):
            if sum(matrix[j][i] for j in range(n)) == 0:
                sources.append(i + 1)
            if sum(matrix[i]) == 0:
                sinks.append(i + 1)
                
        print(len(sources))
        for s in sources:
            print(s)
        print(len(sinks))
        for s in sinks:
            print(s)
