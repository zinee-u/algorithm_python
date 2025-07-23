from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100000
INF = 10**18

dist = [INF] * (MAX + 1)
dist[N] = 0

dq = deque([N])
while dq:
    x = dq.popleft()
    if x == K:
        break
    # 이동 리스트: (다음 위치, 비용)
    for nx, w in ((x*2, 0), (x-1, 1), (x+1, 1)):
        if 0 <= nx <= MAX and dist[nx] > dist[x] + w:
            dist[nx] = dist[x] + w
            if w == 0:
                dq.appendleft(nx)
            else:
                dq.append(nx)

print(dist[K])
