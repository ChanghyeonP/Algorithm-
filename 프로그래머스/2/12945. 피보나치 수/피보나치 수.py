def solution(n):
    answer = [0,1]			# F(0)=0, F(1)=1
    for i in range(2,n+1):
        answer.append((answer[i-1] + answer[i-2]) % 1234567)
    
    return answer[-1]	