sample1 = [
    [1, 1, 1, 1, 1],
    3
]
# 5

sample2 = [
    [4, 1, 2, 1],
    4
]
# 2

sample3 = [
    [1, 2, 3],
    0
]
# 2


def solution(numbers, target):
    num = [n for n in numbers]

    k = len(numbers)

    res = 0
    for i in range(2**k):
        grid = [-1 for _ in range(k)]
        flag = 0
        rem = i
        while 0 < rem:
            if rem % 2 == 1:
                grid[flag] = 1

            flag += 1
            rem = rem // 2

        total = 0
        for j in range(k):
            total += grid[j] * num[j]

        if total == target:
            res += 1

    return res


    


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)