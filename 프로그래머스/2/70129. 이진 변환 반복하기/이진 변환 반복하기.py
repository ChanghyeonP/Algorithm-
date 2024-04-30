def solution(s):
    answer = []
    zero_count = 0
    count = 0
    
    while True:
        if s == '1':
            break;
        zero_count += s.count('0')
        s = s.replace('0','')
        s = format(len(s), 'b')
        
        count +=1
    answer = [count, zero_count]
    return answer