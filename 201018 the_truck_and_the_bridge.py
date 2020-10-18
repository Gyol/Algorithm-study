"""
https://programmers.co.kr/learn/courses/30/lessons/42583
10테케중 4테케 시간초과 실패
느린 대신 차근차근 푸는 코드!
나중에 다시 풀어보쟝
"""


tick = 0
trucks1 = [7, 4, 5, 6]
trucks2 = [10]
trucks3 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
bridge = []

# 이번에 bridge로 보낼 truck순서
# bridge[0]에 진입을 시켰으면 truck_index = 1
truck_index = 0

bridge_length1 = 2
bridge_length2 = 100
bridge_length3 = 100
weight1 = 10
weight2 = 100
weight3 = 100

for i in range(bridge_length2):
    bridge.append(0)

while True:
    tick += 1

    for i in range(len(bridge)):
        bridge[len(bridge) - i - 1] = bridge[len(bridge) - 1 - i - 1]
    bridge[0] = 0

    if len(trucks3) > truck_index and weight3 >= sum(bridge) + trucks3[truck_index]:
        bridge[0] = trucks3[truck_index]
        truck_index += 1

    if truck_index == len(trucks3) and sum(bridge) == 0:
        break

print(tick)
