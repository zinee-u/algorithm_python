import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    info = list(map(int, input().split()))
    node = info[0]
    for i in range(1, len(info) - 1, 2):
        next_node, dist = info[i], info[i + 1]
        graph[node].append((next_node, dist))


def dfs(node, dist_sum):
    visited[node] = 1
    global max_dist, farthest_node
    if dist_sum > max_dist:
        max_dist = dist_sum
        farthest_node = node
    for next_node, cost in graph[node]:
        if not visited[next_node]:
            dfs(next_node, dist_sum + cost)

visited = [False] * (V + 1)
max_dist = 0
farthest_node = 0
dfs(1, 0)


visited = [0 for _ in range(V + 1)]
max_dist = 0
dfs(farthest_node, 0)

print(max_dist)