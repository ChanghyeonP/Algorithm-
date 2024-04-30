def solution(A, B):
    A.sort()
    B.sort(reverse=True)  # B 배열은 내림차순으로 정렬

    result = 0
    for a, b in zip(A, B):
        result += a * b

    return result