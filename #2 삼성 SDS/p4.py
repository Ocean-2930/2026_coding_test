sample1 = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]
# 예상 결과: 9


sample2 = [
    [1, 100, 100, 100],
    [100, 1, 100, 100],
    [100, 100, 1, 100],
    [100, 100, 100, 1]
]
# 예상 결과: 4


sample3 = [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]
]
# 예상 결과: 15


sample4 = [
    [8, 6, 4, 7],
    [5, 9, 3, 8],
    [6, 7, 5, 4],
    [9, 2, 8, 6]
]
# 예상 결과: 15

def dfs(res, arr, buff):
    if len(arr) == 1:
        res.append(buff + [arr[0]])
    
    for i in range(len(arr)):
        nx = list(arr[0:i]) + list([] if i == (len(arr) - 1) else arr[i+1:len(arr)])

        dfs(res, nx, buff[:]+[arr[i]])



def solution(cost):
    tasks = []
    dfs(tasks, range(len(cost)), [])

    res = sum([sum(a) for a in cost])
    for t in tasks:
        s = 0
        for i in range(len(cost)):
            s += cost[i][t[i]]

        if s < res:
            res = s

    return res



ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)