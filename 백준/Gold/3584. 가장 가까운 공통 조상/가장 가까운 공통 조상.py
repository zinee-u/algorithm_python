import sys
sys.setrecursionlimit(10**6)

from collections import deque
T = int(input())


def find_pr(ch, lst):
  global graph
  if len(graph[ch]) == 0:
    # print(lst)
    return
  else:
    for pr in graph[ch]:
      lst.append(pr)
      find_pr(pr, lst)

for _ in range(T):
  N = int(input())
  # print(N)
  graph = [[] for _ in range(N+1)]
  lst_pr1, lst_pr2 = deque(), deque()
  for i in range(N-1):
    A, B = map(int, input().split())
    graph[B].append(A)
  n1, n2 = map(int, input().split())
  # print(n1, n2)
  # print(graph[n2])
  lst_pr1.append(n1)
  lst_pr2.append(n2)
  find_pr(n1, lst_pr1)
  find_pr(n2, lst_pr2)
  # print(lst_pr1, lst_pr2)
  if len(lst_pr1) - len(lst_pr2) > 0:
    for _ in range(len(lst_pr1) - len(lst_pr2)):
      lst_pr2.appendleft(0)
    # print(lst_pr2)
  elif len(lst_pr2) - len(lst_pr1) > 0:
    for _ in range(len(lst_pr2) - len(lst_pr1)):
      lst_pr1.appendleft(0)
    # print(lst_pr1)
  for i in range(len(lst_pr1)):
    if lst_pr1[i] == lst_pr2[i]:
      ans = lst_pr1[i]
      print(ans)
      break