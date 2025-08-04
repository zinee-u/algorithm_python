import heapq

INF = float("inf")

N, M, X = map(int, input().split(' '))

arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, d = map(int, input().split(' '))
    arr[a].append([b, d])

def dik(s):
    dist = [INF] * (N+1)
    dist[s] = 0
    q = []
    heapq.heappush(q, [0, s])
    while q:
        d, v = heapq.heappop(q)
        if dist[v] < d:
            continue
        for nv, nd in arr[v]:
            distance = nd + d
            if dist[nv] > distance:
                dist[nv] = distance
                heapq.heappush(q,[distance, nv])
    return dist

ans = [[]]
for i in range(1, N+1):
    ans.append(dik(i))

res = 0
for i in range(1, N+1):
    res = max(res,ans[i][X]+ans[X][i])
print(res)