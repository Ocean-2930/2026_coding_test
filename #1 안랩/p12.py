sample1 = [
    9,
    [
        [1, 3],
        [2, 3],
        [3, 4],
        [4, 5],
        [4, 6],
        [4, 7],
        [7, 8],
        [7, 9]
    ]
]
# 1

sample2 = [
    4,
    [
        [1, 2],
        [2, 3],
        [3, 4]
    ]
]
# 0

sample3 = [
    7,
    [
        [1, 2],
        [2, 7],
        [3, 7],
        [3, 4],
        [4, 5],
        [6, 7]
    ]
]
# 1

class NodeClass:
    def __init__(self):
        self.connected = 0
        self.wires = []

    def add_wire(self, w):
        self.wires.append(w)

    def connect(self, k):
        if self.connected == k:
            return 0

        self.connected = k

        res = 1
        for w in self.wires:
            res += w.connect(self, k)
        return res

class WireClass:
    def __init__(self, n1, n2):
        self.node1 = n1
        self.node2 = n2
        self.connected = True

    def connect(self, n, k):
        if not self.connected:
            return 0

        if self.node1 == n:
            tar = self.node2
        elif self.node2 == n:
            tar = self.node1
        else:
            return 0

        return tar.connect(k)

def solution(n, wires):
    nodes = []
    for _ in range(n):
        nodes.append(NodeClass())

    wlist = []
    for w in wires:
        n1 = nodes[w[0]-1]
        n2 = nodes[w[1]-1]

        buff = WireClass(n1, n2)
        wlist.append(buff)

        n1.add_wire(buff)
        n2.add_wire(buff)

    res = -1
    for i, w in enumerate(wlist):
        w.connected = False

        cnt = []

        for node in nodes:
            con = node.connect(i+1)
            if con != 0:
                cnt.append(con)

        buff = abs(cnt[0] - cnt[1])

        if res == -1:
            res = buff

        if buff < res:
            res = buff

        w.connected = True

    return res



ans = solution(*sample1)
print(ans)

ans = solution(*sample2)
print(ans)

ans = solution(*sample3)
print(ans)

"""
DFS: Depth First Search
재귀적으로 깊게 들어가는 경로 우선 탐색

BFS: Breadth First Search
큐를 활용해서 가까운 노드들을 너비 우선 탐색
"""