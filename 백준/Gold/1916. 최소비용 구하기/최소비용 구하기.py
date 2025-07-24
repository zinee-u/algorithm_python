import sys
from heapq import heappop, heappush
# input = sys.stdin.readline

n = int(input()) # city
m = int(input()) # bus

# sys.stdin.readline().split()

data = list(map(int, sys.stdin.readline().split(' ')) for _ in range(m))
# print(data)
# arr, dst = map(int, input().split(' '))
INF = float('inf')
graph = [[] for _ in range(n)]

# print(graph)
lst_cost = [INF for _ in range(n)]
visited = [False for _ in range(n)]

# node1 <-> node2
# graph[node1] = node2

for start, end, cost in data:
	# print(start, end, cost)
	graph[start - 1].append([end - 1, cost])


S, E = map(int, input().split(' '))


# print(graph)
# Start
# lst_cost[0] = 0

#Start=1, END=5

q = [[0, S - 1]]
# visited[S - 1] = True
lst_cost[S-1] = 0

while q:
	pre_cost, pre_node = heappop(q)

	if visited[pre_node]: continue
		
	for cur_node, cur_cost in graph[pre_node]:
		# print(cur_node)
		
		visited[pre_node] = True
		mv_cost = cur_cost + pre_cost
		# print(pre_node, cur_node, mv_cost)
		if lst_cost[cur_node] > mv_cost:
			visited[pre_node] = True
			lst_cost[cur_node] = mv_cost
			heappush(q, [mv_cost, cur_node])
	# print(lst_cost)
print(lst_cost[E-1])