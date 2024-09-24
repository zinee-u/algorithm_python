w, h = map(int, input().split())
n = int(input())
arr = [[0 for _ in range(w)] for _ in range(h)]

lst_w, lst_h = [0], [0]
max_diffw, max_diffh = -1, -1
for _ in range(n):
	cmd, num = map(int, input().split())
	if cmd==0:
		lst_h.append(num)
	else:
		lst_w.append(num)
lst_h.append(h)
lst_w.append(w)
lst_h.sort()
lst_w.sort()
# print(lst_h, lst_w)
for i in range(1,len(lst_h)):
	max_diffh = max(max_diffh,lst_h[i]-lst_h[i-1])

for i in range(1,len(lst_w)):
	max_diffw = max(max_diffw,lst_w[i]-lst_w[i-1])

print(max_diffh*max_diffw)