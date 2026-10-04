sample1 = [["119", "97674223", "1195524421"]]
# False

sample2 = [["123", "456", "789"]]
# True

sample3 = [["12", "123", "1235", "567", "88"]]
# False


def solution(phone_book):
    ln = len(phone_book)

    for i in range(ln):
        al = len(phone_book[i])

        j = 0
        while i + j + 1 < ln:
            j += 1
            bl = len(phone_book[i + j])

            if al == bl:
                continue

            ref = ""
            tar = ""
            subln = 0
            if bl < al:
                subln = bl
                ref = phone_book[i + j]
                tar = phone_book[i]
            else:
                subln = al
                ref = phone_book[i]
                tar = phone_book[i + j]

            if ref == tar[:subln]:
                return False

    return True

ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)

"""
풀이 #1
hash 사용

set(phone_number)
>
for n in phone_number
>
for i in range(len(n)):
>
if n[:i] in set:


풀이 #2
sort 사용
phone_number.sort()
>
for i in range(1, len(phone_number))
>
if phone_number[i].startswith(phone_number[i-1]):

"""