# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / "sample_input.txt", "r")

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

change = [
    [],
    [2, 3, 1, 0],
    [1, 3, 0, 2],
    [3, 2, 0, 1],
    [2, 0, 3, 1],
    [2, 3, 0, 1]
]

def crash(hole, tiletype, x, y, nx, ny, direction):
    match tiletype:
        case 0:
            return nx, ny, direction, 0

        case 1 | 2 | 3 | 4 | 5:
            return nx, ny, change[tiletype][direction], 1

        case 6 | 7 | 8 | 9 | 10:
            hx, hy = hole[(nx, ny)]
            return hx, hy, direction, 0

    return nx, ny, direction, 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())

    board = [[5 for _ in range(n+2)]]
    for _ in range(n):
        board.append([5] + [int(c) for c in input().split()] + [5])
    board.append([5 for _ in range(n+2)])

    holes = dict()

    buff = [[] for _ in range(5)]
    for i in range(n):
        for j in range(n):
            k = board[i+1][j+1]
            if not (6 <= k <= 10):
                continue

            buff[k-6].append((j + 1, i + 1))

    for b in buff:
        if len(b) != 2:
            continue

        holes[b[0]] = b[1]
        holes[b[1]] = b[0]

    res = 0
    for i in range(n):
        for j in range(n):
            if board[i+1][j+1] != 0:
                continue

            for k in range(len(directions)):
                sx = j + 1
                sy = i + 1

                x = j + 1
                y = i + 1
                d = k

                score = 0
                while True:
                    if board[y+directions[d][1]][x+directions[d][0]] == -1 or (((x+directions[d][0]) == sx) and (y+directions[d][1] == sy)):
                        break

                    nx, ny, nd, ns = crash(holes, board[y+directions[d][1]][x+directions[d][0]], x, y, x+directions[d][0], y+directions[d][1], d)
                    x = nx
                    y = ny
                    d = nd
                    score += ns

                if res < score:
                    res = score

    print(f"#{test_case} {res}")

    # ///////////////////////////////////////////////////////////////////////////////////
