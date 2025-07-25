N = int(input())
M = int(input())

arr = [list(map(int, input().split(' '))) for _ in range(M)]
graph = [[] for _ in range(N+1)]
for a, b, dist in arr:
    graph[a].append([b, dist])
    # graph[b].append([a, dist])

used = [0] * (N+1)
INF = float("inf")
dist = [INF] * (N+1)
start, end = map(int, input().split(' '))
# print(start, end)
dist[start] = 0
parent = [0] * (N+1)

for _ in range(N):
    cur = -1
    min_dist = INF
    for i in range(1, N+1):
        if not used[i] and min_dist > dist[i]:
            min_dist = dist[i]
            cur = i
    if cur == -1:
        break
    used[cur] = 1

    for nxt, d in graph[cur]:
        if dist[nxt] > dist[cur] + d:
            dist[nxt] = dist[cur] + d
            parent[nxt] = cur
            
print(dist[end])

path = []
cur = end
while cur != 0:
    path.append(cur)
    cur = parent[cur]

print(len(path))
print(*path[::-1])