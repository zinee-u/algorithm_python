import sys
from collections import deque

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(arr)

max_val = max(map(max, arr))
# print(max_val)
# Sujin LOVE
# LOVE SUJIN

dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]
max_cnt = -1

def bfs(q):
  while q:
    r, c, cnt = q.popleft()
    for d in range(4):
      nr, nc = r + dr[d], c + dc[d]
      if(-1 < nr < N and -1 < nc < N and visited[nr][nc] == 0):
        if arr[nr][nc] >= h:
          visited[nr][nc] = cnt
          q.append([nr, nc, cnt])

for h in range(1, max_val+1):
  q = deque()
  cnt = 1
  # print("height = ", h)
  visited = [[0 for _ in range(N)] for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if arr[i][j] >= h and visited[i][j] == 0:
        visited[i][j] = cnt
        q.append([i, j, cnt])
        bfs(q)
        cnt += 1
        # print(cnt)
      # print(visited)
  max_cnt = max(max_cnt, max(map(max, visited)))
print(max_cnt)