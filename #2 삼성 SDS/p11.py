sample1 = [
    4,
    [
        [0, 0],
        [0, 1],
        [2, 2],
        [1, 2],
        [1, 1],
        [3, 3]
    ]
]
# 예상 결과:
# [
#     [1, 1],
#     [1, 2],
#     [2, 2],
#     [2, 2],
#     [1, 5],
#     [2, 5]
# ]


sample2 = [
    3,
    [
        [1, 1],
        [1, 1],
        [0, 1],
        [2, 1],
        [1, 0],
        [1, 2]
    ]
]
# 예상 결과:
# [
#     [1, 1],
#     [1, 1],
#     [1, 2],
#     [1, 3],
#     [1, 4],
#     [1, 5]
# ]


sample3 = [
    5,
    [
        [0, 0],
        [0, 1],
        [4, 4],
        [4, 3],
        [2, 2],
        [1, 2],
        [0, 2],
        [3, 2],
        [4, 2]
    ]
]
# 예상 결과:
# [
#     [1, 1],
#     [1, 2],
#     [2, 2],
#     [2, 2],
#     [3, 2],
#     [3, 2],
#     [2, 5],
#     [2, 6],
#     [1, 9]
# ]


sample4 = [
    2,
    [
        [0, 0],
        [1, 1]
    ]
]
# 예상 결과:
# [
#     [1, 1],
#     [2, 1]
# ]

def findroot(connections, i, j, N):
    c = connections[i][j]

    if c != -1:
        return findroot(connections, c // N, c % N, N)

    return i, j


def solution(n, commands):
    grid = [[0] * n for _ in range(n)]
    con = [[-1] * n for _ in range(n)]
    size = {}

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    res = []
    for c in commands:
        x = c[0]
        y = c[1]
        
        if grid[x][y] == 1:
            continue

        grid[x][y] = 1

        root = -1
        for d in directions:
            nx = x + d[0]
            ny = y + d[1]

            if not ((0<= nx <n) and (0<= ny < n)):
                continue

            if grid[nx][ny] == 0:
                continue

            i, j = findroot(con, nx, ny, n)

            if root == -1:
                root = n * i + j
                con[x][y] = root
                size[root] += 1
            else:
                c = n * i + j
                con[i][j] = root
                size[root] += size[c]
                size.pop(c, None)

        if root == -1:
            size[n * x + y] = 1

        res.append([len(size), max(size.values())])

    return res


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)

ans = solution(*sample4)
print(ans)

"""
좋아. 이번에는 **격자 상태 변화 + 연결 그룹 관리**가 들어가는 삼성식 문제로 줄게. 풀이 방향은 언급하지 않고 문제와 실행 가능한 샘플만 제공할게.

# 문제. 통신 기지 복구

크기 `N × N`의 지역이 있다.

처음에는 모든 칸의 통신 기지가 고장 난 상태이다.

복구 명령이 순서대로 주어지며, 각 명령에서는 특정 위치 `(r, c)`의 통신 기지를 복구한다.

복구된 통신 기지들은 서로 연결되어 하나의 통신망을 형성할 수 있다.

## 통신망 연결 조건

복구된 두 기지가 상하좌우로 인접해 있다면 두 기지는 직접 연결된다.

또한 다른 복구된 기지를 거쳐 서로 이동할 수 있다면 모두 하나의 통신망에 속한다.

대각선으로만 인접한 기지는 연결되지 않는다.

예를 들어 다음 상태에서:

```text
1 1 0
0 1 0
0 0 1
```

`1`은 복구된 기지, `0`은 고장 난 기지이다.

왼쪽 위의 세 기지는 하나의 통신망이지만, 오른쪽 아래 기지는 별도의 통신망이다.

따라서 현재 통신망은 총 2개이다.

---

## 복구 명령

각 명령은 다음과 같다.

```python
[r, c]
```

해당 위치의 기지를 복구한다.

이미 복구된 기지를 다시 복구하는 명령이 들어오면 아무 변화도 일어나지 않는다.

---

## 각 명령 이후 계산할 값

각 복구 명령을 처리한 직후 다음 두 값을 구한다.

1. 현재 존재하는 통신망의 개수
2. 가장 많은 기지를 포함한 통신망의 크기

예를 들어 현재 상태가:

```text
1 1 0 0
0 1 0 1
0 0 0 1
0 0 0 0
```

이라면 통신망은 2개이고, 각각의 크기는 3과 2이다.

따라서 결과는:

```python
[2, 3]
```

이다.

---

# 반환값

모든 복구 명령에 대해

```python
[통신망 개수, 가장 큰 통신망의 크기]
```

를 계산하여 순서대로 배열에 담아 반환하라.

---

# 제한 조건

```text
1 <= N <= 500

1 <= 복구 명령의 개수 <= 200000

0 <= r < N
0 <= c < N
```

같은 위치에 대한 복구 명령이 여러 번 주어질 수 있다.

격자에서 연결은 상하좌우만 인정한다.

---

# 샘플 코드

```python
sample1 = [
    4,
    [
        [0, 0],
        [0, 1],
        [2, 2],
        [1, 2],
        [1, 1],
        [3, 3]
    ]
]
# 예상 결과:
# [
#     [1, 1],
#     [1, 2],
#     [2, 2],
#     [2, 2],
#     [1, 5],
#     [2, 5]
# ]


sample2 = [
    3,
    [
        [1, 1],
        [1, 1],
        [0, 1],
        [2, 1],
        [1, 0],
        [1, 2]
    ]
]
# 예상 결과:
# [
#     [1, 1],
#     [1, 1],
#     [1, 2],
#     [1, 3],
#     [1, 4],
#     [1, 5]
# ]


sample3 = [
    5,
    [
        [0, 0],
        [0, 1],
        [4, 4],
        [4, 3],
        [2, 2],
        [1, 2],
        [0, 2],
        [3, 2],
        [4, 2]
    ]
]
# 예상 결과:
# [
#     [1, 1],
#     [1, 2],
#     [2, 2],
#     [2, 2],
#     [3, 2],
#     [3, 2],
#     [2, 5],
#     [2, 6],
#     [1, 9]
# ]


sample4 = [
    2,
    [
        [0, 0],
        [1, 1]
    ]
]
# 예상 결과:
# [
#     [1, 1],
#     [2, 1]
# ]


def solution(n, commands):
    pass


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)

ans = solution(*sample4)
print(ans)
```

목표 출력:

```text
[[1, 1], [1, 2], [2, 2], [2, 2], [1, 5], [2, 5]]

[[1, 1], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]

[[1, 1], [1, 2], [2, 2], [2, 2], [3, 2], [3, 2], [2, 5], [2, 6], [1, 9]]

[[1, 1], [2, 1]]
```

이번에는 `N=500`, 명령 최대 `200,000개`라는 제한까지 고려해서 구현해봐.
"""

"""
solution
def findroot(connections, i, j, n):
    c = connections[i][j]

    if c == -1:
        return i, j

    ri, rj = findroot(connections, c // n, c % n, n)

    # 경로 압축
    connections[i][j] = ri * n + rj

    return ri, rj


def solution(n, commands):
    grid = [[0] * n for _ in range(n)]
    con = [[-1] * n for _ in range(n)]

    size = {}

    directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ]

    res = []
    max_size = 0

    for x, y in commands:

        # 이미 복구된 기지
        if grid[x][y] == 1:
            res.append([len(size), max_size])
            continue

        grid[x][y] = 1

        # 인접한 서로 다른 네트워크의 root 수집
        roots = set()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if grid[nx][ny] == 0:
                continue

            ri, rj = findroot(con, nx, ny, n)
            roots.add(ri * n + rj)

        current = x * n + y

        # 주변 네트워크가 없음
        if not roots:
            size[current] = 1
            max_size = max(max_size, 1)

        else:
            # 임의의 네트워크 하나를 대표로 선택
            root = next(iter(roots))

            con[x][y] = root

            total_size = 1

            for other in roots:
                total_size += size[other]

                if other != root:
                    oi = other // n
                    oj = other % n

                    con[oi][oj] = root
                    size.pop(other)

            size[root] = total_size
            max_size = max(max_size, total_size)

        res.append([len(size), max_size])

    return res
"""