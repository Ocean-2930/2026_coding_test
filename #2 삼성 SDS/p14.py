sample1 = [
    4,
    [
        [0, 2],
        [1, 2],
        [2, 3]
    ]
]
# 예상 결과: [0, 1, 2, 3]


sample2 = [
    5,
    [
        [0, 3],
        [1, 3],
        [1, 4],
        [2, 4]
    ]
]
# 예상 결과: [0, 1, 2, 3, 4]


sample3 = [
    3,
    [
        [0, 1],
        [1, 2],
        [2, 0]
    ]
]
# 예상 결과: []


sample4 = [
    6,
    [
        [2, 5],
        [0, 4],
        [1, 4],
        [4, 5]
    ]
]
# 예상 결과: [0, 1, 2, 3, 4, 5]


sample5 = [
    4,
    []
]
# 예상 결과: [0, 1, 2, 3]


import heapq


def solution(n, conditions):
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    # a -> b
    # a를 끝내야 b를 할 수 있음
    for a, b in conditions:
        graph[a].append(b)
        indegree[b] += 1

    # 현재 바로 수행 가능한 공정들
    q = []

    for i in range(n):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    res = []

    while q:
        current = heapq.heappop(q)
        res.append(current)

        # current를 완료했으므로
        # current를 선행 조건으로 가지는 공정들의
        # 남은 선행 조건 개수를 하나 줄임
        for nxt in graph[current]:
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                heapq.heappush(q, nxt)

    # 모든 공정을 처리하지 못했다면 사이클 존재
    if len(res) != n:
        return []

    return res


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
좋아. 이번에는 **그래프의 선후관계 처리**가 핵심인 문제로 가자. 풀이 힌트 없이 문제와 샘플만 줄게.

# 문제. 공정 순서 결정

`N`개의 공정이 있다.

각 공정은 `0`번부터 `N-1`번까지 번호가 매겨져 있다.

일부 공정에는 선행 공정 조건이 있다.

예를 들어

```python
[2, 5]
```

라는 조건은

```text
2번 공정을 완료한 뒤에만 5번 공정을 시작할 수 있다.
```

는 의미다.

모든 공정을 한 번씩 수행하려고 한다.

동시에 여러 공정을 수행할 수는 없으며, 한 번에 하나의 공정만 수행한다.

---

## 공정 선택 규칙

현재 수행 가능한 공정이 여러 개라면 **공정 번호가 가장 작은 공정**을 먼저 수행한다.

어떤 공정이 수행 가능하려면 해당 공정의 모든 선행 공정이 이미 완료되어 있어야 한다.

---

## 반환값

모든 공정을 수행할 수 있다면 실제 수행한 공정 번호를 순서대로 배열에 담아 반환하라.

선행 조건 때문에 모든 공정을 수행하는 것이 불가능하다면 빈 배열 `[]`을 반환하라.

---

## 제한 조건

```text
1 <= N <= 100000

0 <= conditions의 길이 <= 200000

conditions[i] = [a, b]

0 <= a, b < N
a != b
```

같은 선행 조건이 중복으로 주어지지는 않는다.

모든 공정이 반드시 하나 이상의 선행 조건을 가지는 것은 아니다.

---

# 예시

다음과 같은 조건이 있다고 하자.

```text
0 → 2
1 → 2
2 → 3
```

처음에는 `0`, `1`을 수행할 수 있다.

번호가 작은 공정을 먼저 수행하므로:

```text
0
```

을 먼저 수행한다.

그 다음에는 여전히 `1`이 수행 가능하므로:

```text
1
```

을 수행한다.

이제 `2`의 모든 선행 공정이 완료되었으므로 `2`를 수행할 수 있다.

최종 순서는:

```python
[0, 1, 2, 3]
```

이 된다.

---

# 샘플 코드

```python
sample1 = [
    4,
    [
        [0, 2],
        [1, 2],
        [2, 3]
    ]
]
# 예상 결과: [0, 1, 2, 3]


sample2 = [
    5,
    [
        [0, 3],
        [1, 3],
        [1, 4],
        [2, 4]
    ]
]
# 예상 결과: [0, 1, 2, 3, 4]


sample3 = [
    3,
    [
        [0, 1],
        [1, 2],
        [2, 0]
    ]
]
# 예상 결과: []


sample4 = [
    6,
    [
        [2, 5],
        [0, 4],
        [1, 4],
        [4, 5]
    ]
]
# 예상 결과: [0, 1, 2, 3, 4, 5]


sample5 = [
    4,
    []
]
# 예상 결과: [0, 1, 2, 3]


def solution(n, conditions):
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
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3]
```
"""