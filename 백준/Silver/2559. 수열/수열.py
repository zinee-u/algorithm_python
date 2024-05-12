n, k = map(int, input().split())
arr = list(map(int, input().split()))
# print(arr)

tmp_sum = sum(arr[0:k])
answer = sum(arr[0:k])

for i in range(n-k):
	tmp_sum -= arr[i]
	tmp_sum += arr[i+k]
	answer = max(answer, tmp_sum)

print(answer)