def solution(s):
    answer = ''
    num_to_word = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    current_word = ''
    for char in s:
        if char.isalpha():
            current_word += char
            if current_word in num_to_word:
                answer += num_to_word[current_word]
                current_word = ''
        else:
            answer += char
            
    return int(answer)