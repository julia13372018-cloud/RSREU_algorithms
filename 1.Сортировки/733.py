import sys

def quicksort(A):
    if len(A) <= 1:
        return A
    pivot = A[len(A) // 2]
    left = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    right = [x for x in A if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    lines = sys.stdin.read().split()
    if lines:
        n = int(lines[0])
        A = [int(x) for x in lines[1:n+1]]
        print(*(quicksort(A)))
