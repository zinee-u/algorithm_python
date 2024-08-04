from collections import deque

R, C, T = map(int, input().split())
# print(R,C,T)

arr = [list(map(int, input().split())) for _ in range(R)]
# print(arr)

posRobot = []
q = deque()


# find posRobot and dust
for i in range(R):
	for j in range(C):
		if arr[i][j] == -1:
			posRobot.append([i, j])
		elif arr[i][j] > 0:
			q.append([i, j, arr[i][j]])


dr, dc = [0, -1, 0, 1], [1, 0, -1, 0]

def diffusion(q):
		
	while q:
		r, c, dust = q.popleft()
		cnt = 0
		for d in range(4):
			nr, nc = r + dr[d], c + dc[d]
			if [nr, nc] in posRobot:
				continue
			if -1 < nr < R and -1 < nc < C:
				arr[nr][nc] += (dust//5)
				cnt += 1
		dust //= 5
		arr[r][c] = arr[r][c] - (dust*cnt)
		
		

def clean():
	#upper
	idx = 0
	r, c = posRobot[0][0], 0
	cleanDust = 0
	# print(r,c)
	while True:
		ur, uc = r + dr[idx], c + dc[idx]
		# print(ur, uc)
		# break
		if ur == posRobot[0][0] and uc == posRobot[0][1]:
			break
		if not(-1 < ur < R and -1 < uc < C):
			idx = (idx+1)%4
			continue
		arr[ur][uc], cleanDust = cleanDust, arr[ur][uc]
		r, c = ur, uc

	#lower
	idx = 0
	cleanDust = 0
	r, c = posRobot[1][0], 0
	# print(r,c)
	while True:
		lr, lc = r - dr[idx], c + dc[idx]
		# print(lr, lc)
		# break
		if lr == posRobot[1][0] and lc == posRobot[1][1]:
			break
		if not (-1 < lr < R and -1 < lc < C):
			idx = (idx+1)%4
			continue
		arr[lr][lc], cleanDust = cleanDust, arr[lr][lc]
		r, c = lr, lc
		
	
for _ in range(T):
	# diffusion
	diffusion(q)
	
	# clean
	clean()

	for i in range(R):
		for j in range(C):
			if arr[i][j]>0:
				q.append([i, j, arr[i][j]])

ans = 0
for i in range(R):
	for j in range(C):
		if arr[i][j] > 0:
			ans += arr[i][j]

print(ans)