import sys
T = int(input())

def search_bin(num, s, e):
	while s <= e:
		mid = (s + e) // 2
		if num == n[mid]:
			return 1
		if num > n[mid]:
			s = mid + 1
		elif num < n[mid]:
			e = mid - 1
	return 0


for _ in range(T):
	len_n = int(input())
	n = list(map(int, sys.stdin.readline().split()))
	n.sort()
	len_m = int(input())
	m = list(map(int, sys.stdin.readline().split()))
	for num in m:
		print(search_bin(num, 0, len_n-1))