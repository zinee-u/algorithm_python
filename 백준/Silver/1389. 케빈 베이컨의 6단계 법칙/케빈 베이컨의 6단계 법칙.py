from collections import deque

n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(m)]
# print(arr)
graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1 - 1].append(v2 - 1)
    graph[v2 - 1].append(v1 - 1)


def bfs(node):
    visited = [-1 for _ in range(n)]
    q = deque()
    q.append(node)
    visited[node] = 0

    while q:
        start = q.popleft()
        for end in graph[start]:
            if visited[end] == -1:
                visited[end] = visited[start] + 1
                q.append(end)
    min_kevin = sum(visited)
    return min_kevin

min_dist = float("INF")
ans = 0
for i in range(n):
    kevin = bfs(i)
    if kevin < min_dist:
        min_dist = kevin
        ans = i + 1

print(ans)