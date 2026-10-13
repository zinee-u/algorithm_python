# 7주차 · 추가 정보를 가진 BFS

위치가 같아도 소지품이 다르면 다른 상태임을 익힙니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-11-23 · 기본 기술

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

## 2026-11-24 · 기본 기술

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

## 2026-11-25 · 기본 기술

### 주말 · 열쇠가 있어야 지나는 문

S에서 E까지 최소 이동 횟수를 구하세요. K를 밟으면 열쇠를 얻으며 D는 열쇠가 있어야 통과합니다. #은 벽입니다. 열쇠는 사라지지 않습니다. 불가능하면 -1입니다.

- 행·열 1~20
- S,E는 각각 하나, K는 0~1개

```python
def solution(board):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[["SKDE"]]` | `3` |
| `[["SDE"]]` | `-1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 스탬프 문제와 같은 3차원 visited입니다.
2. 보유하지 않은 상태에서 D로 가는 후보만 건너뜁니다.

좌표와 열쇠 보유 상태를 함께 저장합니다. 문 통과 조건은 다음 칸을 검사할 때 확인합니다.

```python
from collections import deque
def solution(board):
  N,M = len(board),len(board[0])
  for r in range(N):
    for c in range(M):
      if board[r][c] == 'S': sr,sc = r,c
  visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
  q = deque([[sr,sc,0,0]])
  visited[sr][sc][0] = True
  while q:
    r,c,key,cnt = q.popleft()
    if board[r][c] == 'E': return cnt
    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
      nr,nc = r+dr,c+dc
      if not (0 <= nr < N and 0 <= nc < M): continue
      cell = board[nr][nc]
      if cell == '#' or (cell == 'D' and not key): continue
      nxt_key = 1 if cell == 'K' else key
      if visited[nr][nc][nxt_key]: continue
      visited[nr][nc][nxt_key] = True
      q.append([nr,nc,nxt_key,cnt+1])
  return -1
```

</details>

## 2026-11-26 · 기본 기술

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

## 2026-11-27 · 가리고 다시 풀기

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

## 2026-11-28 · 토요일 응용

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

## 2026-11-29 · 일요일 전이

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

## 가리고 설명할 질문

좌표만 방문 처리해도 되는지 어떻게 판단하나요?

<details><summary>답 확인</summary>

같은 좌표에서 앞으로 가능한 행동이 달라지는 추가 정보(스탬프/열쇠)가 있으면 상태에 포함해야 합니다.

</details>
