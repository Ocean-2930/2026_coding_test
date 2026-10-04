sample1 = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]
# 11

sample2 = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1]
]
# -1

sample3 = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
]
# 5

def validate(maps, x, y):
    return 0 <= x and 0 <= y and x < len(maps[0]) and y < len(maps)

def floodfill(maps, dist, x, y, depth):
    if not validate(maps, x, y):
        return

    if maps[y][x] == 0:
        return

    if dist[y][x] != -1:
        if dist[y][x] <= depth:
            return

    dist[y][x] = depth

    floodfill(maps, dist, x+1, y, depth + 1)
    floodfill(maps, dist, x, y+1, depth + 1)
    floodfill(maps, dist, x-1, y, depth + 1)
    floodfill(maps, dist, x, y-1, depth + 1)


def mysolution(maps):
    dist = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    floodfill(maps, dist, 0, 0, 1)

    return dist[-1][-1]


from collections import deque

def solution(maps):
    dist = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    q = deque()
    q.append((0, 0))
    dist[0][0] = 1

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not validate(maps, nx, ny):
                continue

            if maps[ny][nx] == 0:
                continue

            if dist[ny][nx] != -1:
                continue

            dist[ny][nx] = dist[y][x] + 1
            q.append((nx, ny))

    return dist[-1][-1]


ans = solution(sample1)
print(ans)

ans = solution(sample2)
print(ans)

ans = solution(sample3)
print(ans)