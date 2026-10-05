sample1 = [
    [0, 1, 5, 1],
    [2, 2, 2, 1],
    [5, 5, 1, 1],
    [9, 1, 1, 0]
]
# 예상 결과: 7


sample2 = [
    [0, 1, -1, 1],
    [2, 3, -1, 1],
    [-1, 1, -1, 1],
    [4, 1, 1, 0]
]
# 예상 결과: 7


sample3 = [
    [0, -1, 1],
    [-1, -1, 1],
    [1, 1, 0]
]
# 예상 결과: -1


sample4 = [
    [0, 9, 9, 9, 9],
    [1, 1, 1, 1, 9],
    [9, 9, 9, 1, 9],
    [9, 1, 1, 1, 9],
    [9, 1, 9, 9, 0]
]
# 예상 결과: 15

from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])

    directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

    cost = [[-1] * m for _ in range(n)]
    cost[0][0] = 0

    q = deque()
    q.append((0, 0, 0))

    while len(q):
        buff = q.popleft()

        if (cost[buff[1]][buff[0]] != -1) and (cost[buff[1]][buff[0]] < buff[2]):
            continue

        for d in directions:
            nx = buff[0] + d[0]
            ny = buff[1] + d[1]

            if not ((0 <= nx < m) and (0 <= ny < n)):
                continue

            if board[ny][nx] == -1:
                continue

            ncost = cost[buff[1]][buff[0]] + board[ny][nx]

            if cost[ny][nx] == -1:
                cost[ny][nx] = ncost
                q.append((nx, ny, ncost))
                continue

            if cost[ny][nx] <= ncost:
                continue

            cost[ny][nx] = ncost
            q.append((nx, ny, ncost))
            
    
    return cost[n-1][m-1]


ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)

"""
좋아. 이번에는 앞의 완전탐색, 백트래킹, 우선순위 큐 활용과는 조금 다른 유형으로 갈게. 풀이 힌트 없이 문제와 샘플만 줄게.

# 문제. 최소 이동 비용

크기 `N × M`의 지도가 있다.

각 칸에는 해당 칸으로 이동할 때 필요한 비용이 적혀 있다.

출발점은 `(0, 0)`, 도착점은 `(N-1, M-1)`이다.

현재 칸에서 상하좌우로 한 칸씩 이동할 수 있다.

## 이동 비용

어떤 칸 `(r, c)`로 이동하면 `board[r][c]`만큼의 비용이 발생한다.

출발점 `(0, 0)`의 비용은 계산하지 않는다.

예를 들어:

```text
0 2 5
1 3 1
4 1 0
```

에서

```text
(0,0) → (1,0) → (1,1) → (1,2) → (2,2)
```

로 이동한다면 총 비용은

```text
1 + 3 + 1 + 0 = 5
```

이다.

## 장애물

값이 `-1`인 칸은 장애물이다.

장애물로는 이동할 수 없다.

출발점과 도착점은 장애물이 아니다.

## 반환값

출발점에서 도착점까지 이동할 수 있는 모든 경로 중 총 이동 비용의 최솟값을 반환하라.

도착점에 도달할 수 없다면 `-1`을 반환한다.

## 제한 조건

```text
2 <= N <= 100
2 <= M <= 100

board[r][c]는 -1 또는 0 이상 100 이하이다.

board[0][0] != -1
board[N-1][M-1] != -1
```

같은 칸을 여러 번 지나가는 것도 금지하지 않는다.

# 샘플 코드

```python
sample1 = [
    [0, 1, 5, 1],
    [2, 2, 2, 1],
    [5, 5, 1, 1],
    [9, 1, 1, 0]
]
# 예상 결과: 7


sample2 = [
    [0, 1, -1, 1],
    [2, 3, -1, 1],
    [-1, 1, -1, 1],
    [4, 1, 1, 0]
]
# 예상 결과: 7


sample3 = [
    [0, -1, 1],
    [-1, -1, 1],
    [1, 1, 0]
]
# 예상 결과: -1


sample4 = [
    [0, 9, 9, 9, 9],
    [1, 1, 1, 1, 9],
    [9, 9, 9, 1, 9],
    [9, 1, 1, 1, 9],
    [9, 1, 9, 9, 0]
]
# 예상 결과: 15


def solution(board):
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
7
7
-1
15
```
"""

"""
solution
heapq를 활용해서 항상 최소 비용 경로부터 계산하기
"""