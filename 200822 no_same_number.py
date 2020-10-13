# 프로그래머스 코딩테스트 연습 - 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

arr1 = [1, 1, 3, 3, 0, 1, 1]
arr2 = [4, 4, 4, 3, 3]
answer = []

for i in range(len(arr2)):
    if i == 0:
        answer.append(arr2[i])
    elif arr2[i-1] != arr2[i]:
        answer.append(arr2[i])

print(answer)