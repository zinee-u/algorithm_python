n = int(input())

lst_num = [i for i in range(1, n+1)]

st = []

while len(lst_num) != 1:
	st.append(lst_num.pop(0))
	lst_num.append(lst_num.pop(0))


for i in range(len(st)):
	print(st[i], end=' ')

print(lst_num[0])