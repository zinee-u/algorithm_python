from collections import deque

m, n = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs(q, team):
	pwr = 1
	while q:
		r, c = q.popleft()
		for d in range(4):
			nr, nc = r + dr[d], c + dc[d]
			if -1 < nr < n and -1 < nc < m:
				if arr[nr][nc] == team and visited[nr][nc] == 0:
					visited[nr][nc] = 1
					pwr += 1
					q.append([nr, nc])
	
	return pwr

# main
pwr_w, pwr_b = 0, 0
sum_w, sum_b = 0, 0
q = deque()

for i in range(n):
	for j in range(m):
		if arr[i][j] == 'W' and visited[i][j] == 0:
			visited[i][j] = 1
			q.append([i, j])
			pwr_w = bfs(q, 'W')
			pwr_w **= 2
			sum_w += pwr_w
		elif arr[i][j] == 'B' and visited[i][j] == 0:
			visited[i][j] = 1
			q.append([i, j])
			pwr_b = bfs(q, 'B')
			pwr_b **= 2
			sum_b += pwr_b

print(sum_w, sum_b)