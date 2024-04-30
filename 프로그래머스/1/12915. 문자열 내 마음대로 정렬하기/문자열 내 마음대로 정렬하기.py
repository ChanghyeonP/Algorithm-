def solution(strings, n):
    strings = sorted(strings)
    strings.sort(key = lambda x : x[n])
    answer = strings
    return answer
