# 19주차 · 30분 혼합 모의 주

유형 힌트 없이 상태·전이·종료를 적고 풀어봅니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2027-02-15 · 기본 기술

### 주말 · 배치 한 장을 검수하기

주어진 배치 하나가 올바른지 판단하세요. 모든 카드 번호를 한 번씩 써야 하고, 금지된 두 카드는 어느 순서로도 이웃하면 안 됩니다. 위치(1부터)×밝기의 총합이 target이면 True입니다.

- 1 ≤ 카드 수 ≤ 8
- path 원소는 0 이상 카드 수 미만
- 밝기는 1~9
- 모든 조건을 만족할 때만 True

```python
def solution(brightness, path, forbidden, target):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[2,5,3],[1,0,2],[[1,2]],18]` | `true` |
| `[[2,5,3],[1,0,2],[[0,1]],18]` | `false` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. used를 카드 번호별로 만드세요.
2. 점수 비교는 모든 카드를 확인한 다음에 합니다.

새 배치를 찾는 문제가 아닙니다. 중복·길이, 이웃, 전체 점수의 세 조건을 순서대로 검사합니다.

```python
def solution(brightness, path, forbidden, target):
  n = len(brightness)
  if len(path) != n:
    return False
  used = [False] * n
  score = 0
  for position, card in enumerate(path, start=1):
    if used[card]:
      return False
    used[card] = True
    score += position * brightness[card]
  for i in range(1, n):
    for a, b in forbidden:
      if [path[i-1], path[i]] == [a,b] or [path[i-1], path[i]] == [b,a]:
        return False
  return score == target
```

</details>

## 2027-02-16 · 기본 기술

### 현재 고를 수 있는 작업

아직 처리하지 않은 작업 중 요청 시각이 now 이하인 것만 후보입니다. 소요시간,요청시각,입력 번호 순서로 가장 앞선 작업 번호를 반환하세요. 후보가 없으면 -1입니다.

- 0 ≤ 작업 수 ≤ 1000
- 요청 시각과 now는 0 이상
- 소요시간은 양수

```python
def solution(jobs, now):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,9],[10,1],[2,4]],3]` | `2` |
| `[[[5,1]],4]` | `-1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 먼저 request <= now로 걸러냅니다.
2. 후보의 정렬 키는 처리 순서를 사용합니다.

짧은 작업이어도 미래에 요청되면 후보에 넣지 않습니다.

```python
def solution(jobs, now):
  ready = []
  for job_id,job in enumerate(jobs):
    request,load = job
    if request <= now:
      ready.append([load,request,job_id])
  if not ready:
    return -1
  ready.sort()
  return ready[0][2]
```

</details>

## 2027-02-17 · 기본 기술

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

## 2027-02-18 · 기본 기술

### 동시 이동 한 번만 계산

양수는 오른쪽, 음수는 왼쪽으로 한 칸 동시에 이동합니다. 0은 빈칸입니다. 이동 후 같은 칸에 온 값은 더합니다. 배열 밖으로 나간 것은 버립니다. 한 번 이동한 배열을 반환하세요.

- 1 ≤ 길이 ≤ 10000
- 값은 -100~100

```python
def solution(values):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[3,0,-2]]` | `[0,1,0]` |
| `[[3,-2]]` | `[-2,3]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. nxt는 0으로 시작합니다.
2. 음수의 목적지는 i-1, 양수는 i+1입니다.

원본에서 방향을 읽고 새 배열의 목적지에 +=로 더합니다. 서로 엇갈리면 같은 칸에 도착하지 않으므로 합쳐지지 않습니다.

```python
def solution(values):
  nxt = [0]*len(values)
  for i,value in enumerate(values):
    if value == 0: continue
    dest = i+1 if value > 0 else i-1
    if 0 <= dest < len(values): nxt[dest] += value
  return nxt
```

</details>

## 2027-02-19 · 가리고 다시 풀기

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

## 2027-02-20 · 토요일 응용

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

## 2027-02-21 · 일요일 전이

### 시험 복원 1 · 이진 스티커 최소 교환

N명이 각각 M개의 스티커를 정해진 위치에 가지고 있습니다. sticker[r][c]는 r번 사람의 c번 위치에 있는 스티커 값이며, 값은 0 또는 1입니다. 한 번의 교환에서는 서로 다른 두 사람을 고르고 각 사람의 임의의 위치에서 스티커 하나씩을 골라 맞바꿉니다. 서로 다른 열끼리도 교환할 수 있지만 같은 사람의 두 위치를 직접 교환할 수는 없습니다. 모든 위치의 값이 target과 정확히 일치하도록 만드는 최소 교환 횟수를 반환하세요. 이미 같으면 0입니다. 주어지는 모든 입력은 허용된 교환을 통해 반드시 target과 같게 만들 수 있습니다.

- sticker와 target은 동일한 크기의 직사각형 배열이며 모든 원소는 0 또는 1입니다.
- 한 번의 교환은 서로 다른 행의 위치 두 개를 맞바꾸는 연산입니다.
- 행 안의 순서까지 일치해야 합니다. 목표와 이미 일치한 위치도 교환에 사용할 수 있습니다.
- 허용된 교환으로 sticker를 target과 같게 만들 수 있는 입력만 주어집니다. 불가능한 경우는 처리하지 않습니다.
- 이 빌드업 과정의 연습 범위는 전체 12칸 이하입니다. 목표 도달이 보장됩니다.

```python
def solution(sticker, target):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[1],[0]],[[1],[0]]]` | `0` |
| `[[[1,0],[0,0]],[[0,0],[1,0]]]` | `1` |
| `[[[1,0,0],[0,0,0]],[[0,0,1],[0,0,0]]]` | `2` |
| `[[[1,1,0,0],[0,0,0,0]],[[0,0,1,1],[0,0,0,0]]]` | `4` |
| `[[[1,1,1,0,0],[0,0,0,0,0]],[[0,0,0,0,0],[1,0,1,0,1]]]` | `3` |
| `[[[1,1,1,1],[1,1,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,1,1],[1,1,1,1]]]` | `6` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 큐에 [배치 전체, 교환 횟수]를 넣으세요.
2. 서로 다른 행의 두 칸을 골라 새 배열에서 교환하세요.
3. visited에는 전체 배치를 넣고, 같은 배치를 다시 큐에 넣지 마세요.

전체 배치가 상태이고 교환 한 번이 이동 한 번입니다. visited = [sticker]는 처음 확인한 배치를 저장한 리스트입니다. visited는 어느 칸을 방문했는지가 아니라 어떤 전체 배치를 확인했는지를 기록합니다. if nxt in visited는 nxt와 모든 칸의 값이 같은 배치가 이미 저장되어 있는지 비교합니다. 처음 보는 배치만 visited.append(nxt)로 기록하고 큐에 넣습니다. 교환 횟수는 visited에 넣지 않습니다.

```python
from collections import deque

def solution(sticker, target):
  N, M = len(sticker), len(sticker[0])
  q = deque()
  q.append([sticker, 0])

  # 방문한 칸이 아니라 방문한 배치 전체를 저장합니다.
  visited = [sticker]

  while q:
    arr, cnt = q.popleft()
    if arr == target:
      return cnt

    # 서로 다른 두 행에서 교환할 칸을 하나씩 고릅니다.
    for r1 in range(N):
      for r2 in range(r1 + 1, N):
        for c1 in range(M):
          for c2 in range(M):
            if arr[r1][c1] == arr[r2][c2]:
              continue

            # 현재 배치를 바꾸지 않도록 각 행까지 복사합니다.
            nxt = [row[:] for row in arr]
            temp = nxt[r1][c1]
            nxt[r1][c1] = nxt[r2][c2]
            nxt[r2][c2] = temp

            if nxt in visited:
              continue

            visited.append(nxt)
            q.append([nxt, cnt + 1])
```

</details>

## 가리고 설명할 질문

풀이 전 종이에 적을 세 문장은?

<details><summary>답 확인</summary>

상태가 무엇인지, 한 번의 선택/이동이 무엇인지, 언제 답이 완성되는지입니다.

</details>
