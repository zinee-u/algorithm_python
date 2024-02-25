from heapq import heappop, heappush

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


sum_cost = 0


def bfs(q, n, graph, tc):
	# visited[0][0] = 1
	min_cost = float('INF')
	v = set()
	while q:
		cost, r, c = heappop(q)
		# print(cost, r, c)
		if r == (n-1) and c == (n-1):
			answer = "Problem %d: %d"
			
			return print(answer %(tc, cost))
			
		for d in range(4):
			nr, nc = r + dr[d], c + dc[d]
			# print(nr, nc)
			if -1 < nr < n and -1 < nc < n:
				# print(nr, nc)
				
				# print(v)
				if ((r, c, nr, nc) and (nr, nc, r, c)) not in v:
					v.add((r, c, nr, nc))
					v.add((nr, nc, r, c))
					heappush(q, [cost + graph[nr][nc], nr, nc])



# q.heappush(q, [0, 0, graph[0][0]])

n = -1
tc = 0
while n!= 0:
	n = int(input())
	if n == 0:
		break
	tc+=1
	# print(n)
	# visited = [[0 for _ in range(n)] for _ in range(n)]
	
	graph = [list(map(int, input().split(' '))) for _ in range(n)]
	# print(graph)
	q = [[graph[0][0], 0, 0]]
	bfs(q, n, graph, tc)
#min_cost 찾기
		