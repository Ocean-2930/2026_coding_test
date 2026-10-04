sample1 = [
    [93, 30, 55],
    [1, 30, 5]
]
# [2, 1]

sample2 = [
    [95, 90, 99, 99, 80, 99],
    [1, 1, 1, 1, 1, 1]
]
# [1, 3, 2]


def solution(progresses, speeds):
    res = [0]
    days = []

    if len(progresses) == 0:
            return res

    for i in range(len(progresses)):
        k = (100-progresses[i]) / speeds[i]
        k = int(k) + (1 if 0 < (k-int(k)) else 0)

        days.append(k)

    flag = days[0]
    res = [1]
    for i in range(1, len(days)):
        if days[i] <= flag:
            res[-1] += 1
        else:
            flag = days[i]
            res.append(1)

    return res


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)