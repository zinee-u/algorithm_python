from collections import deque
m, n = map(int, input().split())
# print(n, m)
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

# arr = [list(map(int, input().split())) for _ in range(n)]
arr = []
# print(arr)
for _ in range(n):
    arr.append(list(map(int, input().split())))
    # print(list(map(int, input().split())))

# print(arr)

dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
q = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]
sum_day = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j, 0])
            visited[i][j] = 1
        elif arr[i][j] == -1:
            visited[i][j] == -1
            sum_day += 1

max_day = 0

while q:
    r, c, day = q.popleft()
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if -1 < nr < n and -1 < nc < m:
            if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = day + 1
                q.append([nr, nc, day + 1])
    max_day = max(max_day, day)
# print(visited)

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            sum_day -= 1
if sum_day != 0:
    answer = -1
else:
    # answer = max(map(max, visited))
    answer = max_day
print(answer)