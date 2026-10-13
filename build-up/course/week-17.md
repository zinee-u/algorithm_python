# 17주차 · 분기와 복사 복습 주

분기 간 상태 오염을 독립 실행과 복구 두 방식으로 해결합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2027-02-01 · 기본 기술

### 원본을 지키는 수정본

각 changes 원소 [r,c,value]를 순서대로 적용한 새 배열을 반환하세요. r,c는 0부터 시작합니다. 입력 board는 바꾸면 안 됩니다.

- 1 ≤ 행·열 수 ≤ 10
- 0 ≤ 변경 횟수 ≤ 20
- 모든 좌표는 범위 안입니다.

```python
def solution(board, changes):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[1,2],[3,4]],[[0,1,9]]]` | `[[1,9],[3,4]]` |
| `[[[1]],[[0,0,2],[0,0,5]]]` | `[[5]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. nxt = board는 복사가 아닙니다.
2. 행마다 row[:]로 복사한 뒤 changes를 반복하세요.

바깥 리스트만 복사하면 행은 공유됩니다. [row[:] for row in board]로 행까지 복사하고 새 배열만 수정합니다.

```python
def solution(board, changes):
  nxt = [row[:] for row in board]
  for r, c, value in changes:
    nxt[r][c] = value
  return nxt
```

</details>

## 2027-02-02 · 기본 기술

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

## 2027-02-03 · 기본 기술

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

## 2027-02-04 · 기본 기술

### 동시에 한 칸 이동

모든 값을 동시에 오른쪽으로 한 칸 옮기세요. 맨 오른쪽 값은 버리고 새 맨 왼쪽은 0입니다. 입력은 수정하지 않고 결과를 반환하세요.

- 1 ≤ 길이 ≤ 10000

```python
def solution(values):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[1,2,3,4]]` | `[0,1,2,3]` |
| `[[9]]` | `[0]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. nxt를 0으로 채워 만드세요.
2. 원래 i의 값은 새 i+1에 들어갑니다.

읽을 원본과 쓸 결과를 분리합니다. 앞에서 바꾼 값을 다음 칸이 다시 읽으면 안 됩니다.

```python
def solution(values):
  nxt = [0] * len(values)
  for i in range(len(values)-1):
    nxt[i+1] = values[i]
  return nxt
```

</details>

## 2027-02-05 · 가리고 다시 풀기

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

## 2027-02-06 · 토요일 응용

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

## 2027-02-07 · 일요일 전이

### 전시 패널의 부분 회전

전시 패널에서 지정된 정사각형의 일부 칸만 회전하려고 합니다. 각 연산 [top, left, size, d]는 (top, left)를 왼쪽 위로 하는 size × size 부분 배열에 적용합니다. 이 부분 배열 안의 주 대각선, 가운데 열, 부 대각선, 가운데 행의 원소만 그 부분 배열의 중심을 기준으로 d도 회전합니다. 시계 방향 45도 한 번은 주 대각선 → 가운데 열 → 부 대각선 → 가운데 행 → 주 대각선의 이동을 동시에 적용합니다. 부분 배열의 왼쪽 위 원소는 가운데 열 맨 위로, 가운데 열 맨 위 원소는 오른쪽 위로 이동합니다. 네 줄 이외의 칸, 중심 칸, 부분 배열 밖의 칸은 그대로입니다. 양수 각도는 시계 방향, 음수는 반시계 방향입니다. operations를 앞에서부터 차례대로 적용한 최종 board를 2차원 리스트로 반환하세요. 다음 연산은 바로 앞 연산의 결과에 적용하며, 회전 영역끼리 겹칠 수 있습니다.

- 1 ≤ board의 행 수, 열 수 ≤ 31이며, 모든 행의 길이는 같습니다.
- 1 ≤ board[r][c] ≤ 1,000,000
- 0 ≤ len(operations) ≤ 20
- 각 연산의 top, left는 0부터 시작하는 행·열 번호입니다. size는 1 이상의 홀수입니다.
- 0 ≤ top, 0 ≤ left, top + size ≤ 행 수, left + size ≤ 열 수이므로 지정한 정사각형은 항상 board 안에 들어갑니다.
- -360 ≤ d ≤ 360이며 d는 45의 배수입니다.
- 각 45도 단계에서는 그 단계 직전의 값을 동시에 옮깁니다. 서로 다른 연산은 입력 순서대로 적용합니다.
- operations가 비어 있으면 원래 배열을 반환합니다. size가 1이거나 d가 0, 360, -360인 연산은 배열을 바꾸지 않습니다.

```python
def solution(board, operations):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]],[[0,1,3,45]]]` | `[[1,7,2,3,5],[6,12,8,4,10],[11,13,14,9,15]]` |
| `[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]],[[0,0,3,45],[1,2,3,-45]]]` | `[[6,1,2,4,5],[11,7,9,10,15],[12,13,3,14,20],[16,17,8,18,19]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 한 연산 안의 이동은 동시에 일어나지만, 여러 연산은 순서대로 일어납니다. 겹친 영역이 있으므로 모든 각도를 하나로 합치거나 매번 최초 board에서 값을 읽으면 안 됩니다.
2. 부분 배열 안에서는 좌표가 0부터 size - 1까지라고 생각하세요. 그 안의 (r, c)는 전체 패널의 (top + r, left + c)입니다. 부분 배열을 복사해 원래 값을 보관한 뒤, 이 좌표 변환을 거쳐 결과에 쓰면 됩니다.
3. result = [row[:] for row in board]로 시작합니다. 각 연산을 (d // 45) % 8번 반복하고, 매 45도 직전에 before = [row[left:left + size] for row in result[top:top + size]]를 만드세요. before에서 네 줄의 값을 읽고 result[top + r][left + c]에만 쓴 다음 다음 단계로 넘어갑니다.

기본 문제의 한 단계 회전 함수를 부분 배열에 적용하는 구현·시뮬레이션입니다. 두 종류의 순서를 구별해야 합니다. 한 45도 단계 안에서 네 줄을 옮기는 것은 동시 갱신이므로, 쓰기 전에 해당 부분 배열의 값을 before에 모두 복사합니다. 반면 operations에 담긴 여러 연산은 앞 연산을 끝낸 뒤 그 결과에 다음 연산을 적용합니다. 특히 겹친 영역은 연산 순서에 따라 값이 달라지므로 각도를 무조건 합칠 수 없습니다.

전체 결과 배열 result를 행마다 복사하고, 각 연산의 steps = (d // 45) % 8을 구합니다. 매 단계 before를 현재 result의 부분 배열에서 새로 만듭니다. mid = size // 2라고 하면 로컬 좌표 (i, i) → (i, mid), (i, mid) → (i, size - 1 - i), (i, size - 1 - i) → (mid, size - 1 - i), (mid, i) → (i, i)를 사용합니다.

before는 로컬 좌표로 읽고, result에 쓸 때만 행에 top, 열에 left를 더합니다. 예를 들어 result[top + i][left + mid] = before[i][i]입니다. 오프셋은 한 번만 더해야 합니다. before의 각 행은 슬라이스로 새로 만들었으므로 result에 써도 before는 바뀌지 않습니다. 네 줄에 해당하는 칸만 쓰므로 그 밖의 값은 자동으로 보존됩니다.

전체 행·열 수를 R, C, 각 연산의 크기를 s_j, 정규화한 회전 횟수를 k_j라 하면 시간 복잡도는 O(RC + Σ(k_j × s_j²)), 공간 복잡도는 O(RC + max(s_j²))입니다. 연산이 없으면 시간·공간 모두 초기 결과 복사에 드는 O(RC)입니다.

```python
def solution(board, operations):
  result = [row[:] for row in board]

  for top, left, size, d in operations:
    mid = size // 2
    steps = (d // 45) % 8

    for _ in range(steps):
      before = [row[left:left + size]
                for row in result[top:top + size]]
      for i in range(size):
        result[top + i][left + mid] = before[i][i]
        result[top + i][left + size - 1 - i] = before[i][mid]
        result[top + mid][left + size - 1 - i] = before[i][size - 1 - i]
        result[top + i][left + i] = before[mid][i]

  return result
```

</details>

## 가리고 설명할 질문

자식 후보를 만들 때 부모를 바꾸지 않는 가장 단순한 방법은?

<details><summary>답 확인</summary>

부모의 행까지 복사한 새 배열을 만들고 그 배열만 수정합니다. 형제 후보마다 다시 복사합니다.

</details>
