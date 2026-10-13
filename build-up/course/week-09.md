# 9주차 · 최소 비용과 갱신

비용 초기화, 후보 비용, 오래된 힙 항목을 구분합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-12-07 · 기본 기술

### 요금과 목적지의 자리

0번부터 n-1번까지 방향 있는 도로 [출발,도착,요금]을 연결 목록으로 바꾸세요. graph[node]의 각 원소는 [다음노드,요금]이며 입력 순서를 유지합니다.

- 1 ≤ n ≤ 100
- 간선 수 0~500
- 요금은 0 이상

```python
def solution(n, roads):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[3,[[0,1,5],[0,2,2]]]` | `[[[1,5],[2,2]],[],[]]` |
| `[1,[]]` | `[[]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 반대 방향을 자동으로 추가하지 마세요.
2. 각 노드의 리스트를 독립적으로 만드세요.

연결 목록과 힙의 필드 순서는 다를 수 있습니다. graph는 [다음노드,요금], heap은 [총비용,노드]입니다.

```python
def solution(n, roads):
  graph = [[] for _ in range(n)]
  for a,b,w in roads:
    graph[a].append([b,w])
  return graph
```

</details>

## 2026-12-08 · 기본 기술

### 기존 기록과 후보 비용 비교

dist에는 시작점에서 각 노드까지 현재 알려진 비용이 있고 -1은 아직 모름입니다. node는 비용을 아는 노드입니다. edges의 [다음노드,요금]으로 한 번씩 이동한 후보를 반영한 새 dist를 반환하세요. 입력은 바꾸지 않습니다.

- 노드 수 1~100
- 요금은 0 이상
- edges의 목적지는 node와 다릅니다.

```python
def solution(dist, node, edges):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[0,7,-1],0,[[1,3],[2,8]]]` | `[0,3,8]` |
| `[[0,2,9],1,[[2,4]]]` | `[0,2,6]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. candidate = dist[node] + weight입니다.
2. 기존 기록이 없거나 candidate가 더 작을 때 갱신하세요.

후보는 현재 노드 비용+이동 요금입니다. 도착 노드의 기존 비용에 더하는 것이 아닙니다.

```python
def solution(dist, node, edges):
  result = dist[:]
  for nxt,weight in edges:
    candidate = dist[node]+weight
    if result[nxt] == -1 or candidate < result[nxt]:
      result[nxt] = candidate
  return result
```

</details>

## 2026-12-09 · 기본 기술

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

## 2026-12-10 · 기본 기술

### 기존 기록과 후보 비용 비교

dist에는 시작점에서 각 노드까지 현재 알려진 비용이 있고 -1은 아직 모름입니다. node는 비용을 아는 노드입니다. edges의 [다음노드,요금]으로 한 번씩 이동한 후보를 반영한 새 dist를 반환하세요. 입력은 바꾸지 않습니다.

- 노드 수 1~100
- 요금은 0 이상
- edges의 목적지는 node와 다릅니다.

```python
def solution(dist, node, edges):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[0,7,-1],0,[[1,3],[2,8]]]` | `[0,3,8]` |
| `[[0,2,9],1,[[2,4]]]` | `[0,2,6]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. candidate = dist[node] + weight입니다.
2. 기존 기록이 없거나 candidate가 더 작을 때 갱신하세요.

후보는 현재 노드 비용+이동 요금입니다. 도착 노드의 기존 비용에 더하는 것이 아닙니다.

```python
def solution(dist, node, edges):
  result = dist[:]
  for nxt,weight in edges:
    candidate = dist[node]+weight
    if result[nxt] == -1 or candidate < result[nxt]:
      result[nxt] = candidate
  return result
```

</details>

## 2026-12-11 · 가리고 다시 풀기

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

## 2026-12-12 · 토요일 응용

### 공유 작업실의 부품 운반 시간

작업실 사이의 일방통행 운반로를 여러 번 이어서 사용할 수 있습니다. solution(n, roads, start)를 작성해 start에서 각 작업실까지의 최소 운반 시간을 번호 순서대로 담은 길이 n의 정수 리스트를 반환하세요. start의 시간은 0, 도달할 수 없는 작업실의 값은 -1입니다. 같은 최소 시간을 만드는 경로가 여러 개여도 시간만 반환하며, 경로 자체를 고르지 않습니다.

- 1 ≤ n ≤ 50,000, 0 ≤ len(roads) ≤ 150,000.
- 1 ≤ start ≤ n. 각 roads 원소는 정수 [a, b, time]이며 1 ≤ a, b ≤ n입니다.
- 0 ≤ time ≤ 1,000,000,000. 음수 시간은 없습니다.
- [a, b, time]은 a → b에만 적용됩니다. 반대 방향은 별도의 원소가 있을 때만 사용 가능합니다.
- 같은 두 작업실을 잇는 여러 운반로, 완전히 같은 원소, 자기 자신으로 향하는 운반로가 있을 수 있습니다.
- 최소 시간 합은 32비트 정수 범위를 넘을 수 있습니다. 입력 순서는 경로 순서와 무관합니다.

```python
def solution(n, roads, start):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[5,[[1,2,9],[1,3,2],[3,2,1],[2,4,4],[3,4,10]],1]` | `[0,3,2,7,-1]` |
| `[4,[[4,2,0],[2,3,5],[4,3,8],[3,1,2],[2,3,5]],4]` | `[7,0,5,0]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 운반로 개수가 아니라 시간 합을 최소화해야 합니다. 지금까지 발견한 시간 중 가장 작은 작업실부터 처리하려면 어떤 자료구조가 필요할까요?
2. distance[v]는 현재까지 발견한 v의 최선 시간입니다. 더 짧은 경로를 찾으면 새 항목을 힙에 넣고, 나중에 꺼낸 오래된 항목의 시간이 distance[v]와 다르면 무시하세요.
3. 인접 리스트와 heapq를 사용하세요. (시간, 작업실)을 저장하고 새 시간이 더 작을 때만 갱신합니다. 마지막에 무한대인 값을 -1로 바꾸세요.

각 작업실의 최선 시간을 distance에 두고 시작점을 0으로 설정합니다. 최소 힙에서 (시간, 작업실)을 꺼내면 distance와 같은 항목만 확장합니다. 처음에는 긴 경로로 등록했던 작업실이 나중에 짧은 경로로 다시 등록될 수 있으므로 힙의 오래된 항목을 건너뛰는 조건이 필요합니다. 운반 시간이 음수가 아니어서 가장 작은 유효 시간을 먼저 꺼내는 다익스트라 알고리즘을 사용할 수 있습니다. 시간 복잡도는 O((n + m) log(m + 1)), 공간 복잡도는 O(n + m)이며 m은 운반로 수입니다.

```python
import heapq

def solution(n, roads, start):
  graph = [[] for _ in range(n + 1)]
  for a, b, cost in roads:
    graph[a].append((b, cost))
  distance = [float('inf')] * (n + 1)
  distance[start] = 0
  queue = [(0, start)]
  while queue:
    cost, node = heapq.heappop(queue)
    if cost != distance[node]:
      continue
    for neighbor, weight in graph[node]:
      candidate = cost + weight
      if candidate < distance[neighbor]:
        distance[neighbor] = candidate
        heapq.heappush(queue, (candidate, neighbor))
  return [-1 if value == float('inf') else value
          for value in distance[1:]]
```

</details>

## 2026-12-13 · 일요일 전이

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

## 가리고 설명할 질문

다음 후보 비용과 오래된 항목을 버리는 조건은?

<details><summary>답 확인</summary>

candidate=현재 누적비용+간선 요금입니다. 꺼낸 비용이 dist[node]보다 크면 오래된 항목입니다.

</details>
