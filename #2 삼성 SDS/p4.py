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

"""
좋아. 이번에는 이전 문제들과 겹치지 않게 **선택 조합을 끝까지 탐색해야 하는 유형**으로 갈게. 풀이 힌트 없이 문제와 샘플만 줄게.

# 문제. 작업 배정

`N`명의 직원과 `N`개의 작업이 있다.

각 직원은 정확히 하나의 작업을 맡아야 하며, 각 작업 역시 정확히 한 명의 직원에게만 배정되어야 한다.

직원 `i`가 작업 `j`를 수행할 때 필요한 비용은 `cost[i][j]`로 주어진다.

모든 직원에게 서로 다른 작업을 하나씩 배정했을 때, 필요한 총 비용의 최솟값을 반환하라.

## 제한 조건

```text
1 <= N <= 10

1 <= cost[i][j] <= 1000
```

모든 직원은 반드시 하나의 작업을 맡아야 한다.

모든 작업은 정확히 한 번만 배정되어야 한다.

예를 들어 `N = 3`이라면 다음과 같은 배정은 가능하다.

```text
직원 0 -> 작업 2
직원 1 -> 작업 0
직원 2 -> 작업 1
```

하지만 다음 배정은 불가능하다.

```text
직원 0 -> 작업 1
직원 1 -> 작업 1
직원 2 -> 작업 2
```

작업 1이 두 명에게 중복 배정되었기 때문이다.

# 샘플 코드

```python
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


def solution(cost):
    pass


ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)
```

목표 출력:

```text
9
4
15
15
```
"""