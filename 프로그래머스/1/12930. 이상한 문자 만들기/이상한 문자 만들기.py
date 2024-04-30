def solution(s):
    res=""
    ans = []
    for w in s.split(' ') : #단어 순회
        for i in range(len(w)): # 글자 순회
            if i % 2 == 0 : # 인덱스가 짝수
                res+=w[i].upper() #대문자로
            else : 
                res += w[i].lower()
        ans.append(res) #바뀐 단어 넣기
        res = "" #단어 초기화
    return ' '.join(ans) #공백 넣어 출력