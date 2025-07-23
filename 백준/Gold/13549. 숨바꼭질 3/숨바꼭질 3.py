from collections import deque
N, K = map(int, input().split())
INF = float("inf")
visited = [INF] * 100001
q = deque()
q.append([N, 0])
visited[N] = 0

while q:
    pos_cur, t = q.popleft()
    if pos_cur == K:
        print(t)
        break
    
    pos_nxt = pos_cur * 2
    if -1 < pos_nxt < 100001 and visited[pos_nxt] > visited[pos_cur]:
        q.appendleft([pos_nxt, t])
        visited[pos_nxt]=visited[pos_cur]

    pos_nxt = pos_cur + 1
    if -1 < pos_nxt < 100001 and visited[pos_nxt] > visited[pos_cur]+1:
        q.append([pos_nxt, t+1])
        visited[pos_nxt]=visited[pos_cur]+1
    
    pos_nxt = pos_cur - 1
    if -1 < pos_nxt < 100001 and visited[pos_nxt] > visited[pos_cur]+1:
        q.append([pos_nxt, t+1])
        visited[pos_nxt]=visited[pos_cur]+1