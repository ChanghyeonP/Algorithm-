def solution(a, b, g, s, w, t):
    start = 0
    answer = end = (10**9) * (10**5) * 4
    
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0
        
        for gold_weight, silver_weight, weight, time_taken in zip(g, s, w, t):
            move_count = mid // (time_taken * 2)
            if mid % (time_taken * 2) >= time_taken:
                move_count += 1
                
            possible_move_weight = move_count * weight
            
            gold += gold_weight if (gold_weight < possible_move_weight) else (possible_move_weight)
            silver += silver_weight if (silver_weight < possible_move_weight) else (possible_move_weight)
            total += gold_weight + silver_weight if (gold_weight + silver_weight < possible_move_weight) else (possible_move_weight)
        
        if total >= a + b and gold >= a and silver >= b:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
            
    return answer
