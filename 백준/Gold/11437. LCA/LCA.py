import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(100000)
input = sys.stdin.read

def dfs(node, parent, depth):
    depths[node] = depth
    parents[node][0] = parent
    for next_node in tree[node]:
        if next_node != parent:
            dfs(next_node, node, depth + 1)

def set_parent():
    for j in range(1, LOG):
        for i in range(1, N + 1):
            if parents[i][j - 1] != -1:
                parents[i][j] = parents[parents[i][j - 1]][j - 1]

def lca(a, b):
    if depths[a] > depths[b]:
        a, b = b, a
    
    for i in range(LOG - 1, -1, -1):
        if depths[b] - depths[a] >= (1 << i):
            b = parents[b][i]
    
    if a == b:
        return a
    
    for i in range(LOG - 1, -1, -1):
        if parents[a][i] != parents[b][i]:
            a = parents[a][i]
            b = parents[b][i]
    
    return parents[a][0]

input_data = input().split()
index = 0

N = int(input_data[index])
index += 1

tree = defaultdict(list)

for _ in range(N - 1):
    u = int(input_data[index])
    v = int(input_data[index + 1])
    index += 2
    tree[u].append(v)
    tree[v].append(u)

M = int(input_data[index])
index += 1

pairs = []
for _ in range(M):
    a = int(input_data[index])
    b = int(input_data[index + 1])
    index += 2
    pairs.append((a, b))

LOG = int(math.log2(N)) + 1
depths = [0] * (N + 1)
parents = [[-1] * LOG for _ in range(N + 1)]

dfs(1, -1, 0)
set_parent()

results = []
for a, b in pairs:
    results.append(lca(a, b))

for result in results:
    print(result)
