# 프로그래머스 코딩테스트 연습 - 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584
# 정확성 통과, 효율성 탈락

prices = [1, 2, 3, 2, 3, 0, 3, 4, 3, 2, 1]
answer = []
length = len(prices)-1
for i in prices:
    for idx, j in enumerate(prices[1:], start=1):
        if i > j:
            answer.append(idx)
            break
        elif i == min(prices):
            answer.append(length)
            break
        else:
            continue
    length = length - 1
    prices = prices[1:]
answer.append(0)
print(answer)