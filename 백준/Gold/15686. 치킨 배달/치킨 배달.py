N, M = map(int, input().split())
# print(N,M)

arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)


dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]

def get_sum_dst(pos_hm, lst_ch):
  sum_dst = 0
  for r1, c1 in pos_hm:
    cal_dst = 0
    min_dst = float("INF")
    for r2, c2 in lst_ch:
      cal_dst = abs(r2-r1)+abs(c2-c1)
      min_dst = min(cal_dst, min_dst)
    sum_dst += min_dst
  return sum_dst

ans_dst = float("INF")

# combination nCm, nCm-1, ... ,nC1
def recur(i, cnt, num_ch):
  global lst_ch, pos_hm, ans_dst
  
  if cnt == num_ch:
    ans_dst = min(ans_dst,get_sum_dst(pos_hm,lst_ch))
    return
  
  if i == len(pos_ch):
    return
  
  lst_ch.append(pos_ch[i])
  recur(i+1, cnt+1, num_ch)
  lst_ch.pop()
  recur(i+1, cnt, num_ch)

# main
pos_ch, pos_hm = [], [] # available
lst_ch = []
# cal. dist
dst_min = float("INF")

for i in range(N):
  for j in range(N):
    if arr[i][j] == 1:
      pos_hm.append([i, j])
    if arr[i][j] == 2:
      pos_ch.append([i, j])

# all events
for num_ch in range(1, M+1):
  # print("DBG num_ch = ", num_ch)
  recur(0,0,num_ch)

# answer
print(ans_dst)