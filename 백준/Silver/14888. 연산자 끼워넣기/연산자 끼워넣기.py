N = int(input())
# print(N)
nums = list(map(int, input().split(' ')))
# + - * //
nums_op = list(map(int, input().split(' ')))

# print(nums)
# print(nums_op)

# +(2), -(1), *(1), //(1)
# A[0]
# A[0] + A[1]
min_val, max_val = float("INF"), float("-INF")
ans = []

def recur(res, i):
  global min_val, max_val
  if i == N:
    min_val = min(min_val, res)
    max_val = max(max_val, res)
    return
  # print("DBG res, i", res ,i)
  # +
  if nums_op[0] > 0:
    nums_op[0] -= 1
    recur(res+nums[i],i+1)
    nums_op[0] += 1
  # -
  if nums_op[1] > 0:
    nums_op[1] -= 1
    recur(res-nums[i],i+1)
    nums_op[1] += 1
  # *
  if nums_op[2] > 0:
    nums_op[2] -= 1
    recur(res*nums[i],i+1)
    nums_op[2] += 1
  # //
  if nums_op[3] > 0:
    nums_op[3] -= 1
    if res < 0:
      res *= -1
      tmp = res // nums[i]
      tmp *= -1
    else:
      tmp = res // nums[i]
    recur(tmp,i+1)
    nums_op[3] += 1

recur(nums[0], 1)

print(max_val)
print(min_val)