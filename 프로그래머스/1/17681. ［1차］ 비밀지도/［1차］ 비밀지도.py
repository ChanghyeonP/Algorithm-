def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        binary_str1 = bin(arr1[i])[2:]
        binary_str2 = bin(arr2[i])[2:]

        binary_str1 = binary_str1.zfill(n)
        binary_str2 = binary_str2.zfill(n)

        # 리스트 컴프리헨션 및 zip을 사용하여 이진 표현을 결합
        result_str = ''.join(['#' if b1 == '1' or b2 == '1' else ' ' for b1, b2 in zip(binary_str1, binary_str2)])

        answer.append(result_str)

    return answer
