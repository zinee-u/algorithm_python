# 5주차 · 격자에서 한 번의 이동

한 칸 이동과 멈출 때까지 이동, 연결 구역 전체를 구분합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-11-09 · 기본 기술

### 격자에서 한 칸씩 이동

0은 통로, 1은 벽입니다. 왼쪽 위에서 오른쪽 아래까지 상하좌우로 이동하는 최소 횟수를 반환하세요. 시작·끝이 벽이거나 갈 수 없으면 -1입니다.

- 1 ≤ 행·열 수 ≤ 30
- 이동 한 번은 이웃 칸 하나로 가는 것

```python
def solution(board):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,0,0],[1,1,0]]]` | `3` |
| `[[[0]]]` | `0` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. dist는 행별로 독립인 2차원 배열이어야 합니다.
2. 출발점 거리는 0입니다.

노드는 좌표입니다. 목표를 꺼냈을 때 거리를 반환합니다.

```python
from collections import deque
def solution(board):
  N, M = len(board), len(board[0])
  if board[0][0] or board[N-1][M-1]:
    return -1
  dist = [[-1]*M for _ in range(N)]
  dist[0][0] = 0
  q = deque([[0,0]])
  dr, dc = [-1,0,1,0], [0,-1,0,1]
  while q:
    r,c = q.popleft()
    if r == N-1 and c == M-1:
      return dist[r][c]
    for d in range(4):
      nr,nc = r+dr[d],c+dc[d]
      if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0 and dist[nr][nc] == -1:
        dist[nr][nc] = dist[r][c]+1
        q.append([nr,nc])
  return -1
```

</details>

## 2026-11-10 · 기본 기술

### 연결 구역의 합

양수 칸끼리 상하좌우로 연결된 각 구역의 합을 구하고 가장 큰 합을 반환하세요. 0은 빈 칸이며 양수가 없으면 0입니다.

- 행·열 수 1~30
- 값은 0~9

```python
def solution(board):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[1,2,0],[0,0,5],[3,3,0]]]` | `6` |
| `[[[0,0]]]` | `0` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 바깥 이중 반복문에서 미방문 양수 칸을 찾습니다.
2. 각 BFS의 total은 0부터 다시 시작합니다.

BFS 한 번은 한 구역 전체입니다. 시작점도 큐에 넣을 때 방문 처리합니다.

```python
from collections import deque
def solution(board):
  N,M = len(board),len(board[0])
  visited = [[False]*M for _ in range(N)]
  answer = 0
  for sr in range(N):
    for sc in range(M):
      if not board[sr][sc] or visited[sr][sc]:
        continue
      q = deque([[sr,sc]])
      visited[sr][sc] = True
      total = 0
      while q:
        r,c = q.popleft()
        total += board[r][c]
        for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
          nr,nc = r+dr,c+dc
          if 0 <= nr < N and 0 <= nc < M and board[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append([nr,nc])
      answer = max(answer,total)
  return answer
```

</details>

## 2026-11-11 · 기본 기술

### 미끄러져 멈추는 좌표

board는 .과 D로 구성됩니다. start=[행,열]에서 direction 방향으로 벽 또는 격자 끝 바로 앞까지 미끄러져 멈춘 좌표를 반환하세요. 방향 0,1,2,3은 각각 위,왼쪽,아래,오른쪽입니다.

- 행·열 1~30
- 시작 칸은 .
- 0 ≤ direction ≤ 3

```python
def solution(board, start, direction):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[["...D.","....."],[0,0],3]` | `[0,2]` |
| `[["."],[0,0],0]` | `[0,0]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. cr,cc를 현재 위치로 쓰세요.
2. 다음 칸이 유효할 때만 cr,cc를 갱신합니다.

한 칸 미리 확인해서 막혔으면 멈춥니다. 이동 중간 칸과 도착 칸을 구분합니다.

```python
def solution(board, start, direction):
  N,M = len(board),len(board[0])
  dr,dc = [-1,0,1,0],[0,-1,0,1]
  r,c = start
  while True:
    nr,nc = r+dr[direction],c+dc[direction]
    if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] == 'D':
      return [r,c]
    r,c = nr,nc
```

</details>

## 2026-11-12 · 기본 기술

### 주말 · 멈춘 칸에서 다시 선택

R에서 시작해 방향을 고르면 D나 끝 직전까지 미끄러집니다. 멈출 때만 방향을 다시 고를 수 있습니다. G에 멈추기 위한 최소 방향 선택 횟수를 반환하세요. 불가능하면 -1입니다.

- 행·열은 2~20
- R,G는 각각 하나
- 다른 문자는 . 또는 D

```python
def solution(board):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[["R.G","..."]]` | `1` |
| `[["R.G.","...."]]` | `-1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 각 방향에서 while로 최종 cr,cc를 구합니다.
2. G를 지나가기만 한 것은 도착이 아닙니다.

BFS 간선 하나는 한 칸 이동이 아니라 한 번 미끄러지기입니다. 방문 처리와 큐 삽입은 미끄러지는 반복문 밖에 둡니다.

```python
from collections import deque
def solution(board):
  N,M = len(board),len(board[0])
  for r in range(N):
    for c in range(M):
      if board[r][c] == 'R':
        sr,sc = r,c
  visited = [[False]*M for _ in range(N)]
  visited[sr][sc] = True
  q = deque([[sr,sc,0]])
  for_pop = [[-1,0],[1,0],[0,-1],[0,1]]
  while q:
    r,c,cnt = q.popleft()
    if board[r][c] == 'G':
      return cnt
    for dr,dc in for_pop:
      cr,cc = r,c
      while True:
        nr,nc = cr+dr,cc+dc
        if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] == 'D':
          break
        cr,cc = nr,nc
      if not visited[cr][cc]:
        visited[cr][cc] = True
        q.append([cr,cc,cnt+1])
  return -1
```

</details>

## 2026-11-13 · 가리고 다시 풀기

### 미끄러져 멈추는 좌표

board는 .과 D로 구성됩니다. start=[행,열]에서 direction 방향으로 벽 또는 격자 끝 바로 앞까지 미끄러져 멈춘 좌표를 반환하세요. 방향 0,1,2,3은 각각 위,왼쪽,아래,오른쪽입니다.

- 행·열 1~30
- 시작 칸은 .
- 0 ≤ direction ≤ 3

```python
def solution(board, start, direction):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[["...D.","....."],[0,0],3]` | `[0,2]` |
| `[["."],[0,0],0]` | `[0,0]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. cr,cc를 현재 위치로 쓰세요.
2. 다음 칸이 유효할 때만 cr,cc를 갱신합니다.

한 칸 미리 확인해서 막혔으면 멈춥니다. 이동 중간 칸과 도착 칸을 구분합니다.

```python
def solution(board, start, direction):
  N,M = len(board),len(board[0])
  dr,dc = [-1,0,1,0],[0,-1,0,1]
  r,c = start
  while True:
    nr,nc = r+dr[direction],c+dc[direction]
    if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] == 'D':
      return [r,c]
    r,c = nr,nc
```

</details>

## 2026-11-14 · 토요일 응용

### 온실 안쪽 수확 구역 고르기

온실 지도에서 양의 수확량을 가진 칸들이 상하좌우로 이어져 있으면 하나의 수확 구역입니다. 대각선으로는 연결되지 않으며 0인 칸이나 지도 밖으로 이동할 수 없습니다. 구역에 속한 칸 중 하나라도 지도의 맨 위·맨 아래 행 또는 맨 왼쪽·맨 오른쪽 열에 있으면 그 구역 전체는 수확 대상에서 제외합니다. 남은 구역 중 하나를 골라 그 구역의 모든 칸을 수확하려 합니다. solution(yields)는 얻을 수 있는 최대 수확량 합계를 정수로 반환하세요. 선택 가능한 구역이 없으면 0을 반환합니다. 하나의 연결된 구역을 일부로 나누어 선택할 수 없습니다.

- 1 ≤ 행 수, 열 수 ≤ 100이며 모든 행의 길이는 같습니다.
- 각 원소는 0 이상 1,000 이하의 정수입니다. 0은 빈 칸이며 구역에 포함되지 않습니다.
- 구역은 양수인 칸들이 상하좌우로 연결된 최대 묶음입니다.
- 경계에 닿는지 여부는 구역의 모든 칸을 기준으로 판단합니다. 경계까지 0인 통로가 있는지는 고려하지 않습니다.
- 선택한 한 구역의 합만 반환합니다. 선택 가능한 여러 구역의 합을 더하지 않습니다.

```python
def solution(yields):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,0,0,0,0,0],[0,4,2,0,8,0],[0,0,3,0,0,0],[0,7,0,5,5,0],[0,0,0,0,0,0]]]` | `10` |
| `[[[0,6,0,0,0],[0,1,0,4,0],[0,0,0,2,0],[0,5,0,0,0],[0,0,0,0,0]]]` | `6` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 경계에 닿지 않은 개별 칸만 고르면 안 됩니다. 먼저 연결된 구역 전체를 하나의 판단 단위로 묶어 보세요.
2. 구역 하나를 탐색하는 동안 수확량의 합과 경계에 닿았는지 여부를 함께 누적하세요. 경계 접촉을 발견해도 나머지 구역의 방문 처리는 끝내야 합니다.
3. 미방문 양수 칸마다 스택 탐색을 시작합니다. 꺼낸 칸의 값을 total에 더하고 경계 칸이면 touches_edge를 True로 만듭니다. 탐색 종료 후 touches_edge가 False인 경우에만 최대 합계를 갱신하세요.

기본 연결 요소 탐색에 구역별 합계와 경계 접촉 여부를 추가합니다. 한 구역의 모든 칸을 방문한 뒤에야 선택 가능 여부를 확정할 수 있습니다. 경계에 닿는 구역은 합계가 아무리 커도 제외하고, 경계에 닿지 않는 구역의 합계만 최댓값 후보로 사용합니다. 제외될 구역도 끝까지 방문 표시해야 나중에 그 구역의 일부를 별도 구역으로 오인하지 않습니다. 시간과 공간 복잡도는 모두 O(행 수 × 열 수)입니다.

```python
def solution(yields):
  rows, cols = len(yields), len(yields[0])
  seen = [[False] * cols for _ in range(rows)]
  best = 0
  for r in range(rows):
    for c in range(cols):
      if yields[r][c] == 0 or seen[r][c]:
        continue
      seen[r][c] = True
      stack = [(r, c)]
      total = 0
      touches_edge = False
      while stack:
        cr, cc = stack.pop()
        total += yields[cr][cc]
        if cr == 0 or cr == rows - 1 or cc == 0 or cc == cols - 1:
          touches_edge = True
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
          nr, nc = cr + dr, cc + dc
          if 0 <= nr < rows and 0 <= nc < cols:
            if yields[nr][nc] > 0 and not seen[nr][nc]:
              seen[nr][nc] = True
              stack.append((nr, nc))
      if not touches_edge:
        best = max(best, total)
  return best
```

</details>

## 2026-11-15 · 일요일 전이

### 주말 · 멈춘 칸에서 다시 선택

R에서 시작해 방향을 고르면 D나 끝 직전까지 미끄러집니다. 멈출 때만 방향을 다시 고를 수 있습니다. G에 멈추기 위한 최소 방향 선택 횟수를 반환하세요. 불가능하면 -1입니다.

- 행·열은 2~20
- R,G는 각각 하나
- 다른 문자는 . 또는 D

```python
def solution(board):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[["R.G","..."]]` | `1` |
| `[["R.G.","...."]]` | `-1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 각 방향에서 while로 최종 cr,cc를 구합니다.
2. G를 지나가기만 한 것은 도착이 아닙니다.

BFS 간선 하나는 한 칸 이동이 아니라 한 번 미끄러지기입니다. 방문 처리와 큐 삽입은 미끄러지는 반복문 밖에 둡니다.

```python
from collections import deque
def solution(board):
  N,M = len(board),len(board[0])
  for r in range(N):
    for c in range(M):
      if board[r][c] == 'R':
        sr,sc = r,c
  visited = [[False]*M for _ in range(N)]
  visited[sr][sc] = True
  q = deque([[sr,sc,0]])
  for_pop = [[-1,0],[1,0],[0,-1],[0,1]]
  while q:
    r,c,cnt = q.popleft()
    if board[r][c] == 'G':
      return cnt
    for dr,dc in for_pop:
      cr,cc = r,c
      while True:
        nr,nc = cr+dr,cc+dc
        if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] == 'D':
          break
        cr,cc = nr,nc
      if not visited[cr][cc]:
        visited[cr][cc] = True
        q.append([cr,cc,cnt+1])
  return -1
```

</details>

## 가리고 설명할 질문

미끄러지는 BFS에서 큐에 넣을 위치는 어디인가요?

<details><summary>답 확인</summary>

각 방향에서 벽/끝 직전까지 간 최종 정지 위치입니다. 중간 칸은 정점으로 넣지 않습니다.

</details>
