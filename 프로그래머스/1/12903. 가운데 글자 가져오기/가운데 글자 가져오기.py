def solution(s):
    answer = ''
    s = list(str(s))
    if len(s) % 2 == 0:
        answer += s[len(s)//2 - 1] + s[len(s)//2]
    elif len(s) % 2 == 1:
        answer += s[len(s)//2]
    return answer
