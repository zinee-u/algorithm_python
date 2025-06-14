import sys
import copy
from collections import deque
N = int(input())
arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
arr2 = copy.deepcopy(arr)
for i in range(N):
  for j in range(N):
    if arr2[i][j] == 'R':
      arr2[i][j] = 'G'
# print(arr2)
# print(arr)
# 색약 빨초2 파1 정상 빨3 파2 초1

dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]
q1 = deque()
q2 = deque()
visited1 = [[0 for _ in range(N)] for _ in range(N)]
visited2 = [[0 for _ in range(N)] for _ in range(N)]
area_able, area_disable = 0, 0

def bfs(q):
  while q:
    r, c, cnt, col, eye = q.popleft()
    for d in range(4):
      nr, nc = r + dr[d], c + dc[d]
      if -1 < nr < N and -1 < nc < N:
        # able
        if eye == 1:
          if visited1[nr][nc] == 0:
            if arr[nr][nc] == col:
              visited1[nr][nc] = cnt
              q.append([nr, nc, cnt, col, 1])
        #disable
        if eye == 2:
          if visited2[nr][nc] == 0:
            if arr2[nr][nc] == col:
              visited2[nr][nc] = cnt
              q.append([nr, nc, cnt, col, 2])
            
cnt, cnt2 = 1, 1
for i in range(N):
  for j in range(N):
    if visited1[i][j] == 0:
      if arr[i][j] == 'R':
        visited1[i][j] = cnt
        q1.append([i, j, cnt, 'R', 1])
        bfs(q1)
      elif arr[i][j] == 'G':
        visited1[i][j] = cnt
        q1.append([i, j, cnt, 'G', 1])
        bfs(q1)
      else:
        visited1[i][j] = cnt
        q1.append([i, j, cnt, 'B', 1])
        bfs(q1)
      cnt += 1
      # print(visited1)
    if visited2[i][j] == 0:
      if arr2[i][j] == 'B':
        visited2[i][j] = cnt2
        q2.append([i, j, cnt2, 'B', 2])
        bfs(q2)
      else:
        visited2[i][j] = cnt2
        q2.append([i, j, cnt2, 'G', 2])
        bfs(q2)
      cnt2+=1
    # print(visited2)

area_able = max(map(max, visited1))
area_disable = max(map(max, visited2))

print(area_able, area_disable)