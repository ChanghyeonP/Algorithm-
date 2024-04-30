def solution(n):
    answer = list(str(n))
    for i in range(0, len(answer), 1):
        for j in range(0, len(answer)-1, 1):
            if answer[j] < answer[j+1] :
                answer[j] , answer[j+1] = answer[j+1], answer[j]
    
    return int(''.join(answer))