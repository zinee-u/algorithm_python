n1 = int(input())

lst = []

cnt_max = -1
num2 = 0
for n2 in range(n1,-1,-1):
	cnt = 2
	tmp1, tmp2, tmp3 = n1, n2, n1-n2
	while tmp3 > -1:
		cnt += 1
		tmp1, tmp2 = tmp2, tmp3
		tmp3 = tmp1 - tmp2
		cnt_max = max(cnt, cnt_max)
	if cnt_max == cnt:
		num2 = n2

num1, num3 = n1, n1-num2 
lst.append(num1)
lst.append(num2)
lst.append(num3)
while num3 > -1:
	num1, num2 = num2, num3
	num3 = num1 - num2
	if num3 > -1:
		lst.append(num3)

print(len(lst))
print(*lst)