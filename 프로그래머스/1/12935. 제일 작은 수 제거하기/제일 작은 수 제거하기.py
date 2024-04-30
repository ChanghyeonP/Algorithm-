def solution(arr):
    answer = []
    if arr[0] == 10:
        answer.append(-1)
    else :
        a = min(arr)
        arr.remove(a)
        answer = arr
    
    return answer