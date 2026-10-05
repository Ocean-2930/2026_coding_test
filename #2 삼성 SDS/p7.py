sample1 = [
    [7, 10],
    6
]
# 예상 결과: 28


sample2 = [
    [1, 2, 3],
    10
]
# 예상 결과: 6


sample3 = [
    [5],
    7
]
# 예상 결과: 35


sample4 = [
    [3, 8, 11],
    20
]
# 예상 결과: 33


import math

def solution(times, m):
    s = sorted(times)

    cnt = math.ceil(m / len(times))
    high = cnt * s[-1]
    low = cnt * s[0]

    while True:
        if high == low:
            return high

        mid = (high + low) // 2

        final = (high - low == 1)

        workcnt = 0
        for t in s:
            workcnt += mid // t

        if m < workcnt:
            high = mid
            continue

        if workcnt < m:
            if final:
                return high

            low = mid
            continue

        high = mid


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)

ans = solution(*sample4)
print(ans)

"""
좋아. 이번에는 **이분 탐색** 유형으로 가자. 풀이 힌트 없이 문제와 샘플만 줄게.

# 문제. 최소 처리 시간

작업이 총 `M`개 있다.

작업을 처리할 수 있는 기계가 `N`대 있으며, 각 기계는 작업 하나를 처리하는 데 걸리는 시간이 서로 다르다.

`times[i]`는 `i`번째 기계가 작업 하나를 처리하는 데 걸리는 시간이다.

각 기계는 한 번에 하나의 작업만 처리할 수 있지만, 작업을 완료하면 바로 다음 작업을 처리할 수 있다.

모든 기계는 동시에 작업을 시작할 수 있다.

모든 작업을 처리하는 데 필요한 최소 시간을 반환하라.

## 제한 조건

```text
1 <= N <= 100000
1 <= M <= 1000000000
1 <= times[i] <= 1000000000
```

`times`에는 중복된 값이 있을 수 있다.

## 예시

기계 처리 시간이

```text
[7, 10]
```

이고 작업이 `6개`라면,

시간 `28` 동안 첫 번째 기계는 4개, 두 번째 기계는 2개의 작업을 처리할 수 있다.

따라서 총 6개의 작업을 처리할 수 있고, 최소 시간은 `28`이다.

# 샘플 코드

```python
sample1 = [
    [7, 10],
    6
]
# 예상 결과: 28


sample2 = [
    [1, 2, 3],
    10
]
# 예상 결과: 6


sample3 = [
    [5],
    7
]
# 예상 결과: 35


sample4 = [
    [3, 8, 11],
    20
]
# 예상 결과: 33


def solution(times, m):
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
28
6
35
33
```
"""