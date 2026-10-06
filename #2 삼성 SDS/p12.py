sample1 = [
    4,
    [
        [0, 1, 1],
        [0, 2, 4],
        [1, 2, 2],
        [1, 3, 5],
        [2, 3, 1]
    ]
]
# 예상 결과: 4


sample2 = [
    5,
    [
        [0, 1, 3],
        [0, 2, 2],
        [1, 2, 1],
        [1, 3, 4],
        [2, 3, 5],
        [2, 4, 6],
        [3, 4, 2]
    ]
]
# 예상 결과: 9


sample3 = [
    4,
    [
        [0, 1, 2],
        [2, 3, 3]
    ]
]
# 예상 결과: -1


sample4 = [
    1,
    []
]
# 예상 결과: 0


sample5 = [
    3,
    [
        [0, 1, 10],
        [0, 1, 3],
        [1, 2, 4],
        [0, 2, 20]
    ]
]
# 예상 결과: 7

import heapq

def findroot(roots, n):    
    if roots[n] == n:
        return n

    return findroot(roots, roots[n])

"""
def findroot(roots, x):
    if roots[x] != x:
        roots[x] = findroot(roots, roots[x])

    return roots[x]
"""

def solution(n, edges):
    network = n
    roots = list(range(n))

    q = []
    for e in edges:
        heapq.heappush(q, (e[2], e[0], e[1]))

    cost = 0
    while q:
        buff = heapq.heappop(q)

        r1 = findroot(roots, buff[1])
        r2 = findroot(roots, buff[2])

        if r1 != r2:
            cost += buff[0]
            roots[r1] = r2
            network -= 1

        if network == 1:
            break
    
    return cost if network == 1 else -1

"""
edges.sort(key=lambda x: x[2])
"""


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


"""
좋아. 이번에는 방금 익힌 연결 개념을 조금 확장한 문제로 가자. 풀이 힌트 없이 문제와 샘플만 줄게.

# 문제. 도시 전력망 구축

`N`개의 도시가 있다. 도시 번호는 `0`부터 `N-1`까지다.

현재 도시 사이에는 전력망이 전혀 설치되어 있지 않다.

설치 가능한 전력선의 정보가 `edges`로 주어진다.

```python
edges[i] = [a, b, cost]
```

이는 도시 `a`와 도시 `b`를 연결하는 전력선을 `cost`의 비용으로 설치할 수 있다는 의미다.

전력선은 양방향으로 연결된다.

## 목표

모든 도시가 하나의 전력망으로 연결되어야 한다.

두 도시가 직접 연결되어 있지 않더라도 다른 도시들을 거쳐 이동할 수 있다면 연결된 것으로 본다.

예를 들어

```text
0 - 1 - 2
```

라면 `0`과 `2`도 같은 전력망에 속한다.

모든 도시를 연결하기 위해 필요한 **최소 설치 비용**을 반환하라.

모든 도시를 하나의 전력망으로 연결하는 것이 불가능하다면 `-1`을 반환한다.

## 주의사항

모든 설치 가능한 전력선을 사용할 필요는 없다.

같은 두 도시 사이에 비용이 서로 다른 여러 전력선이 존재할 수도 있다.

전력선을 설치한 결과 순환 구조가 생겨도 규칙상 불가능한 것은 아니지만, 최종적으로 필요한 것은 전체 설치 비용의 최솟값이다.

## 제한 조건

```text
1 <= N <= 100000

0 <= edges의 개수 <= 200000

0 <= a, b < N
a != b

1 <= cost <= 1000000000
```

`N = 1`이면 설치해야 할 전력선이 없으므로 정답은 `0`이다.

# 샘플 코드

```python
sample1 = [
    4,
    [
        [0, 1, 1],
        [0, 2, 4],
        [1, 2, 2],
        [1, 3, 5],
        [2, 3, 1]
    ]
]
# 예상 결과: 4


sample2 = [
    5,
    [
        [0, 1, 3],
        [0, 2, 2],
        [1, 2, 1],
        [1, 3, 4],
        [2, 3, 5],
        [2, 4, 6],
        [3, 4, 2]
    ]
]
# 예상 결과: 9


sample3 = [
    4,
    [
        [0, 1, 2],
        [2, 3, 3]
    ]
]
# 예상 결과: -1


sample4 = [
    1,
    []
]
# 예상 결과: 0


sample5 = [
    3,
    [
        [0, 1, 10],
        [0, 1, 3],
        [1, 2, 4],
        [0, 2, 20]
    ]
]
# 예상 결과: 7


def solution(n, edges):
    pass


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
```

목표 출력:

```text
4
9
-1
0
7
```
"""