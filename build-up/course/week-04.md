# 4주차 · BFS의 거리와 방문

큐에 넣는 순간 방문 처리하고 거리의 기준을 정합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-11-02 · 기본 기술

### 방향에 맞는 연결 목록

노드는 0부터 n-1까지입니다. roads=[a,b]를 연결 목록으로 바꾸세요. directed=True면 a→b만, False면 양방향을 추가합니다. 각 목록은 오름차순이며 중복 간선은 그대로 둡니다.

- 1 ≤ n ≤ 30
- 0 ≤ 간선 수 ≤ 100

```python
def solution(n, roads, directed):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[3,[[0,1],[1,2]],true]` | `[[1],[2],[]]` |
| `[3,[[0,1]],false]` | `[[1],[0],[]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. [] * n은 여전히 빈 리스트입니다.
2. 양방향일 때만 반대쪽도 추가하세요.

graph = [[] for _ in range(n)]으로 노드별 독립 리스트를 만듭니다.

```python
def solution(n, roads, directed):
  graph = [[] for _ in range(n)]
  for a, b in roads:
    graph[a].append(b)
    if not directed:
      graph[b].append(a)
  for row in graph:
    row.sort()
  return graph
```

</details>

## 2026-11-03 · 기본 기술

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

## 2026-11-04 · 기본 기술

### 가장 가까운 충전소

양방향 연결 목록과 충전소 노드 목록 starts가 주어집니다. 각 노드에서 가장 가까운 충전소까지 거리를 반환하세요. 충전소가 없거나 갈 수 없으면 -1입니다.

- 1 ≤ 노드 수 ≤ 1000
- starts에는 중복이 없습니다.

```python
def solution(graph, starts):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[1],[0,2],[1,3],[2]],[0,3]]` | `[0,1,1,0]` |
| `[[[1],[0]],[]]` | `[-1,-1]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 시작점마다 BFS를 다시 할 필요가 없습니다.
2. 시작점들의 dist는 전부 0입니다.

모든 시작점을 거리 0으로 큐에 넣으면 한 번의 BFS로 동시에 퍼집니다.

```python
from collections import deque
def solution(graph, starts):
  dist = [-1] * len(graph)
  q = deque()
  for start in starts:
    dist[start] = 0
    q.append(start)
  while q:
    node = q.popleft()
    for nxt in graph[node]:
      if dist[nxt] == -1:
        dist[nxt] = dist[node] + 1
        q.append(nxt)
  return dist
```

</details>

## 2026-11-05 · 기본 기술

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

## 2026-11-06 · 가리고 다시 풀기

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

## 2026-11-07 · 토요일 응용

### 전시장 안내 데스크까지

전시장은 0번부터 n - 1번까지의 구역으로 나뉘어 있습니다. passages의 [a, b]는 a에서 b로, 또는 b에서 a로 이동할 수 있는 통로입니다. 통로 하나를 지나는 데에는 항상 이동 1회가 필요합니다. solution(n, passages, start, goal)을 완성하여 start에서 goal까지 필요한 최소 이동 횟수를 정수로 반환하세요. 도달할 수 없다면 -1을 반환하고, 출발 구역과 목적 구역이 같다면 0을 반환합니다.

- 1 ≤ n ≤ 100
- 구역 번호는 0 이상 n - 1 이하의 정수입니다.
- 0 ≤ len(passages) ≤ n × (n - 1) / 2
- 각 통로는 서로 다른 두 구역을 연결하며, 같은 양방향 통로가 중복해서 주어지지 않습니다.
- 모든 통로의 이동 비용은 1이며, 모든 구역이 연결되어 있다는 보장은 없습니다.

```python
def solution(n, passages, start, goal):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[6,[[0,1],[1,2],[0,3],[3,4],[4,2],[2,5]],0,5]` | `3` |
| `[5,[[0,1],[1,2],[3,4]],0,4]` | `-1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 통로마다 이동 비용이 모두 1입니다. 출발점에서 1회, 2회, 3회 만에 갈 수 있는 구역 순서로 탐색하는 방법을 떠올려 보세요.
2. 각 구역을 처음 발견했을 때 기록한 이동 횟수가 최단 거리입니다. 방문하지 않은 구역은 거리 -1로 표시하고, 큐에 넣는 순간 거리를 기록하세요.
3. 양방향 인접 리스트와 collections.deque를 사용하세요. start의 거리를 0으로 두고, 현재 구역에서 처음 발견한 이웃의 거리를 현재 거리 + 1로 정합니다. 탐색이 끝난 뒤 goal의 거리를 반환하면 됩니다.

통로 정보를 양쪽 인접 리스트에 추가합니다. distance[start] = 0으로 초기화하고 출발 구역을 큐에 넣습니다. 큐에서 구역을 꺼낼 때마다 아직 방문하지 않은 이웃에 현재 거리 + 1을 기록하고 큐에 넣습니다. 큐는 거리가 작은 구역부터 처리하므로 처음 기록한 거리가 최단 거리입니다. 거리를 기록한 구역은 다시 넣지 않아 순환 통로에서도 종료됩니다. goal의 거리가 끝까지 -1이면 도달할 수 없습니다. 시간 복잡도는 O(n + len(passages)), 공간 복잡도도 O(n + len(passages))입니다.

```python
from collections import deque

def solution(n, passages, start, goal):
  graph = [[] for _ in range(n)]
  for a, b in passages:
    graph[a].append(b)
    graph[b].append(a)

  distance = [-1] * n
  distance[start] = 0
  queue = deque([start])

  while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
      if distance[neighbor] != -1:
        continue
      distance[neighbor] = distance[current] + 1
      queue.append(neighbor)

  return distance[goal]
```

</details>

## 2026-11-08 · 일요일 전이

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

## 가리고 설명할 질문

BFS는 언제 방문 처리하고 다음 거리는 무엇인가요?

<details><summary>답 확인</summary>

큐에 넣을 때 방문 처리합니다. 다음 거리는 현재 거리+1입니다. 출발 거리는 0입니다.

</details>
