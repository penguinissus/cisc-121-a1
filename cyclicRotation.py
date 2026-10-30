def solution (A, K):
    for i in range(0, K):
        num = A[len(A)-1]
        # shift all elements to the right starting from the end
        for j in range(len(A)-1, 0, -1):
            A[j] = A[j-1]
        A[0] = num
    return A