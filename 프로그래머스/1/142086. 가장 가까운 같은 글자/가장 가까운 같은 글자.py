def solution(s):
    answer = []
    word_list = {}
    for i, word in enumerate(s):
        if word not in word_list:
            answer.append(-1)
            word_list[word] = i
        else:
            answer.append(i - word_list[word])
            word_list[word] = i
    return answer