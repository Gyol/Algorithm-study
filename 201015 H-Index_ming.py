def solution(citations):
    for h in range(10000):
        cit = 0
        for i in range(len(citations)):
            if h <= citations[i]:
                cit += 1
        if h > cit:
            break
    return h - 1