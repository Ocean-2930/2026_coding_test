sample1 = [
    [1, 5, 2, 6, 3, 7, 4],
    [
        [2, 5, 3],
        [4, 4, 1],
        [1, 7, 3]
    ]
]
# [5, 6, 3]


def solution(array, commands):
    res = []

    for c in commands:
        sublist = array[c[0]-1:c[1]]
        sublist.sort()
        res.append(sublist[c[2]-1])

    return res


ans = solution(*sample1)
print(ans)