from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr = [[-1] * 101 for _ in range(101)]
    visited = [[0] * 101 for _ in range(101)]
    dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
    
    def bfs(q):
        # nonlocal ans
        while q:
            r, c, dist = q.popleft()
            if r == itemY*2 and c == itemX*2:
                answer = dist//2
                return answer
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if -1 < nr < 101 and -1 < nc < 101:
                    if not visited[nr][nc] and arr[nr][nc] == 0:
                        visited[nr][nc] = 1
                        q.append([nr, nc, dist+1])
    
    #main
    for lc, lr, rc, rr in rectangle:
        for i in range(lr*2, rr*2+1):
            for j in range(lc*2, rc*2+1):
                if lr*2 < i < rr*2 and lc*2 < j < rc*2:
                    arr[i][j] = 1
                elif arr[i][j] != 1:
                    arr[i][j] = 0
        # print(arr)
    q = deque()
    q.append([characterY*2, characterX*2, 0])
    visited[characterY*2][characterX*2] = 1
    answer = bfs(q)
    
    
    return answer