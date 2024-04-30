def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(signs), 1):
        if not signs[i]:
            absolutes[i] *= -1
    answer = sum(absolutes)
    return answer