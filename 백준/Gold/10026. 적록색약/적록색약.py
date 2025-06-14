from collections import deque

N = int(input())
arr_rgb = [list(input().strip()) for _ in range(N)]
# print(arr)
arr_gb = [['G' if e == 'R' else e for e in row] for row in arr_rgb]
# print(arr_rgcb)

dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]

def bfs(q, visited, arr):
  visited[q[0][0]][q[0][1]] = 1
  col = arr[q[0][0]][q[0][1]]
  while q:
    r, c = q.popleft()
    for d in range(4):
      nr, nc = r + dr[d], c + dc[d]
      if(-1 < nr < N and -1 < nc < N):
        if not visited[nr][nc] and arr[nr][nc] == col:
          visited[nr][nc] = 1
          q.append([nr, nc])

def cnt_area(arr):
  visited = [[0 for _ in range(N)] for _ in range(N)]
  area = 0
  q = deque()
  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        q.append([i, j])
        bfs(q, visited, arr)
        area += 1
  return area

print(cnt_area(arr_rgb), cnt_area(arr_gb))