import sys
import heapq

N, M, K, X = map(int, sys.stdin.readline().split())
# print(N,M,K,X)
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    # print(a, b)
    arr[a].append(b)

INF = float("inf")

def dik(s):
    dist = [INF] * (N+1)
    dist[s] = 0
    q = []
    heapq.heappush(q,[0, s])
    while q:
        d, v = heapq.heappop(q)
        if d > dist[v]:
            continue
        for nv in arr[v]:
            distance = d+1
            if dist[nv] > distance:
                dist[nv] = distance
                heapq.heappush(q,[distance, nv])
    return dist

ans = []
ret = dik(X)
# print(ret)

for i, val in enumerate(ret):
    if val == K:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    print(*ans)