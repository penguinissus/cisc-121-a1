# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # length could be zero
    if(len(A)==0):
        return None
    num = 1
    # loop through each number starting from 1
    while True:
        if not(num in A):
            return num
        num+=1
    pass