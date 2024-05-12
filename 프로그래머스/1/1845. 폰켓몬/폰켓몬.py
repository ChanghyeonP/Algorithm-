def solution(nums):
    answer = 0
    choose = len(nums) / 2
    temp = set(nums)
    listlen = len(temp)
    if choose < listlen:
        answer = choose
    else :
        answer = listlen
    return answer
    
        
    