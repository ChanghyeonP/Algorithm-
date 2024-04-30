def solution(n):
    answer = 0
    original_n = n
    one_count = lambda x: bin(x).count('1')

    while True:
        n += 1
        if one_count(n) == one_count(original_n):
            return n