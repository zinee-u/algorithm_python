n = int(input())
# lst_sw = list(map(int, input().split()))
lst_sw = [-1] + list(map(int, input().split()))
# print(lst_num)
# print(lst_sw)

num_std = int(input())

for _ in range(num_std):
	g, g_num = map(int, input().split())
	if g == 1:
		for i in range(1, n//g_num+1):
			if lst_sw[i*g_num] == 0:
				lst_sw[i*g_num] = 1
			else:
				lst_sw[i*g_num] = 0
	if g == 2:
		if lst_sw[g_num] == 0:
			lst_sw[g_num] = 1
		else:
			lst_sw[g_num] = 0
		l, r = g_num-1, g_num+1
		while (l>0 and r<=n and lst_sw[l]==lst_sw[r]):
			if lst_sw[l]==0:
				lst_sw[l], lst_sw[r] = 1, 1
			else:
				lst_sw[l], lst_sw[r] = 0, 0
			l -= 1
			r += 1

# print(lst_sw)
for j in range(1,n+1):
	print(lst_sw[j], end=" ")
	if j%20==0:
		print()