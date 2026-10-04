sample1 = [1, 2, 3, 2, 3]
# [4, 3, 1, 1, 0]

sample2 = [5, 4, 3, 2, 1]
# [1, 1, 1, 1, 0]

sample3 = [1, 2, 3, 4, 5]
# [4, 3, 2, 1, 0]

sample4 = [3, 3, 3, 2]
# [3, 2, 1, 0]


def mysolution(prices):
    log = {}
    for i, p in enumerate(prices):
        if p not in log:
            log[p] = [i]
        else:
            log[p].append(i)

    sort_key = sorted(list(log.keys()))

    res = []
    for i in range(len(prices)):
        k = len(prices) - i - 1
        t = prices[i]

        for s in sort_key:
            if t == s:
                log[t] = log[t][1:]
                break

            if len(log[s]) == 0:
                continue

            buff = log[s][0] - i
            if buff < k:
                k = buff

        res.append(k)

    return res

from collections import deque

def solution(prices):
    res = []

    bound = prices[0]
    buff = deque()
    buff.append(0)
    for i in range(1, len(prices)):
        while prices[i] < bound:
            res.append(i - buff[0] - 1)
            buff.popleft()
            if len(buff) == 0:
                bound = prices[i]
            else:
                bound = prices[buff[0]]

        buff.append(i)

    for i in range(len(buff)):
        res.append(len(buff) - i - 1)

    return res

ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)