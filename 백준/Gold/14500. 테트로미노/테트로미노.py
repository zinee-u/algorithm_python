n, m = map(int, input().split())
# print(n)
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

dirArr = [
	[[0, 1, 2, 3], [0, 0, 0, 0]],#ㅣ
	[[0, 0, 0, 0], [0, 1, 2, 3]],#ㅡ
	[[0, 0, 1, 1], [0, 1, 0, 1]],#ㅁ
	[[0, 1, 1, 2], [0, 0, 1, 1]],#h
	[[0, 0, -1, -1], [0, 1, 1, 2]],#_|-
	[[0, -1, -1, -2], [0, 0, 1, 1]],#'h
	[[0, 0, 1, 1], [0, 1, 1, 2]],#-|_
	[[0, 0, 1, 0], [0, 1, 1, 2]],#ㅜ
	[[0, 1, 1, 2], [0, -1, 0, 0]],#ㅓ
	[[0, 0, -1, 0], [0, 1, 1, 2]],#ㅗ
	[[0, 1, 1, 2], [0, 0, 1, 0]],#ㅏ
	[[0, 1, 2, 2], [0, 0, 0, 1]], #L
	[[0, -1, -1, -1], [0, 0, 1, 2]], #'ㄱ
	[[0, 0, 1, 2], [0, 1, 1, 1]], #7
	[[0, 0, 0, -1], [0, 1, 2, 2]], #'ㄴ
	[[0, 0, -1, -2], [0, 1, 1, 1]], #'L
	[[0, 0, 0, 1], [0, 1, 2, 2]], #ㄱ
	[[0, -1, -2, -2], [0, 0, 0, 1]], #'7
	[[0, 1, 1, 1], [0, 0, 1, 2]], #ㄴ
]

def calNum(i, j):
	maxSum = 0
	for dr, dc in dirArr:
		sumB = 0
		valid = True
		for d in range(4):
			nr, nc = i + dr[d], j + dc[d]
			if(0<= nr <n and 0<= nc <m):
				sumB += arr[nr][nc]
			else:
				valid = False
				break
		if valid:
			maxSum = max(sumB,maxSum)
	return maxSum

retMax = 0
for i in range(n):
	for j in range(m):
		retMax = max(calNum(i, j),retMax)

print(retMax)
