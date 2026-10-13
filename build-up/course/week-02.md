# 2주차 · 개수와 연속 구간

set으로 개수를 잃던 문제를 count로 해결합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-10-19 · 기본 기술

### 처음 나온 값도 세기

정수 목록에서 각 값이 몇 번 나오는지 세어 [값, 개수] 목록을 값 오름차순으로 반환하세요.

- 0 ≤ 길이 ≤ 1000
- -100 ≤ 값 ≤ 100

```python
def solution(items):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[3,1,3,2,1]]` | `[[1,2],[2,1],[3,2]]` |
| `[[]]` | `[]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. set은 중복 횟수를 기억하지 못합니다.
2. 출력 순서만 sorted(count)로 정하세요.

count.get(value, 0)은 기존 개수, 없으면 0입니다. 여기에 1을 더해 다시 저장합니다.

```python
def solution(items):
  count = {}
  for value in items:
    count[value] = count.get(value, 0) + 1
  return [[value, count[value]] for value in sorted(count)]
```

</details>

## 2026-10-20 · 기본 기술

### 하나 빼도 종류가 남을까

items에서 removed 값을 한 번씩 제거합니다. 각 값은 그 시점에 반드시 남아 있습니다. 제거할 때마다 남은 서로 다른 값의 개수를 기록해 반환하세요.

- 1 ≤ items 길이 ≤ 1000
- 0 ≤ removed 길이 ≤ items 길이

```python
def solution(items, removed):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[["A","A","B"],["A","A","B"]]` | `[2,1,0]` |
| `[[1,2,3],[]]` | `[]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. items=[A,A,B]에서 A 하나를 빼도 A는 남습니다.
2. count[value]를 줄인 다음 0인지 확인하세요.

개수가 0이 되는 순간에만 그 종류를 딕셔너리에서 지웁니다.

```python
def solution(items, removed):
  count = {}
  for value in items:
    count[value] = count.get(value, 0) + 1
  res = []
  for value in removed:
    count[value] -= 1
    if count[value] == 0:
      del count[value]
    res.append(len(count))
  return res
```

</details>

## 2026-10-21 · 기본 기술

### 연속 구간과 전체 개수 구분

문자열을 같은 문자가 연속한 구간으로 나누어 [문자, 길이] 목록을 반환하세요. 떨어져 있는 같은 문자는 다른 구간입니다.

- 0 ≤ 길이 ≤ 10000
- A,B,C만 등장합니다.

```python
def solution(text):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `["AABBCAA"]` | `[["A",2],["B",2],["C",1],["A",2]]` |
| `[""]` | `[]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. ABAA는 A 3개 한 구간이 아닙니다.
2. 새 문자면 새 항목, 같은 문자면 마지막 길이를 늘립니다.

전체 빈도가 아니라 바로 앞 문자와 같은지를 확인합니다.

```python
def solution(text):
  res = []
  for ch in text:
    if res and res[-1][0] == ch:
      res[-1][1] += 1
    else:
      res.append([ch, 1])
  return res
```

</details>

## 2026-10-22 · 기본 기술

### 숫자 카드의 공통 재고

숫자 문자열 x,y에서 같은 숫자를 하나씩 짝지어 가장 큰 수를 만드세요. 짝이 없으면 "-1", 0만 있으면 "0", 나머지는 내림차순 문자열을 반환합니다.

- 1 ≤ 각 문자열 길이 ≤ 100000
- 문자는 0~9뿐입니다.

```python
def solution(x, y):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `["5525","1255"]` | `"552"` |
| `["100","200"]` | `"0"` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 10칸짜리 개수 배열 두 개면 충분합니다.
2. 문자열 전체를 정수로 바꾸지 않아도 0만 있는지 알 수 있습니다.

쓸 수 있는 숫자 d의 개수는 두 문자열 개수의 최솟값입니다. 큰 숫자부터 이어 붙입니다.

```python
def solution(x, y):
  a = [0] * 10
  b = [0] * 10
  for ch in x:
    a[int(ch)] += 1
  for ch in y:
    b[int(ch)] += 1
  parts = []
  for d in range(9, -1, -1):
    parts.append(str(d) * min(a[d], b[d]))
  result = ''.join(parts)
  if not result:
    return '-1'
  if result[0] == '0':
    return '0'
  return result
```

</details>

## 2026-10-23 · 가리고 다시 풀기

### 하나 빼도 종류가 남을까

items에서 removed 값을 한 번씩 제거합니다. 각 값은 그 시점에 반드시 남아 있습니다. 제거할 때마다 남은 서로 다른 값의 개수를 기록해 반환하세요.

- 1 ≤ items 길이 ≤ 1000
- 0 ≤ removed 길이 ≤ items 길이

```python
def solution(items, removed):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[["A","A","B"],["A","A","B"]]` | `[2,1,0]` |
| `[[1,2,3],[]]` | `[]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. items=[A,A,B]에서 A 하나를 빼도 A는 남습니다.
2. count[value]를 줄인 다음 0인지 확인하세요.

개수가 0이 되는 순간에만 그 종류를 딕셔너리에서 지웁니다.

```python
def solution(items, removed):
  count = {}
  for value in items:
    count[value] = count.get(value, 0) + 1
  res = []
  for value in removed:
    count[value] -= 1
    if count[value] == 0:
      del count[value]
    res.append(len(count))
  return res
```

</details>

## 2026-10-24 · 토요일 응용

### 주말 · 하루 한 표만 세기

visits의 각 안쪽 리스트는 하루 방문한 부스 이름입니다. 같은 날 여러 번 방문해도 한 표입니다. minimum일 이상 방문한 부스 이름을 사전순으로 반환하세요.

- 0 ≤ 날짜 수 ≤ 100
- 하루 방문 수는 0~100
- 1 ≤ minimum ≤ 100

```python
def solution(visits, minimum):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[["A","A","B"],["B","C"],["A"]],2]` | `["A","B"]` |
| `[[["X","X"]],2]` | `[]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 각 day를 set(day)로 바꾼 뒤 반복하세요.
2. 부스별 횟수와 날짜 수를 혼동하지 마세요.

하루 안에서는 중복을 제거하고, 날짜 사이에서는 개수를 누적합니다.

```python
def solution(visits, minimum):
  count = {}
  for day in visits:
    for booth in set(day):
      count[booth] = count.get(booth, 0) + 1
  return sorted([booth for booth in count if count[booth] >= minimum])
```

</details>

## 2026-10-25 · 일요일 전이

### 숫자 카드의 공통 재고

숫자 문자열 x,y에서 같은 숫자를 하나씩 짝지어 가장 큰 수를 만드세요. 짝이 없으면 "-1", 0만 있으면 "0", 나머지는 내림차순 문자열을 반환합니다.

- 1 ≤ 각 문자열 길이 ≤ 100000
- 문자는 0~9뿐입니다.

```python
def solution(x, y):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `["5525","1255"]` | `"552"` |
| `["100","200"]` | `"0"` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 10칸짜리 개수 배열 두 개면 충분합니다.
2. 문자열 전체를 정수로 바꾸지 않아도 0만 있는지 알 수 있습니다.

쓸 수 있는 숫자 d의 개수는 두 문자열 개수의 최솟값입니다. 큰 숫자부터 이어 붙입니다.

```python
def solution(x, y):
  a = [0] * 10
  b = [0] * 10
  for ch in x:
    a[int(ch)] += 1
  for ch in y:
    b[int(ch)] += 1
  parts = []
  for d in range(9, -1, -1):
    parts.append(str(d) * min(a[d], b[d]))
  result = ''.join(parts)
  if not result:
    return '-1'
  if result[0] == '0':
    return '0'
  return result
```

</details>

## 가리고 설명할 질문

같은 값 하나를 빼면 종류 수도 바로 줄어드나요?

<details><summary>답 확인</summary>

아니요. 남은 개수가 0이 될 때만 그 종류를 지웁니다.

</details>
