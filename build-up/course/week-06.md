# 6주차 · 백트래킹의 선택과 복구

카드 번호별 사용 기록을 만들고 형제 분기의 상태를 복구합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-11-16 · 기본 기술

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

## 2026-11-17 · 기본 기술

### 순서 없는 선택

0~n-1 카드 중 length개를 뽑되 순서만 다른 선택은 한 번만 반환하세요. 각 선택과 전체 결과는 오름차순입니다.

- 1 ≤ n ≤ 8
- 0 ≤ length ≤ n

```python
def solution(n, length):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[4,2]` | `[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]` |
| `[3,0]` | `[[]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. dfs(start)를 사용하세요.
2. 같은 카드를 다시 쓰지 않으므로 dfs(i)가 아니라 dfs(i+1)입니다.

다음 후보의 시작을 i+1로 넘기면 이미 선택한 번호보다 큰 것만 고릅니다. 순열과 달리 모든 번호로 돌아가지 않습니다.

```python
def solution(n, length):
  res,path = [],[]
  def dfs(start):
    if len(path) == length:
      res.append(path[:])
      return
    for i in range(start,n):
      path.append(i)
      dfs(i+1)
      path.pop()
  dfs(0)
  return res
```

</details>

## 2026-11-18 · 기본 기술

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

## 2026-11-19 · 기본 기술

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

## 2026-11-20 · 가리고 다시 풀기

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

## 2026-11-21 · 토요일 응용

### 전시 카드 배치 점수

0번부터 n - 1번까지의 전시 카드를 한 줄에 한 번씩 모두 놓으려고 합니다. n은 len(brightness)이고, i번 카드의 밝기는 brightness[i]입니다. 왼쪽부터 위치 번호를 1, 2, ..., n으로 매겼을 때 배치 점수는 각 카드의 위치 번호 × 밝기를 모두 더한 값입니다. forbidden의 [a, b]에 있는 두 카드는 어느 쪽 순서로도 서로 나란히 놓을 수 없습니다. solution(brightness, forbidden, target)을 완성하여 점수가 정확히 target이고 금지 조건을 모두 지키는 배치를 이차원 리스트로 반환하세요. 배치 하나는 왼쪽부터 놓인 카드 번호의 리스트입니다. 전체 결과는 카드 번호의 사전순으로 정렬하고, 가능한 배치가 없다면 빈 리스트 []를 반환합니다. 밝기가 같은 카드라도 번호가 다르면 서로 다른 카드입니다.

- 1 ≤ n = len(brightness) ≤ 7
- 1 ≤ brightness[i] ≤ 9
- 1 ≤ target ≤ 9 × n × (n + 1) / 2인 정수입니다.
- 0 ≤ len(forbidden) ≤ n × (n - 1) / 2
- 금지 쌍은 0 이상 n - 1 이하의 서로 다른 두 카드 번호로 이루어집니다.
- [a, b]와 [b, a]는 같은 금지 조건을 뜻하며, 같은 조건은 중복해서 주어지지 않습니다.
- 금지 조건은 한 줄에서 바로 이웃한 두 카드에만 적용됩니다. 양 끝을 원처럼 연결하지 않습니다.
- 사전순은 두 배치를 왼쪽부터 비교하여 처음으로 다른 카드 번호가 나온 위치에서 더 작은 번호를 가진 배치를 앞에 두는 순서입니다.

```python
def solution(brightness, forbidden, target):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[1,2,3],[[0,1]],13]` | `[[0,2,1]]` |
| `[[2,2,2],[[0,2]],12]` | `[[0,1,2],[2,1,0]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 왼쪽부터 카드를 하나씩 놓으며 순열을 만드세요. 새 카드가 들어갈 위치와 바로 앞 카드만 알면, 새 점수와 새롭게 생기는 금지 조건 위반을 바로 확인할 수 있습니다.
2. path에 들어 있는 번호만 visited가 True여야 하고, score는 현재 path의 위치별 점수 합이어야 합니다. 다음 카드는 미사용 카드여야 하며 마지막 카드와 금지 쌍이면 제외합니다. 밝기가 모두 양수이므로 부분 점수가 target을 넘으면 그 경로는 실패입니다.
3. 대칭인 금지 행렬을 만들고 dfs(score)에서 카드 번호를 0부터 차례로 시도하세요. 새 점수는 score + (len(path) + 1) * brightness[card]입니다. 선택·재귀 호출·복구 순서를 지키고, n개를 놓았을 때 점수가 target이면 path.copy()를 저장합니다.

카드 번호를 기준으로 visited를 관리해야 밝기가 같은 카드도 각각 사용할 수 있습니다. forbidden을 양방향으로 표시한 행렬을 만든 뒤, DFS에서 미사용 카드를 작은 번호부터 선택합니다. 직전 카드와 금지 쌍인 선택은 건너뛰고, 새 카드가 들어갈 위치를 반영하여 점수를 누적합니다. 밝기가 양수이므로 이미 목표를 넘은 경로는 더 진행할 필요가 없습니다. 모든 카드를 놓았을 때 점수가 정확히 target이면 현재 경로의 복사본을 저장합니다. 재귀 호출 후에는 경로와 방문 표시를 반드시 복구합니다. 작은 카드 번호부터 탐색하므로 결과는 사전순입니다. 시간 복잡도는 최악의 경우 O(n × n!)입니다. 유효한 배치 수를 K라 하면 결과 공간은 O(nK), 금지 행렬을 포함한 결과 외 추가 공간은 O(n²)입니다.

```python
def solution(brightness, forbidden, target):
  count = len(brightness)
  banned = [[False] * count for _ in range(count)]
  for a, b in forbidden:
    banned[a][b] = True
    banned[b][a] = True

  visited = [False] * count
  path = []
  answer = []

  def dfs(score):
    if len(path) == count:
      if score == target:
        answer.append(path.copy())
      return

    position = len(path) + 1
    for card in range(count):
      if visited[card]:
        continue
      if path and banned[path[-1]][card]:
        continue
      next_score = score + position * brightness[card]
      if next_score > target:
        continue
      visited[card] = True
      path.append(card)
      dfs(next_score)
      path.pop()
      visited[card] = False

  dfs(0)
  return answer
```

</details>

## 2026-11-22 · 일요일 전이

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

## 가리고 설명할 질문

DFS의 used와 BFS의 visited는 언제 되돌리나요?

<details><summary>답 확인</summary>

백트래킹 used는 현재 경로만 나타내므로 돌아오면 복구합니다. BFS visited는 확인한 상태를 계속 기억합니다.

</details>
