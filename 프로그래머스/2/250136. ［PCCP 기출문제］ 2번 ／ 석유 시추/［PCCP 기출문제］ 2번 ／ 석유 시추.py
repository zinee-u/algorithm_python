from collections import deque
def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    
    dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]
    visited = [[0] * m for _ in range(n)]
    visited_idx = [[0] * m for _ in range(n)]
    arr_cnt = [[0] * m for _ in range(n)]
    
    def bfs(q):
        pos_oil = []
        pos_oil.append([q[0][0], q[0][1]])
        cnt = 1
        while q:
            r, c, idx = q.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if -1 < nr < n and -1 < nc < m:
                    if not visited[nr][nc] and land[nr][nc] == 1:
                        visited[nr][nc] = 1
                        visited_idx[nr][nc] = idx
                        cnt += 1
                        q.append([nr, nc, idx])
                        pos_oil.append([nr, nc])
        
        for y, x in pos_oil:
            arr_cnt[y][x] = cnt
    
    #main
    idx = 1
    for j in range(m):
        q = deque()
        for i in range(n):
            if land[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                visited_idx[i][j] = idx
                q.append([i, j, idx])
                bfs(q)
                idx += 1
    # print(visited_idx)
    
    # print(idx)
    # tmp_cnt = 0
    for j in range(m):
        visited_area = [0] * (idx)
        tmp_cnt = 0
        for i in range(n):
            area = visited_idx[i][j]
            if area > 0 and not visited_area[area]:
                tmp_cnt = tmp_cnt + arr_cnt[i][j]
                visited_area[area] = 1

        answer = max(tmp_cnt, answer)
    
    return answer