sample1 = [
    [3, 1, 4, 1, 5],
    [
        [0, 2],
        [1, 3],
        [2, 4]
    ]
]
# 예상 결과: [8, 6, 10]


sample2 = [
    [10, -3, 7, 2, -5, 8],
    [
        [0, 5],
        [1, 1],
        [2, 4],
        [3, 5]
    ]
]
# 예상 결과: [19, -3, 4, 5]


sample3 = [
    [5],
    [
        [0, 0]
    ]
]
# 예상 결과: [5]


sample4 = [
    [1, 2, 3, 4, 5, 6],
    [
        [0, 0],
        [0, 5],
        [4, 5],
        [2, 2]
    ]
]
# 예상 결과: [1, 21, 11, 3]


def solution(arr, queries):
    sumarr = []

    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        sumarr.append(sum)

    res = []
    for q in queries:
        r = sumarr[q[1]] - sumarr[q[0]] + arr[q[0]]
        res.append(r)

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
좋아. 이번에는 앞에서 했던 완전탐색, 우선순위 큐, 최단거리와 겹치지 않게 **누적합 + 구간 질의** 유형으로 가자. 풀이 힌트 없이 문제와 샘플만 줄게.

# 문제. 구간 에너지 합

길이 `N`의 정수 배열 `arr`가 주어진다.

이후 여러 개의 질의가 주어진다.

각 질의는 두 정수 `l`, `r`로 이루어져 있으며, 배열의 `l`번째 원소부터 `r`번째 원소까지의 합을 구해야 한다.

인덱스는 `0`부터 시작한다.

각 질의의 결과를 순서대로 배열에 담아 반환하라.

## 제한 조건

```text
1 <= N <= 100000
1 <= Q <= 100000

-100000 <= arr[i] <= 100000

0 <= l <= r < N
```

`Q`는 질의 개수이다.

각 질의는 다음 형태다.

```python
queries[i] = [l, r]
```

## 예시

배열이

```text
[3, 1, 4, 1, 5]
```

이고 질의가

```text
[1, 3]
```

이라면

```text
arr[1] + arr[2] + arr[3]
= 1 + 4 + 1
= 6
```

이므로 결과는 `6`이다.

# 샘플 코드

```python
sample1 = [
    [3, 1, 4, 1, 5],
    [
        [0, 2],
        [1, 3],
        [2, 4]
    ]
]
# 예상 결과: [8, 6, 10]


sample2 = [
    [10, -3, 7, 2, -5, 8],
    [
        [0, 5],
        [1, 1],
        [2, 4],
        [3, 5]
    ]
]
# 예상 결과: [19, -3, 4, 5]


sample3 = [
    [5],
    [
        [0, 0]
    ]
]
# 예상 결과: [5]


sample4 = [
    [1, 2, 3, 4, 5, 6],
    [
        [0, 0],
        [0, 5],
        [4, 5],
        [2, 2]
    ]
]
# 예상 결과: [1, 21, 11, 3]


def solution(arr, queries):
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
[8, 6, 10]
[19, -3, 4, 5]
[5]
[1, 21, 11, 3]
```
"""