sample1 = [10, 2]
# [4, 3]

sample2 = [8, 1]
# [3, 3]

sample3 = [24, 24]
# [8, 6]


def solution(brown, yellow):
    y = 1
    while y <= (yellow / y):
        x = yellow / y

        if x != int(x):
            y += 1
            continue

        x = int(x)
        if brown == (2 * (x + y) + 4):
            return [x + 2, y + 2]

        y += 1

    return None


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)