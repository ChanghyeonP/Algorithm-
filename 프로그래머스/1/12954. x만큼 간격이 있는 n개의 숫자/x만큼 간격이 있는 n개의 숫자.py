def solution(x, n):
    answer = []
    a = 0
    for i in range(0, n):
        a = a + x
        answer.append(a)
    return answer