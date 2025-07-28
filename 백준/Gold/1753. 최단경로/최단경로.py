import sys
import heapq
input = sys.stdin.read
data = input().split()
V, E = int(data[0]), int(data[1])
K = int(data[2])
info = data[3:]

graph = [[] for _ in range(V+1)]
INF = float("inf")
dist = [INF] * (V+1)
dist[K] = 0

for i in range(E):
    a, b, d = map(int, info[i*3:i*3+3])
    graph[a].append((b, d))

pq = []
heapq.heappush(pq, (0, K))

while pq:
    cur_dist, n1 = heapq.heappop(pq)
    if cur_dist > dist[n1]:
        continue

    for n2, d in graph[n1]:
        if dist[n2] > cur_dist + d:
            dist[n2] = cur_dist + d
            heapq.heappush(pq, (dist[n2], n2))

for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])