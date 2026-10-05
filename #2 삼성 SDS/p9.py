sample1 = [4, 7, 2, 9]
# 예상 결과: 16


sample2 = [5, 1, 1, 5]
# 예상 결과: 10


sample3 = [10, 2, 8, 3, 7]
# 예상 결과: 25


sample4 = [-5, -2, -7]
# 예상 결과: 0


sample5 = [6]
# 예상 결과: 6


sample6 = [3, 10, 3, 1, 2]
# 예상 결과: 12


# def solution(scores):
#     ln = len(scores)

#     dp = [[0] * ln for _ in range(ln)]

#     for i in range(ln):
#         dp[0][i] = max(0, scores[i])

#     if len(scores) == 1:
#         return dp[0][0]
    
#     for i in range(ln-1):
#         dp[1][i] = max(dp[0][i], dp[0][i+1])

#     if len(scores) == 2:
#         return dp[1][0]

#     for i in range(2, ln):
#         for j in range(ln - i):
#             dp[i][j] = max(dp[0][j] + dp[i-2][j+2], dp[i-1][j+1])

#     return dp[ln-1][0]

def solution(scores):
    ln = len(scores)
    
    dp = [0 for _ in range(ln)]

    # 이전 2개의 값만 저장해도 ok
    for i in range(ln):
        bbth = dp[i-2] if 2 <= i else 0
        bth = dp[i-1] if 1 <= i else 0
        ith = scores[i]
        dp[i] = max(bbth+ith, bth)

    return dp[-1]

ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)

ans = solution(sample5)
print(ans)

ans = solution(sample6)
print(ans)


"""
좋아. 이번에는 **DP로 이어지는 유형**으로 가자. 풀이 힌트 없이 문제와 샘플만 줄게.

# 문제. 최대 점수 선택

길이 `N`의 정수 배열 `scores`가 주어진다.

각 위치에는 하나의 점수가 있고, 원하는 위치를 선택해서 점수를 얻을 수 있다.

단, **서로 인접한 두 위치를 동시에 선택할 수는 없다.**

선택한 점수들의 합으로 만들 수 있는 최댓값을 반환하라.

## 조건

예를 들어:

```text
scores = [4, 7, 2, 9]
```

다음 선택은 가능하다.

```text
4와 2
4와 9
7과 9
```

하지만 다음 선택은 불가능하다.

```text
4와 7
7과 2
2와 9
```

서로 인접한 위치이기 때문이다.

아무 위치도 선택하지 않는 것도 허용된다.

## 제한 조건

```text
1 <= N <= 100000

-1000 <= scores[i] <= 10000
```

점수에는 음수가 포함될 수 있다.

## 샘플 코드

```python
sample1 = [4, 7, 2, 9]
# 예상 결과: 16


sample2 = [5, 1, 1, 5]
# 예상 결과: 10


sample3 = [10, 2, 8, 3, 7]
# 예상 결과: 25


sample4 = [-5, -2, -7]
# 예상 결과: 0


sample5 = [6]
# 예상 결과: 6


sample6 = [3, 10, 3, 1, 2]
# 예상 결과: 12


def solution(scores):
    pass


ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)

ans = solution(sample5)
print(ans)

ans = solution(sample6)
print(ans)
```

목표 출력:

```text
16
10
25
0
6
12
```
"""