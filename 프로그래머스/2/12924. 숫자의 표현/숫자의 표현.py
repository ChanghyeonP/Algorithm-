def solution(n):
    answer = 0
    
    for start in range(1, n+1):
        current_sum = 0
        i = start
        
        while current_sum < n:
            current_sum += i
            i += 1
        
        if current_sum == n:
            answer += 1
            
    return answer