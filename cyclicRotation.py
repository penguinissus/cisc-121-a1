def solution (A, K):
    for i in range(1, K):
        num = A[len(A)-1]
        for j in range(len(A)-1, 0, -1):
            A[j] = A[j-1]
        A[0] = num
    return A