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

def check(ls, X):
    length = len(ls)

    occupy = [0 for _ in range(length)]

    buff = ls[0]

    for i in range(1, length):
        if buff == ls[i]:
            continue

        if abs(buff - ls[i]) >= 2:
            return 0

        if ls[i] - buff == 1:
            if i < X:
                return 0

            for j in range(X):
                ni = i - 1 - j

                if ls[ni] != buff:
                    return 0

                if occupy[ni] == 1:
                    return 0

                occupy[ni] = 1

        else:
            if i + X > length:
                return 0

            for j in range(X):
                ni = i + j

                if ls[ni] != ls[i]:
                    return 0

                if occupy[ni] == 1:
                    return 0

                occupy[ni] = 1

        buff = ls[i]

    return 1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, X = map(int, input().split())

    ground = []
    for _ in range(N):
        ground.append(list(map(int, input().split())))

    res = 0
    for i in range(N):
        buff = ground[i]
        res += check(buff, X)

    for i in range(N):
        buff = [ls[i] for ls in ground]
        res += check(buff, X)

    print(f"#{test_case} {res}")
    # ///////////////////////////////////////////////////////////////////////////////////
