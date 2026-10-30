def solution(A):
    length = []
    for i in range(1, len(A)):
        sumA = 0
        sumB = 0
        # get the sum of first half and second half seperately
        for j in range(0, i):
            sumA += A[j]
        for j in range(i, len(A)):
            sumB += A[j]
        difference = abs(sumA-sumB)
        length.append(difference)
    return min(length)
    pass