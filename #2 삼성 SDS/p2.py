sample1 = [
    [2, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 2]
]
# 예상 결과: 5


sample2 = [
    [2, 0, 1, 0, 0],
    [0, 0, 1, 0, 2],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 2, 0, 0, 0]
]
# 예상 결과: 6


sample3 = [
    [2, 1, 0],
    [1, 1, 0],
    [0, 0, 0]
]
# 예상 결과: 2

def find_number(board, target):
    res = []
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == target:
                res.append((i, j))

    return res

def dfs(res, targets, arr, flag):
    if len(targets) <= flag:
        return

    for i in range(flag, len(targets)-(2-len(arr))):
        subarr = arr[:]
        subarr.append(targets[i])

        if len(subarr) == 3:
            res.append(subarr)
            continue

        dfs(res, targets, subarr, i + 1)

def creat_wall(board, targets):
    res = [arr[:] for arr in board]
    for c in targets:
        res[c[0]][c[1]] = 1

    return res

from collections import deque

def validate(n, m, a, b):
    return (0<=a<n) and (0<=b<m)

def simulate(board):
    res = [arr[:] for arr in board]

    n = len(board)
    m = len(board[0])

    source = find_number(res, 2)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for s in source:
        q = deque()
        for d in directions:
            q.append((s[0]+d[0], s[1]+d[1]))

        while 0 < len(q):
            focus = q.pop()

            if not validate(n, m, focus[0], focus[1]):
                continue

            if res[focus[0]][focus[1]] != 0:
                continue

            res[focus[0]][focus[1]] = 2

            for d in directions:
                q.append((focus[0]+d[0], focus[1]+d[1]))
        

    room_count = 0
    for i in range(len(res)):
        for j in range(len(res[0])):
            if res[i][j] == 0:
                room_count += 1
    
    return room_count

def solution(board):
    zeros = find_number(board, 0)

    combinations = []
    dfs(combinations, zeros, [], 0)

    res = -1
    for c in combinations:
        blocked = creat_wall(board, c)
        room_count = simulate(blocked)

        if res < room_count:
            res = room_count

    return res


ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

"""
좋아. 이번에는 이전 문제와 다른 유형으로 갈게. 풀이 힌트 없이 문제와 실행 가능한 샘플만 줄게.

# 문제. 방역벽 설치

크기 `N × M`의 연구 구역이 있다.

각 칸은 다음 세 종류 중 하나다.

```text
0 : 빈칸
1 : 기존 벽
2 : 바이러스
```

바이러스의 확산을 최대한 막기 위해 빈칸 중 정확히 3곳에 새로운 벽을 설치하려고 한다.

## 바이러스 확산

새로운 벽 3개를 모두 설치한 뒤 바이러스가 확산된다.

바이러스는 상하좌우로 인접한 빈칸으로 퍼질 수 있다.

기존 벽과 새로 설치한 벽은 통과할 수 없다.

바이러스는 더 이상 퍼질 수 있는 빈칸이 없을 때까지 계속 확산된다.

모든 바이러스는 동시에 확산을 시작한다고 생각하면 된다.

## 안전 영역

바이러스 확산이 모두 끝난 뒤에도 값이 `0`으로 남아 있는 칸을 안전 영역이라고 한다.

새로 설치한 벽 3칸은 안전 영역에 포함하지 않는다.

새로운 벽을 설치할 위치를 적절히 선택하여 얻을 수 있는 안전 영역의 최대 크기를 반환하라.

## 제한 조건

```text
3 <= N <= 8
3 <= M <= 8

board의 각 값은 0, 1, 2 중 하나이다.

빈칸은 최소 3개 존재한다.
바이러스는 최소 1개 존재한다.
새로운 벽은 반드시 서로 다른 빈칸 3곳에 설치해야 한다.
```

# 샘플 코드

```python
sample1 = [
    [2, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 2]
]
# 예상 결과: 5


sample2 = [
    [2, 0, 1, 0, 0],
    [0, 0, 1, 0, 2],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 2, 0, 0, 0]
]
# 예상 결과: 6


sample3 = [
    [2, 1, 0],
    [1, 1, 0],
    [0, 0, 0]
]
# 예상 결과: 2


def solution(board):
    pass


ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)
```

목표 출력은 다음과 같다.

```text
5
6
2
```
"""

"""
from itertools import combinations

for walls in combinations(zeros, 3):
    blocked = creat_wall(board, walls)
    room_count = simulate(blocked)
    res = max(res, room_count)
"""