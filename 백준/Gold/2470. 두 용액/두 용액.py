n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)

s, e = 0, n-1
min_ans = float("INF")

while (s!=e):
	tmp_sum = arr[s] + arr[e]
	
	if abs(min_ans) > abs(tmp_sum):
		min_ans = tmp_sum
		lst = [arr[s], arr[e]]

	if tmp_sum == 0:
		lst = [arr[s], arr[e]]
		break
	elif tmp_sum > 0:
		e -= 1
	else:
		s += 1

print(*lst)