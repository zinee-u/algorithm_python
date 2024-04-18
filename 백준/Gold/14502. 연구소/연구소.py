from collections import deque
import copy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited_w = [[0 for _ in range(m)] for _ in range(n)]

dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]

# 0b 1w 2v

q = deque()
				

lst = []
max_area = 0


def dfs(dep):
	if dep == 3:
		# print(visited_w)
		
		bfs(visited_w)
		return

	for i in range(n):
		for j in range(m):
			if arr[i][j] == 0 and not visited_w[i][j]:
				visited_w[i][j] = 1
				dfs(dep + 1)
				visited_w[i][j] = 0


def bfs(visited_w):
	global max_area
	cp_arr = copy.deepcopy(arr)
	visited_v = [[0 for _ in range(m)] for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if visited_w[i][j] == 1:
				cp_arr[i][j] = 1
			if cp_arr[i][j] == 2 and not visited_v[i][j]:
				q.append([i, j])
				visited_v[i][j] = 1
	
	while q:
		r, c = q.popleft()
		for d in range(4):
			nr, nc = r + dr[d], c + dc[d]
			if -1 < nr < n and -1 < nc < m and cp_arr[nr][nc] == 0 and not visited_v[nr][nc]:
				cp_arr[nr][nc] = 2
				visited_v[nr][nc] = 1
				q.append([nr, nc])

	# print(cp_arr)
	cnt = 0
	for i in range(n):
		for j in range(m):
			if cp_arr[i][j] == 0:
				cnt += 1
				max_area = max(max_area, cnt)
	
# main

dfs(0)

print(max_area)