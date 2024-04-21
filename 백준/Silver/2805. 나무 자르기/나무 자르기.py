n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
# arr2 = list(map(lambda x: x-1, arr))
# print(arr2)
answer = 0
s, e = 0, arr[-1]
while (s <= e):
	cut = 0
	mid = (s+e)//2
	# print(mid)
	for i in range(n):
		if arr[i] > mid:
			cut += (arr[i] - mid)
		if cut > m:
			break
	# print("cut=",cut)

	if cut >= m:
		s = mid + 1
		answer = mid
	else:
		e = mid - 1

print(answer)