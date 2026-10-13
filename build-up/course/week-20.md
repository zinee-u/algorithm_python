# 20주차 · 약점 재현과 전이 주

한 번 맞힌 것보다 시간이 지난 뒤 다시 구현하는지 확인합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2027-02-22 · 기본 기술

### 카드 번호의 순열

0~n-1 카드 중 서로 다른 length개를 순서 있게 뽑은 모든 번호 목록을 사전순으로 반환하세요.

- 1 ≤ n ≤ 6
- 0 ≤ length ≤ n

```python
def solution(n, length):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[3,2]` | `[[0,1],[0,2],[1,0],[1,2],[2,0],[2,1]]` |
| `[2,0]` | `[[]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 완성 조건은 len(path)==length입니다.
2. 결과에는 path[:]를 넣으세요.

used는 이번 경로에서 쓴 카드입니다. 재귀에서 돌아온 뒤 False로 복구하고 path를 pop합니다.

```python
def solution(n, length):
  used = [False]*n
  path,res = [],[]
  def dfs():
    if len(path) == length:
      res.append(path[:])
      return
    for i in range(n):
      if used[i]:
        continue
      used[i] = True
      path.append(i)
      dfs()
      path.pop()
      used[i] = False
  dfs()
  return res
```

</details>

## 2027-02-23 · 기본 기술

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

## 2027-02-24 · 기본 기술

### 주말 · 도착 목록과 대기 힙 합치기

한 번에 작업 하나를 중단 없이 처리합니다. 작업이 끝날 때 도착한 작업 중 소요시간,요청시각,입력 번호 순으로 고릅니다. 대기 작업이 없으면 다음 요청까지 쉽니다. 요청부터 종료까지 시간의 평균을 내림해 반환하세요.

- 1 ≤ 작업 수 ≤ 1000
- 요청 시각 0~100000, 소요시간 1~1000

```python
def solution(jobs):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,3],[1,9],[2,6]]]` | `9` |
| `[[[5,2],[20,1]]]` | `1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 힙이 비면 now를 다음 요청까지 올립니다.
2. 현재 now까지 도착한 작업을 모두 힙에 넣은 뒤 하나 꺼냅니다.

pending은 도착 순서, heap은 처리 우선순위입니다. 누적 시간에는 방금 힙에서 꺼낸 요청 시각을 사용합니다.

```python
import heapq
def solution(jobs):
  pending = sorted([[s,load,i] for i,(s,load) in enumerate(jobs)])
  heap = []
  now,total,idx = 0,0,0
  while idx < len(jobs) or heap:
    if not heap:
      now = max(now,pending[idx][0])
    while idx < len(jobs) and pending[idx][0] <= now:
      request,load,job_id = pending[idx]
      heapq.heappush(heap,[load,request,job_id])
      idx += 1
    load,request,job_id = heapq.heappop(heap)
    now += load
    total += now-request
  return total//len(jobs)
```

</details>

## 2027-02-25 · 기본 기술

### 할인권 상태의 다음 후보

현재 누적요금 cost와 할인권 사용 여부 used(0/1)가 주어집니다. 요금 fare인 구간을 탈 때 가능한 [새 총요금,새 사용여부] 목록을 반환하세요. 할인 미사용 후보를 먼저, 지금 사용하는 후보를 다음에 둡니다.

- 0 ≤ cost,fare,discount ≤ 100000
- 한 번 쓴 할인권은 다시 못 씁니다.
- 할인 요금은 max(0,fare-discount)

```python
def solution(cost, used, fare, discount):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[4,0,3,5]` | `[[7,0],[4,1]]` |
| `[4,1,3,5]` | `[[7,1]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 기본 후보는 [cost+fare, used]입니다.
2. used=0일 때만 두 번째 후보를 만듭니다.

이번에 안 쓰더라도 이미 사용한 상태는 유지됩니다. 전체 누적 비용에서 할인액을 빼지 않습니다.

```python
def solution(cost, used, fare, discount):
  result = [[cost+fare,used]]
  if used == 0:
    result.append([cost+max(0,fare-discount),1])
  return result
```

</details>

## 2027-02-26 · 가리고 다시 풀기

### 금지된 이웃을 건너뛰는 순열

0~n-1 카드를 모두 한 번씩 놓습니다. forbidden의 두 카드는 어느 순서로도 이웃할 수 없습니다. 가능한 배치를 사전순으로 반환하세요.

- 1 ≤ n ≤ 6
- 금지 쌍은 서로 다른 카드 번호

```python
def solution(n, forbidden):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[3,[[0,1]]]` | `[[0,2,1],[1,2,0]]` |
| `[1,[]]` | `[[0]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. blocked를 2차원 bool 배열로 만들 수 있습니다.
2. path가 비어 있지 않을 때만 path[-1]을 읽으세요.

used[i]는 카드 재사용 검사, blocked는 이웃 조건 검사입니다. 두 배열의 역할을 섞지 않습니다.

```python
def solution(n, forbidden):
  blocked = [[False]*n for _ in range(n)]
  for a,b in forbidden:
    blocked[a][b] = True
    blocked[b][a] = True
  used = [False]*n
  path,res = [],[]
  def dfs():
    if len(path) == n:
      res.append(path[:])
      return
    for i in range(n):
      if used[i] or (path and blocked[path[-1]][i]):
        continue
      used[i] = True
      path.append(i)
      dfs()
      path.pop()
      used[i] = False
  dfs()
  return res
```

</details>

## 2027-02-27 · 토요일 응용

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

## 2027-02-28 · 일요일 전이

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

## 가리고 설명할 질문

풀이를 외운 것과 적용할 수 있는 것을 어떻게 구분하나요?

<details><summary>답 확인</summary>

힌트를 가리고 상태를 설명한 뒤 작은 조건이 바뀐 문제를 구현해 봅니다.

</details>
