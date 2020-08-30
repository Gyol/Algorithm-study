words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
begin = 'hit'
target = 'cog'

words.insert(0, begin)
# print(words)

array = [[0 for col in range(len(words))]\
         for row in range(len(words))]

for j in range(len(words)):
    for k in range(len(words)):
        temp = 0
        for i in range(len(begin)):
            if words[j][i] == words[k][i]:
                continue
            else:
                temp = temp+1
            # print(temp)
        if temp == 1:
            array[j][k] = 1
        else:
            array[j][k] = 0
# print(array)


travel = []
travel.append([0, 0])
# print(travel)

didyou = []

for i in words:
    didyou.append(0)
# print(didyou)
didyou[0] = 1

now_word = 0

while len(travel) != now_word:
    for i in range(len(words)):
        if didyou[i] == 0:
            if array[travel[now_word][0]][i] == 1:
                travel.append([i, travel[now_word][1]+1])
                didyou[i] = 1
    now_word = now_word+1
    if words[travel[now_word][0]] == target:
        break
print(travel[now_word][1])
