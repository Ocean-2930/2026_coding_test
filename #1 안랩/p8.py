sample1 = [
    [2, 1, 3, 2],
    2
]
# 1

sample2 = [
    [1, 1, 9, 1, 1, 1],
    0
]
# 5

sample3 = [
    [1],
    0
]
# 1

from collections import deque

def solution(priorities, location):
    ind = sorted(list(set(priorities)))[::-1]
    tar = deque()
    for i in range(len(ind)):
        tar.append(ind[i])

    pri_q = deque()
    ind_q = deque()
    for i in range(len(priorities)):
        pri_q.append(priorities[i])
        ind_q.append(i)

    flag = 1
    while 0 < len(pri_q):
        if pri_q[0] == tar[0]:
            if ind_q[0] == location:
                return flag

            pri_q.popleft()
            ind_q.popleft()

            if tar[0] not in pri_q:
                tar.popleft()

            flag += 1
        else:
            buff = pri_q.popleft()
            pri_q.append(buff)
            buff = ind_q.popleft()
            ind_q.append(buff)

    return None


ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)