from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
grp = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
q = deque()
lst_g = []
def bfs(i, j, g):
    cnt_g = 1
    q.append([i, j, g])
    while q:
        r, c, g = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if -1 < nr < n and -1 < nc < n:
                if visited[nr][nc] == 0 and arr[nr][nc] == 1:
                    visited[nr][nc] = 1
                    grp[r][c] = g
                    grp[nr][nc] = g
                    q.append([nr, nc, g])
                    cnt_g += 1
    lst_g.append(cnt_g)

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            visited[i][j] = 1
            bfs(i, j, cnt)
print(cnt)

lst_g.sort()

for e in lst_g:
    print(e)