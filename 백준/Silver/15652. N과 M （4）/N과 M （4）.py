n, m = map(int, input().split())
arr = []


def recur(dep):
  # base case
  if len(arr) == m:
    print(*arr)
    return

  # logic
  for i in range(dep, n+1):
    arr.append(i)
    recur(i)
    arr.pop()

recur(1)