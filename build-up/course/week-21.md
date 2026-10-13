# 21주차 · 마지막 주 · 익숙한 흐름 확인

새 고난도 유형 대신 자주 틀린 초기화·복사·반환 위치를 확인합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2027-03-01 · 기본 기술

### 자리 번호와 카드 번호

path는 왼쪽부터 놓은 카드 번호입니다. 위치 번호는 1부터 시작합니다. 위치 번호 × 해당 카드 밝기를 모두 더해 반환하세요. 카드는 0번부터 시작합니다.

- 1 ≤ 카드 수 ≤ 20
- path는 모든 카드 번호를 한 번씩 포함합니다.
- 1 ≤ 밝기 ≤ 20

```python
def solution(brightness, path):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[2,5,3],[1,0,2]]` | `18` |
| `[[7],[0]]` | `7` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. enumerate(path, start=1)의 두 값에 각각 이름을 붙이세요.
2. score는 반복 전에 0, 반복 안에서는 +=로 누적합니다.

position은 놓인 순서이고 card는 원래 카드 번호입니다. brightness[card]를 읽고 position을 곱합니다.

```python
def solution(brightness, path):
  score = 0
  for position, card in enumerate(path, start=1):
    score += position * brightness[card]
  return score
```

</details>

## 2027-03-02 · 기본 기술

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

## 2027-03-03 · 기본 기술

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

## 2027-03-04 · 기본 기술

### 길이가 정해진 창의 종류 수

길이 k인 모든 연속 구간에 들어 있는 서로 다른 값의 개수를 왼쪽부터 반환하세요.

- 1 ≤ k ≤ 길이 ≤ 100000
- 각 값은 정수

```python
def solution(items, k):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[1,1,2,3,2],3]` | `[2,3,2]` |
| `[[5,5],1]` | `[1,1]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. count와 l을 함께 유지하세요.
2. 구간이 k칸일 때만 결과에 len(count)를 넣습니다.

오른쪽 값을 추가하고 길이가 k를 넘으면 왼쪽 값 한 개를 뺍니다. 개수가 0일 때만 종류가 사라집니다.

```python
def solution(items, k):
  count = {}
  res = []
  left = 0
  for right,value in enumerate(items):
    count[value] = count.get(value,0)+1
    if right-left+1 > k:
      old = items[left]
      count[old] -= 1
      if count[old] == 0: del count[old]
      left += 1
    if right-left+1 == k:
      res.append(len(count))
  return res
```

</details>

## 2027-03-05 · 가리고 다시 풀기

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

## 2027-03-06 · 토요일 응용

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

## 2027-03-07 · 일요일 전이

### 주말 · 서로 독립인 교환 후보

swaps의 각 [r1,c1,r2,c2]를 원래 board에 딱 한 번 적용한 배열들을 순서대로 반환하세요. 앞 교환의 결과에 다음 교환을 이어 적용하지 않습니다. 원본도 유지하세요.

- 행·열 수는 1~5
- 교환 후보는 0~10개
- 좌표는 유효합니다.

```python
def solution(board, swaps):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[1,2],[3,4]],[[0,0,1,1],[0,0,0,1]]]` | `[[[4,2],[3,1]],[[2,1],[3,4]]]` |
| `[[[7]],[[0,0,0,0]]]` | `[[[7]]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. nxt를 만드는 위치는 swaps 반복문 안입니다.
2. res.append(nxt) 뒤에도 board를 수정하지 마세요.

분기들은 같은 부모에서 출발합니다. 후보마다 원본을 복사해야 합니다.

```python
def solution(board, swaps):
  res = []
  for r1, c1, r2, c2 in swaps:
    nxt = [row[:] for row in board]
    temp = nxt[r1][c1]
    nxt[r1][c1] = nxt[r2][c2]
    nxt[r2][c2] = temp
    res.append(nxt)
  return res
```

</details>

## 2027-03-08 · 가벼운 점검

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

## 가리고 설명할 질문

마지막 점검에서 먼저 볼 네 가지는?

<details><summary>답 확인</summary>

초기값, 상태에 필요한 정보, 갱신/방문 시점, 완료 후 반환 위치입니다.

</details>
