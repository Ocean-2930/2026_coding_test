sample1 = [
    [1, 4, 7, 10],
    12
]
# 예상 결과: 11


sample2 = [
    [-5, -2, 3, 8, 12],
    1
]
# 예상 결과: 1


sample3 = [
    [5, 5, 5, 5],
    9
]
# 예상 결과: 10


sample4 = [
    [-10, -4, 1, 6, 9],
    4
]
# 예상 결과: 5


sample5 = [
    [1, 2, 8, 9],
    10
]
# 예상 결과: 10


def solution(arr, target):
    sarr = sorted(arr)

    low = 0
    high = len(arr) - 1
    highres = sarr[low] + sarr[high]
    highscore = abs(highres - target)

    while low < high:
        res = sarr[low] + sarr[high]
        score = abs(res - target)

        if score == 0:
            return res

        if score < highscore:
            highres = res
            highscore = score

        if score == highscore and res < highres:
            highres = res

        if res < target:
            low += 1

        if target < res:
            high -= 1

    return highres


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
좋아. 이번에는 **투포인터로 이어질 수 있는 유형**으로 가자. 풀이 힌트 없이 문제와 샘플만 줄게.

# 문제. 목표 합에 가장 가까운 두 수

길이 `N`의 정수 배열 `arr`와 목표값 `target`이 주어진다.

배열에서 서로 다른 두 원소를 하나씩 선택했을 때, 두 수의 합이 `target`과 가장 가까워지도록 하려고 한다.

두 수의 합과 `target`의 차이의 절댓값이 최소가 되도록 하는 두 수의 합을 반환하라.

## 조건

두 원소는 반드시 서로 다른 인덱스에서 선택해야 한다.

정답이 여러 개 존재한다면, 그중 두 수의 합이 더 작은 값을 반환한다.

## 제한 조건

```text
2 <= N <= 200000

-1000000000 <= arr[i] <= 1000000000

-2000000000 <= target <= 2000000000
```

배열에는 중복된 값이 존재할 수 있다.

## 예시

```text
arr = [1, 4, 7, 10]
target = 12
```

가능한 합 중 일부는 다음과 같다.

```text
1 + 4 = 5
1 + 10 = 11
4 + 7 = 11
4 + 10 = 14
```

`target = 12`와 가장 가까운 합은 `11`이므로 `11`을 반환한다.

# 샘플 코드

```python
sample1 = [
    [1, 4, 7, 10],
    12
]
# 예상 결과: 11


sample2 = [
    [-5, -2, 3, 8, 12],
    1
]
# 예상 결과: 1


sample3 = [
    [5, 5, 5, 5],
    9
]
# 예상 결과: 10


sample4 = [
    [-10, -4, 1, 6, 9],
    4
]
# 예상 결과: 5


sample5 = [
    [1, 2, 8, 9],
    10
]
# 예상 결과: 10


def solution(arr, target):
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
11
1
10
5
10
```
"""