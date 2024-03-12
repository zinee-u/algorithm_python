import sys
n = int(input())

ps = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
st = []

for lst_ps in ps:
	st = []
	for e in lst_ps:
		if e == '(':
			st.append(e)
		else:
			if st:
				st.pop()
			else:
				st.append(e)
				break

	if st: print("NO")
	else: print("YES")

