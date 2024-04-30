def solution(s, n):
    answer = ''
    for char in s:
        if char.isalpha():
            is_upper = char.isupper()
            # 알파벳을 n만큼 밀고, 범위를 벗어나면 조정
            new_char = chr((ord(char) - ord('A' if is_upper else 'a') + n) % 26 + ord('A' if is_upper else 'a'))
        else:
            new_char = char
        answer += new_char
    return answer