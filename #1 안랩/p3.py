sample1 = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"]
]
# 5

sample2 = [
    ["crow_mask", "face"],
    ["blue_sunglasses", "face"],
    ["smoky_makeup", "face"]
]
# 3


def solution(clothes):
    dct = {}

    for c in clothes:
        if c[1] not in dct:
            dct[c[1]] = 1
        else:
            dct[c[1]] += 1

    keylist = list(dct.keys())

    res = 0
    for i in range(1, 2 ** len(keylist)):
        cnt = 1
        flag = 0
        buff = i
        while 0 < buff:
            if buff % 2 == 1:
                cnt *= dct[keylist[flag]]

            flag +=1
            buff = buff // 2

        res += cnt
            
    return res


ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

"""
풀이
의상 조합을 a, b, c, 안입음 으로 잡고 전부 계산 후 -1 하기
"""