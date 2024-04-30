def solution(name, yearning, photo):
    memory_scores = []  # 각 사진의 기억 점수를 저장할 리스트
    
    for names_in_photo in photo:
        photo_score = 0  # 현재 사진의 기억 점수를 초기화
        
        # 현재 사진에 있는 각 사람에 대한 기억 점수를 계산하여 더함
        for person_name in names_in_photo:
            if person_name in name:  # 현재 사람이 기억하는 사람에 포함되어 있는 경우
                person_index = name.index(person_name)
                photo_score += yearning[person_index]
        
        memory_scores.append(photo_score)  # 현재 사진의 기억 점수를 리스트에 추가
    
    return memory_scores