from collections import deque

n = int(input())

start, end = map(int, input().split(' '))

m = int(input())

# p, c
graph = [[] for _ in range(n + 1)]
q = deque()

for _ in range(m):
	p, c = map(int, input().split(' '))
	graph[p].append(c)
	graph[c].append(p)

# print(graph)

v = [-1 for _ in range(n + 1)]


def bfs(root):
	q.append(root)
	v[root] = 0
	
	while q:
		p = q.popleft()
		if p == end:
			return

		for c in graph[p]:
			if v[c] == -1:
				v[c] = v[p] + 1
				q.append(c)

bfs(start)

print(v[end])