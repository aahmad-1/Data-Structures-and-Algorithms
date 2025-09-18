def split(A):
    n = len(A)
    if n <= 1:
        return 0

    left_max = [0] * n
    left_max[0] = A[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], A[i])

    right_min = [0] * n
    right_min[n-1] = A[n-1]
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], A[i])

    count = 0
    for i in range(n-1):
        if left_max[i] < right_min[i+1]:
            count += 1

    return count

if __name__ == "__main__":
    print(split([1, 2, 3, 4, 5]))
    print(split([5, 4, 3, 2, 1]))
    print(split([2, 1, 2, 5, 7, 6, 9]))
    print(split([1, 2, 3, 1]))