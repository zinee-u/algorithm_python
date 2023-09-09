import sys
# BOJ의 채점 서버에서 이 값은 1,000
# 다른 방법으로 풀어보기
sys.setrecursionlimit(10**6)

dr, dc = [0, 1, 0, -1, 1, -1, 1, -1], [1, 0, -1, 0, 1, -1, -1, 1]

def dfs(r, c):
    visited[r][c] = 1
    for d in range(8):
        nr, nc = r + dr[d], c + dc[d]
        if -1 < nr < row and -1 < nc < col:
            if not visited[nr][nc] and arr[nr][nc]:
                dfs(nr, nc)

while True:
    col, row = map(int, input().split())
    if not (col and row):
        break
    cnt = 0
    visited = [[0 for _ in range(col)] for _ in range(row)]

    arr = [list(map(int, input().split(' '))) for _ in range(row)]

    for r in range(row):
        for c in range(col):
            if not visited[r][c] and arr[r][c]:
                dfs(r, c)
                cnt += 1

    print(cnt)