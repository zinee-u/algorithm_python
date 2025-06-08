N = int(input())
ir,ic,fr,fc = list(map(int, input().split()))
dist = []

for _ in range(N):
  M = int(input())
  path = [[ir, ic]]
  for _ in range(M):
    path.append(list(map(int, input().split())))
  path.append([fr,fc])
  tmp_d = 0
  
  for i in range(1, len(path)):
    # print(i, j)
    tmp_d += abs(path[i][0]-path[i-1][0]) + abs(path[i][1] - path[i-1][1])
  # print(tmp_d)
  dist.append(tmp_d)

min_i, min_d = 0, float("INF")
for i, d in enumerate(dist):
  # print(i, d)
  if min_d > d :
    min_d = d
    min_i = (i+1)

print(min_i)