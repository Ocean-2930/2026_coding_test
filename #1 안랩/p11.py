sample1 = [
    80,
    [
        [80, 20],
        [50, 40],
        [30, 10]
    ]
]
# 3

sample2 = [
    40,
    [
        [40, 20],
        [30, 10],
        [20, 20]
    ]
]
# 2

sample3 = [
    10,
    [
        [20, 5],
        [10, 10]
    ]
]
# 1

def solution(k, dungeons):
    res = 0
    for i in range(len(dungeons)):
        if k < dungeons[i][0]:
            continue

        sub = solution(k-dungeons[i][1], dungeons[:i] + dungeons[i+1:])

        if res < sub + 1:
            res = sub + 1

    return res


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)