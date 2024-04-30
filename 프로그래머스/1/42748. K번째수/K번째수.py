def solution(array, commands):
    answer = []
    
    for command in commands:
        start_idx, end_idx, target_idx = command
        sub_array = array[start_idx - 1:end_idx]
        sub_array.sort()
        answer.append(sub_array[target_idx - 1])

    return answer