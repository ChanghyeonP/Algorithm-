def solution(x):
    answer = True
    a = list(str(x))
    a = [int(i) for i in a]
    a = sum(a)
    if  x % a == 0:
        answer = True
    else :
        answer = False
    return answer