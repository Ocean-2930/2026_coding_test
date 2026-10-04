sample1 = [
    [0, 3],
    [1, 9],
    [2, 6]
]
# 예상 결과: [0, 2, 1]


sample2 = [
    [1, 2],
    [2, 4],
    [3, 2],
    [4, 1]
]
# 예상 결과: [0, 2, 3, 1]


sample3 = [
    [5, 2],
    [5, 2],
    [5, 1],
    [20, 1]
]
# 예상 결과: [2, 0, 1, 3]


sample4 = [
    [10, 3]
]
# 예상 결과: [0]

import heapq

def solution(tasks):
    q = []

    for i in range(len(tasks)):
        heapq.heappush(q, (tasks[i][0], tasks[i][1], i))

    res = []
    time = 0
    memq = []
    while True:
        while 0 < len(q):
            if time < q[0][0]:
                break

            buff = heapq.heappop(q)
            heapq.heappush(memq, (buff[1], buff[0], buff[2]))

        if not memq:
            if not q:
                break

            buff = heapq.heappop(q)
            heapq.heappush(memq, (buff[1], buff[2]))
            time = buff[0]

        task = heapq.heappop(memq)

        time += task[0]

        res.append(task[2])
                

    return res


ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)

"""
좋아. 이번에는 **우선순위 큐를 직접 떠올릴 수 있는 유형**으로 가보자. 풀이 힌트 없이 문제와 실행 가능한 샘플만 줄게.

# 문제. 작업 처리 센터

하나의 작업 처리 센터가 있다.

센터에는 여러 개의 작업 요청이 들어오며, 각 작업은 다음 세 값을 가진다.

```text
요청 시각
소요 시간
작업 번호
```

센터에는 작업을 처리할 수 있는 서버가 하나뿐이다.

서버는 한 번 작업을 시작하면 해당 작업이 끝날 때까지 다른 작업을 처리할 수 없다.

## 작업 선택 규칙

서버가 비어 있는 시점에, 이미 요청이 들어와 대기 중인 작업들 가운데 다음 우선순위에 따라 하나를 선택한다.

1. 소요 시간이 짧은 작업
2. 소요 시간이 같다면 작업 번호가 작은 작업

선택된 작업은 즉시 실행한다.

## 대기 중인 작업이 없는 경우

현재 시각에 처리 가능한 작업이 하나도 없다면, 서버는 다음 작업이 요청되는 시각까지 아무 일도 하지 않는다.

## 반환값

모든 작업을 처리했을 때, 작업이 실제로 실행된 순서대로 작업 번호를 배열에 담아 반환하라.

## 제한 조건

```text
1 <= 작업 개수 <= 100000

0 <= 요청 시각 <= 1000000000
1 <= 소요 시간 <= 1000000000

작업 번호는 0부터 시작하며,
입력 배열에서의 인덱스와 동일하다.
```

입력은 다음 형태다.

```python
tasks[i] = [request_time, processing_time]
```

작업 번호는 자동으로 `i`가 된다.

# 샘플 코드

```python
sample1 = [
    [0, 3],
    [1, 9],
    [2, 6]
]
# 예상 결과: [0, 2, 1]


sample2 = [
    [1, 2],
    [2, 4],
    [3, 2],
    [4, 1]
]
# 예상 결과: [0, 2, 3, 1]


sample3 = [
    [5, 2],
    [5, 2],
    [5, 1],
    [20, 1]
]
# 예상 결과: [2, 0, 1, 3]


sample4 = [
    [10, 3]
]
# 예상 결과: [0]


def solution(tasks):
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

목표 출력은 다음과 같다.

```text
[0, 2, 1]
[0, 2, 3, 1]
[2, 0, 1, 3]
[0]
```

이제 직접 풀어봐. 코드 보내면 이전과 동일하게 **정확성, 반례, 경계 조건, 시간복잡도, Python 구현 문제** 순서로 볼게.
"""