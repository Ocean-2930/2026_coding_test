sample1 = [
    [70, 50, 80, 50],
    100
]
# 3

sample2 = [
    [70, 80, 50],
    100
]
# 3

sample3 = [
    [40, 40, 40, 40],
    80
]
# 2

sample4 = [
    [40, 50, 60, 70],
    100
]
# 3

def ride(people, limit, k):
    if len(people) == 0:
        return 0

    res = -1
    for i in range(len(people)):
        if k < people[i]:
            continue

        buff = ride(people[:i]+people[i+1:], limit, k-people[i])

        if res == -1:
            res = buff
        elif buff < res:
            res = buff

    if res == -1:
        return ride(people, limit, limit) + 1

    return res



def mysolution(people, limit):
    peo = [n for n in people]

    return ride(peo, limit, 0)

def solution(people, limit):
    length = len(people)
    peo = sorted([n for n in people])[::-1]
    flags = [False for _ in range(length)]

    res = 0
    for i in range(length):
        if flags[i]:
            continue

        flags[i] = True
        res += 1
        for j in range(1, length-i):
            if flags[i+j]:
                continue
            
            if peo[i] + peo[i+j] <= limit:
                flags[i+j] = True
                break

    return res



ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)

ans = solution(*sample4)
print(ans)