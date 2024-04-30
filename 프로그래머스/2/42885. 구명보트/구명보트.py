def solution(people, limit):
    #answer = 0
    #count = 0
    #people = sorted(people)
    #i, j = 0, len(people) - 1
    
    #while i <= j:
    #    if people[i] + people[j] <= limit:
    #        i += 1
    #        j -=j
    #    else:
    #        j -= 1
    #    answer += 1
    #return answer
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer