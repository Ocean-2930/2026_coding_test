sample1 = [
    4,
    [
        [0, 1, 8],
        [1, 3, 8],
        [0, 2, 3],
        [2, 3, 20]
    ]
]
# 예상 결과: 10


sample2 = [
    5,
    [
        [0, 1, 10],
        [1, 2, 10],
        [2, 4, 10],
        [0, 3, 100],
        [3, 4, 1]
    ]
]
# 예상 결과: 15


sample3 = [
    3,
    [
        [0, 1, 5]
    ]
]
# 예상 결과: -1


sample4 = [
    2,
    [
        [0, 1, 7]
    ]
]
# 예상 결과: 3


sample5 = [
    4,
    [
        [0, 1, 4],
        [1, 2, 4],
        [2, 3, 4],
        [0, 3, 20]
    ]
]
# 예상 결과: 10

import heapq


def solution(n, roads):
    # 인접 리스트 만들기
    graph = [[] for _ in range(n)]

    for a, b, cost in roads:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    INF = float('inf')

    # dist[node][0] : 할인권을 아직 안 쓰고 node에 도착한 최소 비용
    # dist[node][1] : 할인권을 이미 쓰고 node에 도착한 최소 비용
    dist = [[INF, INF] for _ in range(n)]

    dist[0][0] = 0

    # (현재까지 비용, 현재 도시, 할인권 사용 여부)
    q = []
    heapq.heappush(q, (0, 0, 0))

    while q:
        cost, node, used = heapq.heappop(q)

        # 이미 더 싼 경로가 발견된 상태라면 무시
        if dist[node][used] < cost:
            continue

        for next_node, road_cost in graph[node]:

            # 1. 할인권을 사용하지 않고 이동
            next_cost = cost + road_cost

            if next_cost < dist[next_node][used]:
                dist[next_node][used] = next_cost
                heapq.heappush(
                    q,
                    (next_cost, next_node, used)
                )

            # 2. 아직 할인권을 안 썼다면
            # 이번 도로에서 할인권 사용
            if used == 0:
                discount_cost = cost + road_cost // 2

                if discount_cost < dist[next_node][1]:
                    dist[next_node][1] = discount_cost
                    heapq.heappush(
                        q,
                        (discount_cost, next_node, 1)
                    )

    answer = min(
        dist[n - 1][0],
        dist[n - 1][1]
    )

    if answer == INF:
        return -1

    return answer


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
좋아. 이번에는 **다익스트라를 한 단계 확장한 상태 기반 최단거리 문제**로 가자. 풀이 힌트 없이 문제와 샘플만 줄게.

# 문제. 할인권이 있는 도로

`N`개의 도시와 `M`개의 양방향 도로가 있다.

도시는 `0`번부터 `N-1`번까지 번호가 매겨져 있다.

각 도로는 다음과 같이 주어진다.

```python
[a, b, cost]
```

도시 `a`와 `b` 사이를 이동할 때 비용 `cost`가 든다는 의미다.

당신은 도시 `0`에서 도시 `N-1`까지 이동하려고 한다.

단, 여행 중 **딱 한 번**, 원하는 도로 하나에 대해 비용을 절반만 낼 수 있는 할인권을 사용할 수 있다.

도로 비용이 홀수라면 할인 후 비용은 정수 나눗셈으로 계산한다.

예를 들어 비용이 `7`이라면 할인 후 비용은 `3`이다.

할인권은 사용하지 않아도 된다.

## 반환값

도시 `0`에서 도시 `N-1`까지 이동하는 최소 비용을 반환하라.

도착할 수 없다면 `-1`을 반환한다.

## 제한 조건

```text
2 <= N <= 100000
1 <= M <= 200000

1 <= cost <= 1000000000

0 <= a, b < N
a != b
```

같은 두 도시 사이에 여러 도로가 존재할 수 있다.

그래프는 반드시 연결되어 있다고 보장되지 않는다.

## 샘플 코드

```python
sample1 = [
    4,
    [
        [0, 1, 8],
        [1, 3, 8],
        [0, 2, 3],
        [2, 3, 20]
    ]
]
# 예상 결과: 10


sample2 = [
    5,
    [
        [0, 1, 10],
        [1, 2, 10],
        [2, 4, 10],
        [0, 3, 100],
        [3, 4, 1]
    ]
]
# 예상 결과: 15


sample3 = [
    3,
    [
        [0, 1, 5]
    ]
]
# 예상 결과: -1


sample4 = [
    2,
    [
        [0, 1, 7]
    ]
]
# 예상 결과: 3


sample5 = [
    4,
    [
        [0, 1, 4],
        [1, 2, 4],
        [2, 3, 4],
        [0, 3, 20]
    ]
]
# 예상 결과: 10


def solution(n, roads):
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
10
15
-1
3
10
```
"""