
def solution(X, Y, D):
    distance = Y-X
    jumps = distance//D
    # see if there is a remainder, if so we need to add one more jump
    if distance%jumps != 0:
        jumps += 1
    return jumps
    pass