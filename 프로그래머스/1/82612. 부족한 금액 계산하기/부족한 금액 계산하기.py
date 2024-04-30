def solution(price, money, count):
    answer = -1
    all_price = 0
    for i in range(0, count+1, 1):
        all_price += price * i
        
    all_price -= money
    answer = all_price
    answer = max(0, all_price)
    return answer