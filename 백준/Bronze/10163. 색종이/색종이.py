n = int(input())
area = [[0 for _ in range(1001)] for _ in range(1001)]
pos = []

for i in range(n):
	pos.append(list(map(int, input().split())))
	ic, ir, w, h = pos[i]
	for j in range(ir, ir+h):
		area[j][ic:ic+w] = [i+1] * w

for i in range(1, n+1):
	answer = 0
	for r in range(1001):
		answer += area[r].count(i)
	print(answer)
