def solution(a, b, n):
    answer = 0
    for i in range(n):
        remain = n % a 
        n = (n // a) *b
        answer += n
        n += remain
    return answer