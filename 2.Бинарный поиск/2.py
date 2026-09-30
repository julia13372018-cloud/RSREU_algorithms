import sys

def approximate_binary_search(A, target):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == target:
            return A[mid]
        elif A[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    if left >= len(A):
        return A[-1]
    if right < 0:
        return A[0]
        
    if abs(A[left] - target) < abs(A[right] - target):
        return A[left]
    else:
        return A[right]

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        k = int(input_data[1])
        A = [int(x) for x in input_data[2:n+2]]
        queries = [int(x) for x in input_data[n+2:n+2+k]]
        for q in queries:
            print(approximate_binary_search(A, q))
