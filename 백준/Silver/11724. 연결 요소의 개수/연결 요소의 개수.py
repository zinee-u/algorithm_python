import sys
sys.setrecursionlimit(10**6)
# 시간초과 input() -> sys.stdin.readline()
# https://breakcoding.tistory.com/109
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
# print(graph)

def dfs(node1):
    visited[node1] = 1
    for node2 in graph[node1]:
        if visited[node2] == 0:
            dfs(node2)
        
cnt = 0
for v in range(1, n+1):
    if visited[v] == 0:
        dfs(v)
        cnt += 1

print(cnt)