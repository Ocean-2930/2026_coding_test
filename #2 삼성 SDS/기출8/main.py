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

neighbors = [
    [-1, 1],
    [0, 2],
    [1, 3],
    [2, -1]
]

def rotate(f, t):
    return (f + t + 800) % 8

def spin(focus, magnets, target, direction, spinfrom):
    global neighbors
    
    if spinfrom != 1:
        if neighbors[target][1] != -1:
            ngear = neighbors[target][1]
            if magnets[ngear][rotate(focus[ngear], -2)] != magnets[target][rotate(focus[target], 2)]:
                spin(focus, magnets, ngear, -1 * direction, -1)

    if spinfrom != -1:
        if neighbors[target][0] != -1:
            ngear = neighbors[target][0]
            if magnets[ngear][rotate(focus[ngear], 2)] != magnets[target][rotate(focus[target], -2)]:
                spin(focus, magnets, ngear, -1 * direction, 1)

    focus[target] = rotate(focus[target], -direction)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    K = int(input())

    focus = [0 for _ in range(4)]
    magnets = []
    for _ in range(4):
        magnets.append(list(map(int, input().split())))

    spins = []
    for _ in range(K):
        spins.append(list(map(int, input().split())))

    for s in spins:
        spin(focus, magnets, s[0] - 1, s[1], 0)

    res = 0
    p = 1
    for i in range(4):
        res += p * magnets[i][focus[i]]
        p = p + p

    print(f"#{test_case} {res}")
    # ///////////////////////////////////////////////////////////////////////////////////
