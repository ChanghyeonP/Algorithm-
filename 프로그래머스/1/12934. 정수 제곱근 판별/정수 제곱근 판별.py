import math
def solution(n):
    answer = 0
    n = math.sqrt(n)
    if n == int(n) :
        answer = math.pow(n+1, 2)
    else :
        return -1
    return answer