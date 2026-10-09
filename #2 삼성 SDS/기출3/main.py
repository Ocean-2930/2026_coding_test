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



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m, K = map(int, input().split())

    dead = set()
    alive = {}

    for y in range(n):
        row = list(map(int, input().split()))

        for x in range(m):
            if row[x] != 0:
                life = row[x]

                alive[(x, y)] = (
                    0,
                    life,
                    life + life
                )

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    for hour in range(K):
        born = {}
        dead_buffer = set()

        for pos in alive:
            start_time, active_time, death_time = alive[pos]

            life = active_time - start_time

            if active_time == hour:

                for dx, dy in directions:
                    next_pos = (
                        pos[0] + dx,
                        pos[1] + dy
                    )

                    if next_pos in alive or next_pos in dead:
                        continue

                    if next_pos in born:
                        born[next_pos] = max(
                            born[next_pos],
                            life
                        )
                    else:
                        born[next_pos] = life

            if death_time <= hour + 1:
                dead_buffer.add(pos)

        for pos in dead_buffer:
            dead.add(pos)
            alive.pop(pos)

        birth_time = hour + 1

        for pos, life in born.items():
            alive[pos] = (
                birth_time,
                birth_time + life,
                birth_time + life * 2
            )

    print(f"#{test_case} {len(alive)}")

    # ///////////////////////////////////////////////////////////////////////////////////
