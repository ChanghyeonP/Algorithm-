def solution(num):
    answer = 0
    con = 0
    while num != 1:  
        if num % 2 == 0:
            num = num // 2 
        elif num % 2 == 1:
            num = num * 3 + 1
        con += 1
    if con >= 500 :
        return -1
    answer = con
    return answer