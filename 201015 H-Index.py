"""
https://programmers.co.kr/learn/courses/30/lessons/42747

"""

citations = [3, 0, 6, 1, 5]


for h in range(10000):
    count = 0  # 인용된 횟수
    for i in range(len(citations)):
        if citations[i] >= h:
            count += 1
    if count < h:
        break

print(h-1)
