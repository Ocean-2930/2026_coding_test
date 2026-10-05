sample1 = [
    5,
    [
        ["connect", 0, 1],
        ["connect", 1, 2],
        ["check", 0, 2],
        ["check", 0, 3],
        ["connect", 3, 4],
        ["check", 2, 4]
    ]
]
# 예상 결과: [True, False, False]


sample2 = [
    4,
    [
        ["check", 0, 0],
        ["connect", 0, 1],
        ["connect", 2, 3],
        ["check", 1, 3],
        ["connect", 1, 2],
        ["check", 0, 3]
    ]
]
# 예상 결과: [True, False, True]


sample3 = [
    3,
    [
        ["connect", 0, 1],
        ["connect", 0, 1],
        ["check", 0, 1],
        ["check", 1, 2]
    ]
]
# 예상 결과: [True, False]

# from collections import deque

# def solution(n, commands):
#     grid = [[0] * n for _ in range(n)]

#     res = []
#     for c in commands:
#         if c[0] == "connect":
#             grid[c[1]][c[2]] = 1
#             grid[c[2]][c[1]] = 1
#         elif c[0] == "check":
#             v = []
#             q = deque()
#             q.append(c[1])

#             loopresult = False
#             while len(q):
#                 buff = q.popleft()

#                 if buff == c[2]:
#                     loopresult = True
#                     break

#                 if buff in v:
#                     continue

#                 v.append(buff)

#                 for i in range(n):
#                     if grid[buff][i] == 1:
#                         q.append(i)

#             res.append(loopresult)
    
#     return res

class Node:
    def __init__(self, i):
        self.parent = None
        self.index = i

    def network(self):
        if self.parent:
            return self.parent.network()

        return self.index

    def setparent(self, parent):
        self.parent = parent

def solution(n, commands):
    p = [Node(i) for i in range(n)]

    res = []
    for c in commands:
        if c[0] == "connect":
            na = p[c[1]].network()
            nb = p[c[2]].network()

            if na != nb:
                p[na].setparent(p[nb])
        elif c[0] == "check":
            res.append(p[c[1]].network() == p[c[2]].network())

    return res




ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)

"""
좋아. 이번에는 **Union-Find나 그래프 연결성** 쪽으로 넘어가자. 풀이 힌트 없이 문제와 샘플만 줄게.

# 문제. 네트워크 연결

`N`개의 컴퓨터가 있다. 컴퓨터 번호는 `0`부터 `N-1`까지다.

처음에는 모든 컴퓨터가 서로 연결되어 있지 않다.

이후 여러 개의 명령이 순서대로 주어진다.

명령은 두 종류다.

```text
["connect", a, b]
["check", a, b]
```

`connect a b`는 컴퓨터 `a`와 `b`를 직접 연결한다.

연결은 양방향이다.

직접 연결되어 있지 않더라도 다른 컴퓨터들을 거쳐 이동할 수 있다면 두 컴퓨터는 같은 네트워크에 속한다고 본다.

예를 들어:

```text
0 - 1 - 2
```

와 같이 연결되어 있다면 `0`과 `2`도 서로 연결된 상태다.

`check a b` 명령이 주어지면, 두 컴퓨터가 같은 네트워크에 속해 있으면 `True`, 아니면 `False`를 결과 배열에 추가한다.

모든 명령을 처리한 뒤 `check` 명령들의 결과를 순서대로 반환하라.

## 제한 조건

```text
1 <= N <= 100000
1 <= 명령 개수 <= 200000

0 <= a, b < N
```

같은 두 컴퓨터를 여러 번 연결하는 명령이 주어질 수 있다.

자기 자신을 연결하거나 확인하는 명령도 주어질 수 있다.

# 샘플 코드

```python
sample1 = [
    5,
    [
        ["connect", 0, 1],
        ["connect", 1, 2],
        ["check", 0, 2],
        ["check", 0, 3],
        ["connect", 3, 4],
        ["check", 2, 4]
    ]
]
# 예상 결과: [True, False, False]


sample2 = [
    4,
    [
        ["check", 0, 0],
        ["connect", 0, 1],
        ["connect", 2, 3],
        ["check", 1, 3],
        ["connect", 1, 2],
        ["check", 0, 3]
    ]
]
# 예상 결과: [True, False, True]


sample3 = [
    3,
    [
        ["connect", 0, 1],
        ["connect", 0, 1],
        ["check", 0, 1],
        ["check", 1, 2]
    ]
]
# 예상 결과: [True, False]


def solution(n, commands):
    pass


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)
```

목표 출력:

```text
[True, False, False]
[True, False, True]
[True, False]
```
"""

"""
solution
def solution(n, commands):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)

        if ra != rb:
            parent[rb] = ra

    res = []

    for c in commands:
        if c[0] == "connect":
            union(c[1], c[2])

        elif c[0] == "check":
            res.append(find(c[1]) == find(c[2]))

    return res
"""