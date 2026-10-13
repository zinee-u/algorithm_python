# 10주차 · 상태별 최저 비용

할인권·진입 방향별로 기록을 분리합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-12-14 · 기본 기술

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

## 2026-12-15 · 기본 기술

### 첫 이동에는 코너가 없다

방향 번호 0,1,2,3으로 이루어진 이동 기록의 도로 비용을 구하세요. 한 이동은 100, 직전 이동과 방향이 다르면 추가 500입니다. 첫 이동에는 추가 비용이 없습니다. 실제 격자 경로 가능성은 검사하지 않습니다.

- 0 ≤ 길이 ≤ 10000

```python
def solution(directions):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[0,0,1]]` | `800` |
| `[[2]]` | `100` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 매번 기본 100을 더합니다.
2. prv != -1 and prv != direction일 때 추가 500입니다.

첫 방향은 -1로 두고 직전 방향이 존재할 때만 비교합니다.

```python
def solution(directions):
  total = 0
  prv = -1
  for direction in directions:
    total += 100
    if prv != -1 and prv != direction:
      total += 500
    prv = direction
  return total
```

</details>

## 2026-12-16 · 기본 기술

### 각 후보에 스탬프 복사하기

현재 보유 상태 is_a,is_b와 다음 이동 후보 칸들의 문자 목록 cells가 주어집니다. 후보마다 독립적으로 도착했을 때의 [A보유,B보유]를 반환하세요. A 또는 B를 밟으면 해당 값이 1이 됩니다.

- is_a,is_b는 0 또는 1
- cells는 A,B,. 중 0~4개

```python
def solution(is_a, is_b, cells):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[0,0,["A",".","B"]]` | `[[1,0],[0,0],[0,1]]` |
| `[1,0,["B","."]]` | `[[1,1],[1,0]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 현재 is_a,is_b를 직접 변경하지 마세요.
2. 각 후보의 초기값은 이전 후보 결과가 아닙니다.

반복문 안에서 nxt_a,nxt_b를 현재 상태에서 다시 만들어야 다른 방향에 스탬프가 새지 않습니다.

```python
def solution(is_a, is_b, cells):
  res = []
  for cell in cells:
    nxt_a,nxt_b = is_a,is_b
    if cell == 'A':
      nxt_a = 1
    if cell == 'B':
      nxt_b = 1
    res.append([nxt_a,nxt_b])
  return res
```

</details>

## 2026-12-17 · 기본 기술

### 주말 · 방향을 기억하는 최저 비용

0은 빈 칸,1은 벽인 정사각형에서 좌상단부터 우하단까지 도로를 만드세요. 한 칸 100, 이전 방향과 달라지면 추가 500입니다. 첫 이동은 100입니다. 최저 비용을 반환하고 갈 수 없으면 -1입니다.

- 1 ≤ N ≤ 15
- 시작과 끝은 빈 칸
- 상하좌우로 이동

```python
def solution(board):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,0],[0,0]]]` | `700` |
| `[[[0]]]` | `0` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 출발 방향을 -1로 두세요.
2. 힙에는 갱신한 비용을 넣고, 갱신하지 못했다면 넣지 않습니다.

같은 칸에 와도 들어온 방향에 따라 다음 이동 비용이 다릅니다. dist[r][c][direction]으로 분리합니다.

```python
import heapq
def solution(board):
  N = len(board)
  INF = float('inf')
  dist = [[[INF]*4 for _ in range(N)] for _ in range(N)]
  dist[0][0] = [0,0,0,0]
  heap = [[0,0,0,-1]]
  dr,dc = [-1,0,1,0],[0,-1,0,1]
  while heap:
    cost,r,c,prv = heapq.heappop(heap)
    if prv != -1 and cost > dist[r][c][prv]: continue
    for d in range(4):
      nr,nc = r+dr[d],c+dc[d]
      if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc]: continue
      candidate = cost+100
      if prv != -1 and prv != d: candidate += 500
      if candidate < dist[nr][nc][d]:
        dist[nr][nc][d] = candidate
        heapq.heappush(heap,[candidate,nr,nc,d])
  result = min(dist[N-1][N-1])
  return -1 if result == INF else result
```

</details>

## 2026-12-18 · 가리고 다시 풀기

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

## 2026-12-19 · 토요일 응용

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

## 2026-12-20 · 일요일 전이

### 주말 · 방향을 기억하는 최저 비용

0은 빈 칸,1은 벽인 정사각형에서 좌상단부터 우하단까지 도로를 만드세요. 한 칸 100, 이전 방향과 달라지면 추가 500입니다. 첫 이동은 100입니다. 최저 비용을 반환하고 갈 수 없으면 -1입니다.

- 1 ≤ N ≤ 15
- 시작과 끝은 빈 칸
- 상하좌우로 이동

```python
def solution(board):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,0],[0,0]]]` | `700` |
| `[[[0]]]` | `0` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 출발 방향을 -1로 두세요.
2. 힙에는 갱신한 비용을 넣고, 갱신하지 못했다면 넣지 않습니다.

같은 칸에 와도 들어온 방향에 따라 다음 이동 비용이 다릅니다. dist[r][c][direction]으로 분리합니다.

```python
import heapq
def solution(board):
  N = len(board)
  INF = float('inf')
  dist = [[[INF]*4 for _ in range(N)] for _ in range(N)]
  dist[0][0] = [0,0,0,0]
  heap = [[0,0,0,-1]]
  dr,dc = [-1,0,1,0],[0,-1,0,1]
  while heap:
    cost,r,c,prv = heapq.heappop(heap)
    if prv != -1 and cost > dist[r][c][prv]: continue
    for d in range(4):
      nr,nc = r+dr[d],c+dc[d]
      if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc]: continue
      candidate = cost+100
      if prv != -1 and prv != d: candidate += 500
      if candidate < dist[nr][nc][d]:
        dist[nr][nc][d] = candidate
        heapq.heappush(heap,[candidate,nr,nc,d])
  result = min(dist[N-1][N-1])
  return -1 if result == INF else result
```

</details>

## 가리고 설명할 질문

이번에 할인권을 안 쓰면 used를 0으로 바꾸나요?

<details><summary>답 확인</summary>

아니요. 기존 used를 유지합니다. 이미 사용했으면 계속 1이고, 미사용 상태에서만 사용 전이가 가능합니다.

</details>
