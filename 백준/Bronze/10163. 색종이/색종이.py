from collections import deque
n = int(input())
pos = []
visited = [[0 for _ in range(1002)] for _ in range(1002)]



def bfs(q):
	cnt = 1
	ic, ir, w, h = q[0][0], q[0][1], q[0][2], q[0][3]
	visited[ir][ic] = 1
	# print("ic,",ic, ir, w, h)
	while q:
		c, r, w, h = q.popleft()
		for i in range(h):
			for j in range(w):
				nr, nc = r+i, c+j
				# print(nr, nc)
				if -1 < nr < ir+h and -1 < nc < ic+w:
					if not visited[nr][nc]:
						visited[nr][nc] = 1
						cnt += 1
						q.append([nc, nr, w, h])
			# print(q)
	return cnt

area = []
for _ in range(n):
	pos.append(list(map(int, input().split())))
	# print("pos=",pos)

for i in range(n-1, -1, -1):
	# print(pos[i][1], pos[i][0])
	q = deque()
	q.append(pos[i])
	area.append(bfs(q))
	# print(area)

for i in range(n-1, -1, -1):
	print(area[i])