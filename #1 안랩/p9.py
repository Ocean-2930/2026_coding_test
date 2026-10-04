sample1 = [6, 10, 2]
# "6210"

sample2 = [3, 30, 34, 5, 9]
# "9534330"

sample3 = [0, 0, 0, 0]
# "0"

sample4 = [12, 121]
# "12121"


from functools import cmp_to_key

def diff(a, b):
    return -1 if (int(a + b) > int(b + a)) else 1


def solution(numbers):
    buff = []
    for n in numbers:
        buff.append(str(n))

    buff.sort(key=cmp_to_key(diff))
    res = "".join(buff)

    return str(int(res))


ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)