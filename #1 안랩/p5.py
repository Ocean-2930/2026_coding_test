sample1 = [3, 0, 6, 1, 5]
# 3

sample2 = [10, 10, 10, 10]
# 4

sample3 = [0, 0, 0]
# 0

sample4 = [1, 1, 1, 1, 1]
# 1


def solution(citations):
    ls = sorted(citations)
    length = len(ls)

    for i in range(length):
        ind = length - i - 1

        if ls[ind] == i + 1:
            return ls[ind]
        elif ls[ind] < i + 1:
            return i
            
    return length

ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)