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
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.stdin = open(BASE_DIR / "sample_input.txt", "r")


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

def valid(N, coordinate):
    return (0 <= coordinate[0] < N) and (0 <= coordinate[1] < N)

def multicheck(board, ex, start, end):
    ls = abs(start[0] - end[0])
    direction = (((end[0] - start[0]) // ls) , ((end[1] - start[1]) // ls))

    for i in range(1, ls):
        t = board[start[0] + direction[0]*i][start[1] + direction[1]*i]
        
        if t in ex:
            return False
        
        ex.add(t)

    return True

def squarecheck(board, a, b, c, d):
    ls = set()

    ls.add(board[a[0]][a[1]])
    ls.add(board[b[0]][b[1]])
    ls.add(board[c[0]][c[1]])
    ls.add(board[d[0]][d[1]])

    if len(ls) != 4:
        return False

    if not multicheck(board, ls, a, b):
        return False

    if not multicheck(board, ls, b, d):
        return False

    if not multicheck(board, ls, d, c):
        return False

    if not multicheck(board, ls, c, a):
        return False

    return True

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    res = -1

    d1 = (1, -1)
    d2 = (1, 1)
    for i in range(N):
        for j in range(N):
            a = (i, j)

            x = 1
            while True:
                b = (i + d1[0] * x, j + d1[1] * x)
                if not valid(N, b):
                    break

                y = 1
                while True:
                    c = (i + d2[0] * y, j + d2[1] * y)
                    d = (c[0] + d1[0] * x, c[1] + d1[1] * x)

                    if not valid(N, c):
                        break

                    if not valid(N, d):
                        break

                    if 2 * x + 2 * y > res:
                        if squarecheck(board, a, b, c, d):
                            res = 2 * x + 2 * y

                    y += 1

                x += 1

    print(f"#{test_case} {res}")
    # ///////////////////////////////////////////////////////////////////////////////////
