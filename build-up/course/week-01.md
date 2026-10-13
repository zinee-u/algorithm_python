# 1주차 · 변수의 역할과 복사

값·번호·위치를 섞거나 부분 합에서 반환하던 습관을 고칩니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-10-14 · 기본 기술

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

## 2026-10-15 · 기본 기술

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

## 2026-10-16 · 가리고 다시 풀기

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

## 2026-10-17 · 토요일 응용

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

## 2026-10-18 · 일요일 전이

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

## 가리고 설명할 질문

position과 card는 무엇이 다른가요?

<details><summary>답 확인</summary>

position은 배치 순서(1부터), card는 brightness를 읽을 원래 카드 번호입니다.

</details>
