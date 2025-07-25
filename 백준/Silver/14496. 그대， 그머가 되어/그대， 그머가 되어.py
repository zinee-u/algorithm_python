from collections import deque
start, end = map(int, input().split(' '))
N, M = map(int, input().split(' '))
arr = [list(map(int, input().split(' '))) for _ in range(M)]

graph = [[] for _ in range(N+1)]

for n1, n2 in arr:
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [0] * (N+1)
q = deque()
q.append([start, 0])
visited[start] = 1

flag = 0
while q:
    cur, time = q.popleft()
    if cur == end:
        print(time)
        flag = 1
        break
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = 1
            q.append([nxt, time+1])
if flag == 0:
    print(-1)
