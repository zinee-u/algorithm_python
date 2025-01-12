n, k = map(int, input().split())
# print(n, k)

info = [list(map(int, input().split())) for _ in range(n)]
# print(info)

rooms = [[0 for _ in range(7)] for _ in range(2)] # gender, grade

for gen, grd in info:
	rooms[gen][grd] += 1

cnt_room = 0

for gen in range(2):
	for grd in range(1, 7):
		if rooms[gen][grd] > 0:
			cnt_room += (rooms[gen][grd] + k - 1) // k # (X+Y-1)//Y -> Ceiling

print(cnt_room)