sample1 = [
    [1, 4, 7, 10],
    12
]
# 예상 결과: 11


sample2 = [
    [-5, -2, 3, 8, 12],
    1
]
# 예상 결과: 1


sample3 = [
    [5, 5, 5, 5],
    9
]
# 예상 결과: 10


sample4 = [
    [-10, -4, 1, 6, 9],
    4
]
# 예상 결과: 5


sample5 = [
    [1, 2, 8, 9],
    10
]
# 예상 결과: 10


def solution(arr, target):
    sarr = sorted(arr)

    low = 0
    high = len(arr) - 1
    highres = sarr[low] + sarr[high]
    highscore = abs(highres - target)

    while low < high:
        res = sarr[low] + sarr[high]
        score = abs(res - target)

        if score == 0:
            return res

        if score < highscore:
            highres = res
            highscore = score

        if score == highscore and res < highres:
            highres = res

        if res < target:
            low += 1

        if target < res:
            high -= 1

    return highres


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)

ans = solution(*sample4)
print(ans)

ans = solution(*sample5)
print(ans)