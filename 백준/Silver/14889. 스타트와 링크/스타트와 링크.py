N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

nT = N//2
# visited = [[0 for _ in range(N)] for _ in range(N)]
visited = [0 for _ in range(N)]
answer = []
def dfs(depth):
	global answer
	if sum(visited) == nT:
		sumA, sumB = 0, 0
		for i in range(N-1):
			for j in range(i+1, N):
				teamA = visited[i] + visited[j]
				#TeamA
				if teamA == 2:
					sumA += arr[i][j]
					sumA += arr[j][i]
				elif teamA == 0:
					#TeamB
					sumB += arr[i][j]
					sumB += arr[j][i]
		
		answer.append(abs(sumA - sumB))
		return
				
	else:
		for i in range(depth, N):
			# if not visited[i]:
			visited[i] = 1
			dfs(i + 1)
			visited[i] = 0

dfs(0)
print(min(answer))