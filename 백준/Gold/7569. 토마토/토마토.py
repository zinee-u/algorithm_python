import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

q = deque()
arr = []

for k in range(h):
    tmp = []
    for i in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for j in range(m):
            if tmp[i][j] == 1: q.append([k,i,j])
    arr.append(tmp)

dr, dc, dh = (0, -1, 0, 1, 0, 0), (-1, 0, 1, 0, 0, 0), (0, 0, 0, 0, -1, 1)

def bfs():
    while q:
        z, r, c = q.popleft()
        for d in range(len(dr)):
            nz, nr, nc = z + dh[d], r + dr[d], c + dc[d]
            if -1 < nz < h and -1 < nr < n and -1 < nc < m and arr[nz][nr][nc] == 0:
                arr[nz][nr][nc] = arr[z][r][c] + 1
                q.append([nz, nr, nc])

bfs()
result, flag = 0, False

for i in arr:
    for j in i:
        if 0 in j: flag = True
        result = max(result, max(j))

print(-1) if flag else print(result-1)