n, s = map(int, input().split())

arr = list(map(int, input().split()))

i, j = 0, 0
tmp_sum = arr[0]
# print(tmp_sum)
answer = float("INF")

while ((i < n) and (j < n)):
	if tmp_sum >= s:
		answer = min(answer, j-i+1)
		tmp_sum -= arr[i]
		i += 1
	else:
		j += 1
		if j < n:
			tmp_sum += arr[j]
		else:
			tmp_sum -= arr[i]
			i += 1

if answer == float("INF"):
	answer = 0

print(answer)