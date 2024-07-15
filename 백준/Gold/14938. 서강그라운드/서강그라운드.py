import heapq
import sys


input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = list(map(int, input().split()))
# print(arr)
graph = [[] for _ in range(n+1)]


for _ in range(r):
	a, b, l = map(int, input().split())
	# print(a,b,l)
	graph[a].append([l, b])
	graph[b].append([l, a])
# print(graph)


def dijkstra(start):
	q = []
	INF = float("inf")
	dist = [INF for _ in range(n+1)]
	dist[start] = 0

	heapq.heappush(q, [0, start])

	while q:
		# print(q)
		cur_cost, cur_node = heapq.heappop(q)
		for nxt_cost, nxt_node in graph[cur_node]:
			if(dist[nxt_node] > dist[cur_node] + nxt_cost):
				nxt_cost += cur_cost
				dist[nxt_node] = nxt_cost
				heapq.heappush(q, [nxt_cost, nxt_node])
	return dist

ans = -1

for start in range(1, n+1):
	cnt_items = 0
	dist = dijkstra(start)
	for j in range(1, n+1):
		if dist[j] <= m:
			cnt_items += arr[j-1]
	ans = max(ans, cnt_items)

print(ans)