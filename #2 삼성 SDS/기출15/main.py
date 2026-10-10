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

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]    
]

def dfs(board, visit, N, K, usek, current_point, current_len):
    global directions
    
    res = -1
    for d in directions:
        nx = current_point[0] + d[0]
        ny = current_point[1] + d[1]

        if not ((0 <= nx < N) and (0 <= ny < N)):
            continue

        if visit[nx][ny] == 1:
            continue

        if board[current_point[0]][current_point[1]] <= board[nx][ny] - K:
            continue

        nu = 1 if board[current_point[0]][current_point[1]] <= board[nx][ny] else 0

        if nu == 1 and usek == 1:
            continue

        nb = [l[:] for l in board]
        if nu == 1:
            nb[nx][ny] = board[current_point[0]][current_point[1]] - 1
        
        nv = [l[:] for l in visit]
        nv[nx][ny] = 1

        buff = dfs(nb, nv, N, K, 1 if usek == 1 or nu == 1 else 0, (nx, ny), current_len + 1)

        if res < buff:
            res = buff

    if res != -1:
        return res

    return current_len

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    m = 0
    sp = []
    for i in range(N):
        for j in range(N):
            if m < board[i][j]:
                m = board[i][j]
                sp = [(i, j)]
            elif m == board[i][j]:
                sp.append((i, j))

    res = -1
    
    for s in sp:
        vs = [[0 for _ in range(N)] for _ in range(N)]
        vs[s[0]][s[1]] = 1

        ln = dfs(board, vs, N, K, 0, s, 1)
        if res < ln:
            res = ln

    print(f"#{test_case} {res}")
    # ///////////////////////////////////////////////////////////////////////////////////
