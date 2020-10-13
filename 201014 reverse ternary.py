"""
문제 설명
자연수 n이 매개변수로 주어집니다.
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록
solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.
"""

number = 45
ternary = []
decimal = []

while number / 3 > 0:
    ternary.append(number % 3)
    number = number//3

for i in range(len(ternary)):
    decimal.append((3**(len(ternary)-i-1))*ternary[i])

print(sum(decimal))
