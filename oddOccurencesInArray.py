def solution(A):
    # loop through each element
    for i in range(0, len(A)):
        foundPair = False
        # loop to find if there is a pair for the current element
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                foundPair = True
                A[j] = -1 # since they specified elements are only above 0
        if not(foundPair):
            return A[i]
    pass