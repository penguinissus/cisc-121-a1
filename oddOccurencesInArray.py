def solution(A):
    for i in range(0, len(A)):
        foundPair = False
        for j in range(i+1, len(A)):
            # print(i, j)
            if A[i] == A[j]:
                foundPair = True
                A[j] = -1
        if not(foundPair):
            return A[i]
    pass