import sys

N, M, R = map(int, sys.stdin.readline().split(' '))
# print(N, M, R)
arr = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

K = min(N, M)//2

for s in range(K):
  sr, sc = s, s
  er, ec = (N-sr-1), (M-sc-1)
  lst = []
  for c in range(sc, ec):
    lst.append(arr[sr][c])
  for r in range(sr, er):
    lst.append(arr[r][ec])
  for c in range(ec, sc, -1):
    lst.append(arr[er][c])
  for r in range(er, sr, -1):
    lst.append(arr[r][sc])
  # print(lst)
  L = len(lst)
  # print(L)
  V = R % L
  if V:
    lst = lst[V:] + lst[:V]
  # print(lst)
  idx = 0
  for c in range(sc, ec):
    arr[sr][c]=lst[idx]
    idx+=1
  for r in range(sr, er):
    arr[r][ec]=lst[idx]
    idx+=1
  for c in range(ec, sc, -1):
    arr[er][c]=lst[idx]
    idx+=1
  for r in range(er, sr, -1):
    arr[r][sr]=lst[idx]
    idx+=1

for row in arr:
  print(*row)