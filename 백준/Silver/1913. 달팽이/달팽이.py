N = int(input())
num = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
r, c = N//2, N//2
arr[r][c] = 1
# print(r, c)

size = 1
i = 1
ans = []

if num == 1:
    ans = [r+1, c+1]

while True:
    if arr[0][0] == N*N:
        break
    for d in range(4):
        if arr[0][0] == N*N:
            break
        for step in range(size):
            if d % 2 == 0:
                nr = r + dr[d]
                nc = c
            else:
                nr = r
                nc = c + dc[d]
            if (-1 < nr < N and -1 < nc < N):
                i += 1
                if i == num:
                    ans = [nr+1, nc+1]
                arr[nr][nc] = i
                r, c = nr, nc
                # print(r, c)
        if d == 1 or d == 3:
            size += 1
# print(arr)
for row in arr:
    print(*row)
print(*ans)