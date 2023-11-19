import sys
input = sys.stdin.readline

N = int(input())

ans = 0
# arr = [[0 for _ in range(n)] for _ in range(n)]

def check(qr):
	for i in range(qr):
		# 좌우에 있거나, 대각선에 있다면 
		# TODO(여기서 기존 queen이 어떻게 적재되고 있는걸까?)
		if (arr[qr] == arr[i]) or (qr-i == abs(arr[qr] - arr[i])):
			return False
	return True

def dfs(qrow):
	global ans
	if qrow == N:
		ans += 1
		return
	
	# down
	for col in range(N):
		if visited[col] == 0:
			arr[qrow] = col
			# print(arr)
			# cnt += 1
			if check(qrow):
				visited[col] = 1
				dfs(qrow + 1)
				visited[col] = 0


arr = [0 for _ in range(N)]
visited = [0 for _ in range(N)]

dfs(0)

print(ans)