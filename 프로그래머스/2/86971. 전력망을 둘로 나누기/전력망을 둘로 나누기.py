from collections import deque

def solution(n, wires):
	answer = float("INF")
	graph = [[] for _ in range(n + 1)]
	q = deque()
	
	for w in wires:			
		n1, n2 = map(int, w)
		graph[n1].append(n2)
		graph[n2].append(n1)

	for i in range(n-1):
		node = wires[i][1]
		q.append([i, node])
		answer = min(bfs(q, graph, n, wires), answer)
	return answer


def bfs(q, graph, n, wires):
	area = 1
	visited = [0 for _ in range(n + 1)]
	visited[q[0][1]] = 1
	
	while q:
		e, n1 = q.popleft()
		for n2 in graph[n1]:
			if (wires[e][0] == n1 and wires[e][1] == n2) or (wires[e][0] == n2 and wires[e][1] == n1):
				continue
			if visited[n2] == 1: continue
			area += 1
			q.append([e, n2])
			visited[n2] = 1

	diff = abs(n-2*area)
	return diff