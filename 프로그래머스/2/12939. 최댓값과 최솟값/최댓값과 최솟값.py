def solution(s):
    numbers = list(map(int, s.split()))

    min_value = min(numbers)
    max_value = max(numbers)

    result = f"{min_value} {max_value}"

    return result