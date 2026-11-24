import sys

def sift_down(A, n, i):
    while 2 * i + 1 < n:
        left = 2 * i + 1
        right = 2 * i + 2
        j = left
        if right < n and A[right] > A[left]:
            j = right
        if A[i] >= A[j]:
            break
        A[i], A[j] = A[j], A[i]
        i = j

def heap_sort(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(A, n, i)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        sift_down(A, i, 0)

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        A = [int(x) for x in input_data[1:n+1]]
        heap_sort(A)
        print(*(A))
