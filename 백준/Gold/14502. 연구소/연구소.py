from collections import deque
import copy

N, M = map(int, input().split())
# print(N, M)
arr = [list(map(int, input().split())) for _ in range(N)]

dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]


def bfs(pos_virus, v):
  q = deque()
  for i, j in pos_virus:
    q.append([i, j])
  while q:
    r, c = q.popleft()
    for d in range(4):
      nr, nc = r+dr[d], c+dc[d]
      if -1 < nr < N and -1 < nc < M:
        if v[nr][nc] == 0:
          v[nr][nc] = 2
          q.append([nr, nc])
  return v


#Choose 3-position

def recur(idx, cnt):
  global pos_virus, max_cnt, pos, cnt_empty, lst
  
  if cnt == 3:
    v = copy.deepcopy(arr)
    for i, j in lst:
      v[i][j] = 1
    res_arr = bfs(pos_virus, v)
    cnt = 0
    for i in range(N):
      for j in range(M):
        if res_arr[i][j] == 0:
          cnt += 1
    max_cnt = max(cnt, max_cnt)
    return

  if idx == cnt_empty:
    return

  lst.append(pos[idx])
  recur(idx+1, cnt+1)
  lst.pop()
  recur(idx+1, cnt)

q = deque()

pos = []
lst = []
pos_virus=[]
max_cnt = -1
cnt_empty = 0

for i in range(N):
  for j in range(M):
    if arr[i][j] == 0:
      pos.append([i, j])
      cnt_empty += 1
    if arr[i][j] == 2:
      pos_virus.append([i,j])

# print(q)


recur(0, 0)

print(max_cnt)