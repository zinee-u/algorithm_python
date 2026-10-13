# 16주차 · 탐색을 보고 고르는 주

문제 제목의 알고리즘을 가리고 상태와 비용에서 선택합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2027-01-25 · 기본 기술

### 노드까지 최소 이동 횟수

graph는 방향 있는 연결 목록입니다. start부터 각 노드까지 최소 간선 수를 반환하세요. 갈 수 없으면 -1입니다.

- 1 ≤ 노드 수 ≤ 1000
- 0 ≤ start < 노드 수
- 모든 간선 비용은 1

```python
def solution(graph, start):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[1,2],[3],[3],[]],0]` | `[0,1,1,2]` |
| `[[[],[0]],0]` | `[0,-1]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. dist[start]=0과 q=[start]가 함께 시작됩니다.
2. 다음 거리는 dist[node]+1입니다.

dist의 -1은 미방문입니다. 큐에 넣을 때 dist를 갱신해야 중복 삽입을 막습니다.

```python
from collections import deque
def solution(graph, start):
  dist = [-1] * len(graph)
  dist[start] = 0
  q = deque([start])
  while q:
    node = q.popleft()
    for nxt in graph[node]:
      if dist[nxt] != -1:
        continue
      dist[nxt] = dist[node] + 1
      q.append(nxt)
  return dist
```

</details>

## 2027-01-26 · 기본 기술

### 목적지까지 최소 요금

0번부터 n-1번까지 일방통행 도로 [a,b,w]를 이용해 start에서 goal까지 가는 최소 총요금을 반환하세요. 갈 수 없으면 -1입니다.

- 1 ≤ n ≤ 1000
- 간선 수 ≤ 5000
- 0 ≤ 요금 ≤ 10000

```python
def solution(n, roads, start, goal):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[3,[[0,1,9],[0,2,1],[2,1,2]],0,1]` | `3` |
| `[2,[],0,1]` | `-1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. if cost > dist[node]: continue입니다.
2. heappush도 개선 조건의 안에 둡니다.

dist[start]=0으로 시작합니다. 더 저렴한 후보일 때만 기록과 힙을 함께 갱신하고 오래된 힙 항목은 건너뜁니다.

```python
import heapq
def solution(n, roads, start, goal):
  graph = [[] for _ in range(n)]
  for a,b,w in roads:
    graph[a].append([b,w])
  dist = [float('inf')]*n
  dist[start] = 0
  heap = [[0,start]]
  while heap:
    cost,node = heapq.heappop(heap)
    if cost > dist[node]: continue
    for nxt,w in graph[node]:
      candidate = cost+w
      if candidate < dist[nxt]:
        dist[nxt] = candidate
        heapq.heappush(heap,[candidate,nxt])
  return -1 if dist[goal] == float('inf') else dist[goal]
```

</details>

## 2027-01-27 · 기본 기술

### 스탬프 하나를 가져와 퇴장

S에서 출발해 A를 밟은 뒤 E에 도착하는 최소 이동 횟수를 반환하세요. #은 벽이고 상하좌우로 이동합니다. A를 얻기 전에도 E를 지나갈 수 있습니다. 불가능하면 -1입니다.

- 1 ≤ 행·열 ≤ 20
- S,A,E는 각각 하나씩

```python
def solution(board):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[["SEA"]]` | `3` |
| `[["S.AE"]]` | `3` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 보유 상태는 다음 칸의 문자로 갱신합니다.
2. 새 상태로 방문 검사와 큐 삽입을 하세요.

같은 좌표라도 스탬프가 있으면 다른 상태입니다. visited[r][c][has_a]를 사용합니다.

```python
from collections import deque
def solution(board):
  N,M = len(board),len(board[0])
  for r in range(N):
    for c in range(M):
      if board[r][c] == 'S':
        sr,sc = r,c
  visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
  visited[sr][sc][0] = True
  q = deque([[sr,sc,0,0]])
  while q:
    r,c,has_a,cnt = q.popleft()
    if board[r][c] == 'E' and has_a:
      return cnt
    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      nr,nc = r+dr,c+dc
      if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] == '#':
        continue
      nxt_a = has_a
      if board[nr][nc] == 'A':
        nxt_a = 1
      if visited[nr][nc][nxt_a]:
        continue
      visited[nr][nc][nxt_a] = True
      q.append([nr,nc,nxt_a,cnt+1])
  return -1
```

</details>

## 2027-01-28 · 기본 기술

### 주말 · 공항 대신 티켓을 방문 처리

ICN에서 출발해 모든 방향 있는 티켓을 한 번씩 사용한 경로 중 사전순으로 가장 앞선 공항 목록을 반환하세요. 같은 티켓 내용이 여러 장 있어도 각각 사용합니다. 항상 가능한 경로가 있습니다.

- 1 ≤ 티켓 수 ≤ 7
- 각 티켓은 [출발,도착] 공항 이름

```python
def solution(tickets):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[["ICN","A"],["A","ICN"],["ICN","B"]]]` | `["ICN","A","ICN","B"]` |
| `[[["ICN","A"],["ICN","A"],["A","ICN"]]]` | `["ICN","A","ICN","A"]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 완성된 경로 길이는 티켓 수+1입니다.
2. 후보 티켓을 도착 이름 순서로 탐색하고 첫 완성 경로를 반환합니다.

같은 공항은 여러 번 갈 수 있습니다. used는 공항이 아니라 티켓 번호별로 만듭니다.

```python
def solution(tickets):
  used = [False]*len(tickets)
  order = sorted(range(len(tickets)), key=lambda i:tickets[i][1])
  path = ['ICN']
  def dfs(node):
    if len(path) == len(tickets)+1:
      return path[:]
    for i in order:
      a,b = tickets[i]
      if used[i] or a != node:
        continue
      used[i] = True
      path.append(b)
      result = dfs(b)
      path.pop()
      used[i] = False
      if result is not None:
        return result
  return dfs('ICN')
```

</details>

## 2027-01-29 · 가리고 다시 풀기

### 주말 · 여러 출발점의 귀환 거리

0번부터 n-1번까지 양방향 도로를 한 번 지날 때 1분 걸립니다. sources 각 위치에서 goal까지 거리를 순서대로 반환하세요. 갈 수 없으면 -1입니다.

- 1 ≤ n ≤ 10000
- 도로 수 ≤ 30000
- 1 ≤ sources 길이 ≤ n

```python
def solution(n, roads, sources, goal):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[5,[[0,1],[1,2],[2,3]],[0,2,4],3]` | `[3,1,-1]` |
| `[1,[],[0],0]` | `[0]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. sources마다 큐를 재사용하지 마세요.
2. goal을 시작점으로 잡고 마지막에 dist[source]를 읽습니다.

공통 목적지에서 BFS 한 번을 실행합니다. 양방향이므로 거꾸로 구한 거리가 같습니다.

```python
from collections import deque
def solution(n, roads, sources, goal):
  graph = [[] for _ in range(n)]
  for a, b in roads:
    graph[a].append(b)
    graph[b].append(a)
  dist = [-1] * n
  dist[goal] = 0
  q = deque([goal])
  while q:
    node = q.popleft()
    for nxt in graph[node]:
      if dist[nxt] == -1:
        dist[nxt] = dist[node] + 1
        q.append(nxt)
  return [dist[source] for source in sources]
```

</details>

## 2027-01-30 · 토요일 응용

### 두 스탬프를 모아 퇴장하기

체험관 지도 board에서 S는 출발점, E는 출구, A와 B는 서로 다른 스탬프 부스, .은 빈 칸, #은 벽입니다. 상하좌우의 벽이 아닌 칸으로 한 번에 한 칸 이동할 수 있고, 이동할 때마다 이동 횟수가 1 증가합니다. A 또는 B에 처음 들어가면 해당 스탬프를 얻고 이후에도 보유합니다. 두 스탬프를 모두 가진 상태로 E에 도착해야 체험이 끝납니다. 스탬프를 다 모으기 전에도 E를 통과할 수 있으며, 이미 방문한 칸과 부스를 다시 방문해도 됩니다. solution(board)을 완성하여 체험을 끝내는 데 필요한 최소 이동 횟수를 정수로 반환하세요. 불가능하면 -1을 반환합니다.

- 2 ≤ len(board) ≤ 20
- 2 ≤ len(board[0]) ≤ 20이며 모든 행의 길이가 같습니다.
- 각 칸은 S, E, A, B, ., # 중 하나입니다.
- S, E, A, B는 각각 정확히 한 칸씩 존재하며 서로 다른 칸입니다.
- 지도 밖으로 이동하거나 벽을 통과할 수 없고, 대각선 이동은 허용되지 않습니다.
- 스탬프를 얻는 데에는 추가 이동이나 비용이 필요하지 않습니다.

```python
def solution(board):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[["S.A","...","B.E"]]` | `8` |
| `[["ASEB","####"]]` | `5` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 같은 칸에 도착했더라도, 스탬프가 없는 경우와 두 개를 가진 경우는 앞으로 할 수 있는 일이 다릅니다. 위치만으로 방문 여부를 판단해도 될지 생각해 보세요.
2. 방문 상태는 (행, 열, 스탬프 보유 상태)입니다. 보유 상태는 없음, A만, B만, 둘 다의 네 가지이며, 같은 전체 상태를 처음 방문한 이동 횟수가 최단 거리입니다.
3. 스탬프 상태를 0~3으로 저장하고 A에서는 mask | 1, B에서는 mask | 2로 갱신하세요. distance[행][열][mask]와 deque를 사용하며, E이면서 mask == 3인 상태를 꺼냈을 때만 종료합니다.

위치가 같아도 모은 스탬프가 다르면 별개의 상태로 탐색합니다. A 보유를 1, B 보유를 2로 표시하면 보유 상태는 0, 1, 2, 3의 네 가지입니다. 이웃 칸이 부스라면 다음 상태에 해당 스탬프를 추가한 뒤, 아직 방문하지 않은 전체 상태만 큐에 넣습니다. 모든 이동 비용이 1이므로 BFS에서 처음 꺼낸 (출구, 두 스탬프) 상태의 거리가 정답입니다. 출구를 일찍 통과해도 탐색을 계속하며, 이전에 방문한 칸이라도 스탬프 상태가 달라졌다면 다시 탐색해야 합니다. 행 수를 H, 열 수를 W라 하면 상태가 최대 4HW개이므로 시간과 공간 복잡도는 모두 O(HW)입니다.

```python
from collections import deque

def solution(board):
  height = len(board)
  width = len(board[0])
  for row in range(height):
    for col in range(width):
      if board[row][col] == 'S':
        start_row, start_col = row, col

  distance = [[[-1] * 4 for _ in range(width)] for _ in range(height)]
  distance[start_row][start_col][0] = 0
  queue = deque([(start_row, start_col, 0)])

  while queue:
    row, col, mask = queue.popleft()
    steps = distance[row][col][mask]
    if board[row][col] == 'E' and mask == 3:
      return steps

    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      next_row, next_col = row + dr, col + dc
      if not (0 <= next_row < height and 0 <= next_col < width):
        continue
      cell = board[next_row][next_col]
      if cell == '#':
        continue
      next_mask = mask
      if cell == 'A':
        next_mask |= 1
      elif cell == 'B':
        next_mask |= 2
      if distance[next_row][next_col][next_mask] != -1:
        continue
      distance[next_row][next_col][next_mask] = steps + 1
      queue.append((next_row, next_col, next_mask))

  return -1
```

</details>

## 2027-01-31 · 일요일 전이

### 야간 셔틀의 한 번 할인권

일방통행 야간 셔틀을 이어 타며 start에서 goal로 이동합니다. 할인권은 전체 이동 중 최대 한 번 사용할 수 있고, 요금 w인 셔틀에 사용하면 그 이동 요금만 max(0, w - discount)가 됩니다. 남는 할인액은 다음 이동으로 넘길 수 없습니다. solution(n, roads, start, goal, discount)를 작성해 [최소 총요금, 할인권 사용 여부]를 반환하세요. 사용 여부는 미사용 0, 사용 1입니다. 총요금이 같다면 할인권을 사용하지 않는 결과를 우선합니다. 도달할 수 없으면 [-1, 0]을 반환합니다. start와 goal이 같으면 이동하지 않아도 되므로 [0, 0]입니다.

- 1 ≤ n ≤ 30,000, 0 ≤ len(roads) ≤ 100,000.
- 1 ≤ start, goal ≤ n. 각 roads 원소는 정수 [a, b, fare]이며 1 ≤ a, b ≤ n입니다.
- 0 ≤ fare, discount ≤ 1,000,000,000. 할인 후 요금도 음수가 될 수 없습니다.
- 운행 방향은 a → b입니다. 반대 방향은 자동으로 추가되지 않습니다.
- 평행 운행로, 중복 원소, 자기 자신으로 향하는 운행로, 0원 운행로가 있을 수 있습니다.
- 정류장과 운행로를 여러 번 이용할 수 있습니다. 할인권은 이동 횟수와 무관하게 최대 한 번만 사용합니다.
- 경로 자체는 반환하지 않습니다. 총요금과 사용 여부까지 같으면 어떤 경로를 선택해도 결과는 같습니다.

```python
def solution(n, roads, start, goal, discount):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[5,[[1,2,1],[2,5,10],[1,3,3],[3,4,3],[4,5,3]],1,5,8]` | `[3,1]` |
| `[4,[[1,2,0],[2,4,0],[1,3,6],[3,4,2]],1,4,5]` | `[0,0]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 같은 정류장에 같은 요금으로 도착해도 할인권이 남아 있는지에 따라 이후의 선택이 달라집니다. 정류장 외에 무엇을 상태에 포함해야 할까요?
2. distance[v][used]를 할인권 미사용/사용 상태의 최소 요금으로 유지하세요. 미사용 상태에서는 정가로 이동하거나 할인권을 쓰는 두 전이가 가능합니다.
3. 힙에 (요금, 정류장, used)를 넣고 각 상태의 오래된 항목을 건너뛰세요. 목적지의 (distance[goal][0], 0), (distance[goal][1], 1)을 튜플로 비교하면 요금과 미사용 우선 규칙을 함께 처리할 수 있습니다.

정류장마다 할인권이 남은 상태와 사용한 상태를 별개 정점처럼 취급합니다. 모든 상태에서 정가 이동이 가능하고, 미사용 상태에서만 할인 요금으로 사용 상태에 갈 수 있습니다. 할인 후의 요금도 0 이상이므로 확장한 그래프에 다익스트라를 적용합니다. 할인 없는 최단 경로를 먼저 고른 뒤 할인하는 방법은 정답이 아닐 수 있습니다. 힙의 요금과 distance[node][used]가 다르면 이미 개선된 오래된 항목이므로 확장하지 않습니다. 목적지 두 상태를 요금, 사용 여부 순서로 비교합니다. 시간 복잡도는 O((n + m) log(m + 1)), 공간 복잡도는 O(n + m)입니다.

```python
import heapq

def solution(n, roads, start, goal, discount):
  graph = [[] for _ in range(n + 1)]
  for a, b, fare in roads:
    graph[a].append((b, fare))
  distance = [[float('inf')] * 2 for _ in range(n + 1)]
  distance[start][0] = 0
  queue = [(0, start, 0)]
  while queue:
    fare, node, used = heapq.heappop(queue)
    if fare != distance[node][used]:
      continue
    for neighbor, weight in graph[node]:
      candidate = fare + weight
      if candidate < distance[neighbor][used]:
        distance[neighbor][used] = candidate
        heapq.heappush(queue, (candidate, neighbor, used))
      if used == 0:
        candidate = fare + max(0, weight - discount)
        if candidate < distance[neighbor][1]:
          distance[neighbor][1] = candidate
          heapq.heappush(queue, (candidate, neighbor, 1))
  fare, used = min((distance[goal][0], 0), (distance[goal][1], 1))
  return [-1, 0] if fare == float('inf') else [fare, used]
```

</details>

## 가리고 설명할 질문

BFS와 다익스트라 중 무엇을 고르는 기준은?

<details><summary>답 확인</summary>

한 번의 이동 비용이 모두 같으면 BFS, 서로 다른 비음수 비용이면 다익스트라를 우선 고려합니다.

</details>
