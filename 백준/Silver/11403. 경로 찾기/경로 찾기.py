from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [[0 for _ in range(N)] for _ in range(N)]

def bfs(s):
    visited = [0 for _ in range(N)]
    q = deque()
    q.append(s)
    while q:
        n1 = q.popleft()
        for n2 in range(N):
            if arr[n1][n2] == 1 and not visited[n2]:
                visited[n2] = 1
                q.append(n2)
                ans[s][n2] = 1
    

    if visited[s]:
        ans[s][s] = 1

for i in range(N):
    bfs(i)

for row in ans:
    print(*row)