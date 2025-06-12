import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
root = [0 for _ in range(N+1)]

for _ in range(N-1):
  n1, n2 = map(int, sys.stdin.readline().split())
  # print(n1, n2)
  graph[n1].append(n2)
  graph[n2].append(n1)


def dfs(cur, parents):
  root[cur] = parents
  for nxt in graph[cur]:
    if nxt != parents:
      dfs(nxt, cur)

dfs(1, 0)

for i in range(2, N+1):
  print(root[i])