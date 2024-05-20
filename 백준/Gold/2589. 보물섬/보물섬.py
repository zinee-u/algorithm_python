from collections import deque

n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
# print(arr)

dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]


# 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다



# print(dist)


# # 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력



# # tmp_d = float("INF")

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
      q.append([i, j, 0])
      ans_t = max(ans_t, bfs(q))
print(ans_t)