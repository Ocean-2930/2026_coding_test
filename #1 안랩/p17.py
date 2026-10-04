sample1 = [
    3,
    [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
]
# 2

sample2 = [
    3,
    [
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1]
    ]
]
# 1

sample3 = [
    5,
    [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1]
    ]
]
# 3

from collections import deque

def solution(n, computers):
    log = {}

    for i in range(n):
        log[i] = False

    res = 0
    q = deque()
    for i in range(n):
        if log[i]:
            continue

        res += 1

        q.append(i)
        while 0 < len(q):
            t = q.popleft()

            log[t] = True

            for j in range(n):
                if j == t:
                    continue

                if computers[t][j] != 1:
                    continue

                if log[j]:
                    continue
                
                q.append(j)

    return res


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)