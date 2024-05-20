from collections import deque

n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
# print(arr)

dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]


def bfs(q):
  max_t = -1
  visited = [[0 for _ in range(m)] for _ in range(n)]
  visited[q[0][0]][q[0][1]] = 1
  while q:
    # print(q)
    r, c, t = q.popleft()
    max_t = max(t, max_t)
    # print(max_t)
    for d in range(4):
      nr, nc = r + dr[d], c + dc[d]
      if -1 < nr < n and -1 < nc < m and arr[nr][nc] == 'L' and not visited[nr][nc]:
        visited[nr][nc] = 1
        q.append([nr, nc, t+1])
  return max_t

q = deque()
ans_t = -1
for i in range(n):
  for j in range(m):
    if arr[i][j] == 'L':
      if 0<=i-1<n and 0<=i+1<n:
        if arr[i-1][j] == 'L' and arr[i+1][j] == 'L': continue
      if 0<=j-1<m and 0<=j+1<m:
        if arr[i][j-1] == 'L' and arr[i][j-1] == 'L': continue
      q.append([i, j, 0])
      ans_t = max(ans_t, bfs(q))
print(ans_t)