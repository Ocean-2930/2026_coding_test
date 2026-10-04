sample1 = "AAAAE"
# 6

sample2 = "AAAE"
# 10

sample3 = "I"
# 1563

sample4 = "EIO"
# 1189

ind = 1
vowels = ["A", "E", "I", "O", "U"]

def find_index(target, word):
    global ind, vowels

    if target == word:
        return True

    if len(word) != 5:
        for w in vowels:
            ind += 1
            if find_index(target, word + w):
                return True

    return False

    

def solution(word):
    global ind
    ind = 0

    find_index(word, "")

    return ind

ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)