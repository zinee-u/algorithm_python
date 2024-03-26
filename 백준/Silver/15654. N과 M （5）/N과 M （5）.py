n, m = map(int, input().split())
arr = []
lst_num = list(map(int, input().split()))
lst_num.sort()
# print(lst_num)
visited = [ False for _ in range(n) ]

def recur():
  #base
  if len(arr) == m:
    print(*arr)
    return
  
  for i in range(n):
    if visited[i]: continue

    visited[i] = True
    arr.append(lst_num[i])
    recur()
    arr.pop()
    visited[i] = False

recur()