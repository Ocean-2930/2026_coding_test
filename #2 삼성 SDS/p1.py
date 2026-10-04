sample1 = [
    2,
    [
        [3, 5, 1, 4, 1],
        [2, 2, 3, 5, 2],
        [3, 4, 2, 4, 4],
        [4, 4, 1, 4, 2],
        [3, 2, 1, 2, 3]
    ],
    [1, 2, 3, 4, 5, 6, 7, 8, 9] * 100
]
# 예상 결과: [14, 6]


sample2 = [
    1,
    [
        [1, 1, 2, 3, 4],
        [5, 1, 6, 7, 8],
        [2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2],
        [3, 4, 5, 6, 7]
    ],
    [9, 8, 7, 6, 5, 4, 3, 2, 1] * 100
]
# 예상 결과: [3]


sample3 = [
    3,
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 1],
        [2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2],
        [3, 4, 5, 6, 7]
    ],
    [1, 2, 3] * 200
]
# 예상 결과: []

def makemat(m, n):
    return [[0] * m for _ in range(n)]

def copymat(mat):
    m = len(mat[0])
    n = len(mat)

    res = makemat(m, n)

    for i in range(m):
        for j in range(n):
            res[j][i] = mat[j][i]

    return res

def validate(mat, a, b):
    m = len(mat[0])
    n = len(mat)

    return (0 <= a < m) and (0 <= b < n)

origin = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]

spinner = [
    [(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1)],
    [(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0)],
    [(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1)]
]

def spin(board, a, b, deg):
    global origin, spinner

    res = copymat(board)

    for i in range(len(origin)):
        res[b+spinner[deg][i][1]][a+spinner[deg][i][0]] = board[b+origin[i][1]][a+origin[i][0]]

    return res

from collections import deque

def gain(board, a, b):
    global origin

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    score = 0
    for i in range(len(origin)):
        if board[b+origin[i][1]][a+origin[i][0]] == 0:
            continue

        tar = board[b+origin[i][1]][a+origin[i][0]]
        res = []

        q = deque()
        q.append((a+origin[i][0], b+origin[i][1]))
        while 0 < len(q):
            c = q.popleft()

            if board[c[1]][c[0]] != tar:
                continue

            if c in res:
                continue

            res.append(c)

            for d in directions:
                if validate(board, c[0]+d[0], c[1]+d[1]):
                    q.append((c[0]+d[0], c[1]+d[1]))


        if 3 <= len(res):
            score += len(res)
            for c in res:
                board[c[1]][c[0]] = 0

    return score

def fill(board, filler, flag):
    m = len(board[0])
    n = len(board)   

    for i in range(m):
        for j in range(n):
            if board[j][i] == 0:
                board[j][i] = filler[flag]
                flag += 1

    return board, flag

def solution(k, board, refill):
    flag = 0

    m = len(board[0])
    n = len(board)

    res = []

    target = board
    for _ in range(k):
        run_score = 0

        max_score = -1
        coordinate = ()
        after = []
        for l in range(len(spinner)):
            for i in range(1, m-1):
                for j in range(1, n-1):
                    buff = spin(target, i, j, l)
                    score = gain(buff, i, j)
                    if max_score < score:
                        coordinate = (i, j)
                        after = buff

        run_score += max_score
        target, flag = fill(after, refill, flag)

        while True:
            score = gain(target, coordinate[0], coordinate[1])
            
            if score == 0:
                break

            run_score += score
            target, flag = fill(target, refill, flag)

        if run_score == 0:
            break

        res.append(run_score)

    return res

ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)

"""
좋아. 아까 문제를 네가 정리한 방식에 맞춰 다시 줄게. 이번에는 **풀이 힌트 없이 문제 조건과 바로 실행 가능한 샘플만** 제공하겠다.

# 문제. 고대 유적 복원

크기 `N × N`의 유적 지도가 있다.

각 칸에는 `0` 또는 `1` 이상 `9` 이하의 정수가 적혀 있다.

`0`은 빈칸이고, `1~9`는 유물 조각의 종류를 의미한다.

탐사자는 최대 `K`번의 탐사를 진행한다.

각 탐사에서는 `3 × 3` 영역 하나를 선택하여 회전한 뒤 유물을 획득한다.

## 1. 회전

지도에서 `3 × 3` 크기의 영역 하나를 선택한다.

선택한 영역은 다음 중 하나의 각도로 시계 방향 회전할 수 있다.

```text
90도
180도
270도
```

예를 들어 다음 영역을 90도 회전하면

```text
1 2 3
4 5 6
7 8 9
```

다음과 같이 변한다.

```text
7 4 1
8 5 2
9 6 3
```

---

## 2. 유물 획득 가능 여부

회전 후 같은 숫자가 상하좌우로 연결된 영역을 확인한다.

같은 숫자의 유물이 `3개 이상` 연결되어 있다면 해당 그룹의 모든 유물을 획득할 수 있다.

대각선으로 연결된 경우는 같은 그룹으로 보지 않는다.

예를 들어

```text
1 1 2
1 2 2
3 3 4
```

에서는 `1` 세 개와 `2` 세 개가 각각 하나의 그룹이므로 총 6개의 유물을 획득할 수 있다.

---

## 3. 회전 방법 선택

가능한 모든 회전 방법 중 회전 직후 획득할 수 있는 유물의 개수가 가장 많은 방법을 선택한다.

동일한 개수의 유물을 획득할 수 있는 방법이 여러 개라면 다음 기준을 순서대로 적용한다.

1. 회전 각도가 작은 것
2. 선택한 `3 × 3` 영역의 왼쪽 위 열 번호가 작은 것
3. 선택한 `3 × 3` 영역의 왼쪽 위 행 번호가 작은 것

행과 열 번호는 모두 `0`부터 시작한다.

어떤 회전을 하더라도 획득할 수 있는 유물이 하나도 없다면 탐사를 즉시 종료한다.

---

## 4. 유물 제거

선택한 회전을 실제 지도에 적용한다.

이후 크기가 3 이상인 모든 연결 그룹을 동시에 제거한다.

제거된 칸은 `0`이 된다.

제거된 유물의 수는 현재 탐사의 점수에 더한다.

---

## 5. 새로운 유물 배치

제거된 칸에는 대기 중인 유물을 하나씩 채운다.

대기 유물은 `refill` 배열의 앞쪽부터 순서대로 사용한다.

빈칸을 채우는 우선순위는 다음과 같다.

1. 열 번호가 작은 칸
2. 같은 열이라면 행 번호가 큰 칸

예를 들어 이번 제거로 다음 세 칸이 비었다고 하자.

```text
(1, 0)
(3, 0)
(2, 1)
```

채우는 순서는

```text
(3, 0)
(1, 0)
(2, 1)
```

이다.

기존부터 `0`이었던 칸은 채우지 않는다.

이번 제거 과정에서 새롭게 제거된 칸만 채운다.

대기 유물은 모든 탐사가 끝날 때까지 부족하지 않을 만큼 주어진다.

---

## 6. 연쇄 획득

새로운 유물을 배치한 후 다시 크기가 3 이상인 연결 그룹이 생겼다면 다시 해당 그룹을 모두 제거한다.

이후 동일한 규칙으로 새로운 유물을 채운다.

더 이상 제거할 수 있는 그룹이 없을 때까지 이 과정을 반복한다.

한 탐사에서 최초 제거와 모든 연쇄 제거를 통해 획득한 유물의 총합이 해당 탐사의 점수다.

---

## 7. 종료

다음 중 하나를 만족하면 탐사를 종료한다.

```text
K번의 탐사를 모두 완료한 경우
어떤 회전을 하더라도 유물을 획득할 수 없는 경우
```

각 탐사에서 획득한 점수를 순서대로 반환하라.

## 제한 조건

```text
1 <= K <= 10
5 <= N <= 10
board[r][c]는 0 이상 9 이하
refill의 각 값은 1 이상 9 이하
```

`board`는 정사각형 배열이다.

---

# 샘플 코드

```python
sample1 = [
    2,
    [
        [3, 5, 1, 4, 1],
        [2, 2, 3, 5, 2],
        [3, 4, 2, 4, 4],
        [4, 4, 1, 4, 2],
        [3, 2, 1, 2, 3]
    ],
    [1, 2, 3, 4, 5, 6, 7, 8, 9] * 100
]
# 예상 결과: [14, 6]


sample2 = [
    1,
    [
        [1, 1, 2, 3, 4],
        [5, 1, 6, 7, 8],
        [2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2],
        [3, 4, 5, 6, 7]
    ],
    [9, 8, 7, 6, 5, 4, 3, 2, 1] * 100
]
# 예상 결과: [3]


sample3 = [
    3,
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 1],
        [2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2],
        [3, 4, 5, 6, 7]
    ],
    [1, 2, 3] * 200
]
# 예상 결과: []


def solution(k, board, refill):
    pass


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)
```

목표 출력은 다음과 같다.

```text
[14, 6]
[3]
[]
```

코드 작성해서 보내면 먼저 **정확성, 반례, 경계 조건, 시간복잡도, Python 구현 문제** 순서로 볼게.
"""

"""
solution

from collections import deque


sample1 = [
    2,
    [
        [3, 5, 1, 4, 1],
        [2, 2, 3, 5, 2],
        [3, 4, 2, 4, 4],
        [4, 4, 1, 4, 2],
        [3, 2, 1, 2, 3]
    ],
    [1, 2, 3, 4, 5, 6, 7, 8, 9] * 100
]
# 예상 결과: [14, 6]


sample2 = [
    1,
    [
        [1, 1, 2, 3, 4],
        [5, 1, 6, 7, 8],
        [2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2],
        [3, 4, 5, 6, 7]
    ],
    [9, 8, 7, 6, 5, 4, 3, 2, 1] * 100
]
# 예상 결과: [3]


sample3 = [
    3,
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 1],
        [2, 3, 4, 5, 6],
        [7, 8, 9, 1, 2],
        [3, 4, 5, 6, 7]
    ],
    [1, 2, 3] * 200
]
# 예상 결과: []


def makemat(m, n):
    return [[0] * m for _ in range(n)]


def copymat(mat):
    return [row[:] for row in mat]


origin = [
    (-1, -1), (0, -1), (1, -1),
    (1, 0),
    (1, 1), (0, 1), (-1, 1),
    (-1, 0)
]


spinner = [
    # 90도
    [
        (1, -1), (1, 0), (1, 1),
        (0, 1),
        (-1, 1), (-1, 0), (-1, -1),
        (0, -1)
    ],

    # 180도
    [
        (1, 1), (0, 1), (-1, 1),
        (-1, 0),
        (-1, -1), (0, -1), (1, -1),
        (1, 0)
    ],

    # 270도
    [
        (-1, 1), (-1, 0), (-1, -1),
        (0, -1),
        (1, -1), (1, 0), (1, 1),
        (0, 1)
    ]
]


def spin(board, a, b, deg):
    res = copymat(board)

    for i in range(len(origin)):
        ox, oy = origin[i]
        sx, sy = spinner[deg][i]

        res[b + sy][a + sx] = board[b + oy][a + ox]

    return res


def gain(board):
    m = len(board[0])
    n = len(board)

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    visited = [[False] * m for _ in range(n)]

    score = 0
    remove_list = []

    for y in range(n):
        for x in range(m):

            if visited[y][x]:
                continue

            if board[y][x] == 0:
                continue

            tar = board[y][x]

            q = deque()
            q.append((x, y))
            visited[y][x] = True

            group = []

            while q:
                cx, cy = q.popleft()
                group.append((cx, cy))

                for dx, dy in directions:
                    nx = cx + dx
                    ny = cy + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue

                    if visited[ny][nx]:
                        continue

                    if board[ny][nx] != tar:
                        continue

                    visited[ny][nx] = True
                    q.append((nx, ny))

            if len(group) >= 3:
                score += len(group)
                remove_list.extend(group)

    for x, y in remove_list:
        board[y][x] = 0

    return score


def fill(board, filler, flag):
    m = len(board[0])
    n = len(board)

    # 열 번호가 작은 순서
    for x in range(m):

        # 같은 열에서는 행 번호가 큰 순서
        for y in range(n - 1, -1, -1):

            if board[y][x] == 0:
                board[y][x] = filler[flag]
                flag += 1

    return board, flag


def solution(k, board, refill):
    flag = 0

    target = copymat(board)

    m = len(target[0])
    n = len(target)

    res = []

    for _ in range(k):

        max_score = -1
        after = None

        # 회전각 -> 열 -> 행 순서
        # 동점에서는 갱신하지 않으므로 우선순위가 자동 적용됨
        for deg in range(len(spinner)):
            for x in range(1, m - 1):
                for y in range(1, n - 1):

                    buff = spin(target, x, y, deg)

                    score = gain(buff)

                    if max_score < score:
                        max_score = score
                        after = buff

        # 어떤 회전에서도 얻을 유물이 없음
        if max_score == 0:
            break

        run_score = max_score

        target, flag = fill(after, refill, flag)

        # 연쇄 제거
        while True:
            score = gain(target)

            if score == 0:
                break

            run_score += score
            target, flag = fill(target, refill, flag)

        res.append(run_score)

    return res


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)
"""