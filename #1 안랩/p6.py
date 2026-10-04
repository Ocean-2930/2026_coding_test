sample1 = "()()"
# True

sample2 = "(())()"
# True

sample3 = ")()("
# False

sample4 = "(()("
# False


def solution(s):
    depth = 0

    for c in s:
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1

        if depth < 0:
            return False

    return depth == 0


ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)

ans = solution(sample4)
print(ans)