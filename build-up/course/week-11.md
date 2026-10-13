# 11주차 · 투 포인터와 개수

구간 길이와 종류 수를 구분하고 축소 시점을 결정합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-12-21 · 기본 기술

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

## 2026-12-22 · 기본 기술

### 목표 이상인 가장 짧은 구간

양수 배열에서 합이 target 이상인 연속 구간의 최소 길이를 반환하세요. 없으면 0입니다.

- 1 ≤ 길이 ≤ 100000
- 모든 값은 1 이상
- target은 양수

```python
def solution(values, target):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[2,3,1,2,4,3],7]` | `2` |
| `[[1,1],5]` | `0` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. while total >= target에서 축소합니다.
2. 축소하기 전에 현재 길이를 기록하세요.

양수이므로 오른쪽을 늘리면 합이 커지고 왼쪽을 줄이면 합이 작아집니다. 조건을 만족하는 동안 답을 기록하고 줄입니다.

```python
def solution(values, target):
  left,total = 0,0
  answer = len(values)+1
  for right,value in enumerate(values):
    total += value
    while total >= target:
      answer = min(answer,right-left+1)
      total -= values[left]
      left += 1
  return 0 if answer == len(values)+1 else answer
```

</details>

## 2026-12-23 · 기본 기술

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

## 2026-12-24 · 기본 기술

### 연속된 부분 수열의 합

정렬된 양의 정수 수열 sequence에서 합이 k인 연속 구간을 찾으세요. 여러 구간이 가능하면 원소 수가 가장 적은 구간을 고르고, 길이도 같으면 시작 인덱스가 가장 작은 구간을 고릅니다. solution(sequence, k)는 선택한 구간의 시작 인덱스와 끝 인덱스를 [시작, 끝]으로 반환합니다. 인덱스는 0부터 시작하며 양 끝의 원소를 모두 포함합니다.

- 5 ≤ len(sequence) ≤ 1,000,000
- 1 ≤ sequence[i] ≤ 1,000이며 수열은 비내림차순으로 주어집니다.
- 5 ≤ k ≤ 1,000,000,000
- 합이 k인 연속 구간이 하나 이상 존재하는 입력만 주어집니다.
- 길이가 가장 짧은 구간을 반환합니다. 길이가 같으면 시작 인덱스가 더 작은 구간을 반환합니다.
- 결과의 인덱스는 0부터 시작하며, 끝 인덱스도 구간에 포함됩니다.

```python
def solution(sequence, k):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[1,2,3,4,5],7]` | `[2,3]` |
| `[[1,1,1,2,3,4,5],5]` | `[6,6]` |
| `[[2,2,2,2,2],6]` | `[0,2]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 연속 구간을 고르므로 두 끝점 left, right로 후보를 표현할 수 있습니다. 모든 원소가 양수일 때 오른쪽 원소를 추가하면 합이 커지고, 왼쪽 원소를 빼면 합이 작아진다는 성질을 이용하세요.
2. right를 한 칸 옮길 때마다 total에 새 값을 더하세요. total > k인 동안 sequence[left]를 빼고 left를 전진합니다. 줄인 뒤 total == k이면 현재 구간을 정답 후보로 확인합니다. 매번 sum(sequence[left:right + 1])을 계산할 필요가 없습니다.
3. 구간 길이는 right - left + 1입니다. 지금까지의 최단 길이보다 엄격히 짧을 때만 [left, right]를 저장하면 같은 길이의 앞쪽 구간을 유지합니다. 각 포인터는 뒤로 돌아가지 않으므로 이중 반복문이어도 전체 이동 횟수는 O(n)입니다.

이 문제의 단서는 “연속 구간”, “양의 정수”, “최단 길이”입니다. left와 right가 가리키는 구간의 합을 total에 유지합니다. right를 늘리면 합이 커지고 left를 늘리면 합이 작아지므로, 합이 k보다 큰 구간은 왼쪽 원소를 제거하면서 줄일 수 있습니다. 수열의 정렬 여부보다 모든 값이 양수라는 성질이 이 합 조절 규칙의 핵심입니다. 음수가 섞인 수열에는 같은 규칙을 그대로 적용할 수 없습니다.

오른쪽에 value를 추가한 뒤 total > k인 동안 왼쪽 값을 빼고 left를 옮깁니다. total < k가 되면 더 줄여서 k를 만들 수 없으므로 다음 오른쪽 값을 기다립니다. total == k라면 양 끝을 포함한 길이 right - left + 1을 확인합니다. 현재 길이가 best_len보다 작을 때만 갱신하면, 같은 길이의 구간 중 먼저 발견한 앞쪽 구간을 보존합니다. 첫 번째 정답을 찾자마자 반환하면 뒤쪽의 더 짧은 구간을 놓칠 수 있습니다.

두 포인터는 모두 앞으로만 이동합니다. right는 n번, left는 최대 n번 움직이므로 for 안에 while이 있어도 전체 시간 복잡도는 O(n)입니다. 입력 외에 포인터, 합, 정답 구간만 저장하므로 추가 공간은 O(1)입니다. 이 문제는 0부터 시작하는 인덱스를 반환합니다.

```python
def solution(sequence, k):
  left = total = 0
  best_len = len(sequence) + 1
  answer = []

  for right, value in enumerate(sequence):
    total += value

    while total > k:
      total -= sequence[left]
      left += 1

    length = right - left + 1
    if total == k and length < best_len:
      best_len = length
      answer = [left, right]

  return answer
```

</details>

## 2026-12-25 · 가리고 다시 풀기

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

## 2026-12-26 · 토요일 응용

### 보석 쇼핑

보석이 일렬로 진열되어 있습니다. 전체 진열대에 등장하는 모든 보석 종류를 하나 이상 포함하면서, 구매할 보석 수가 가장 적은 연속 구간을 찾으세요. 최소 길이의 구간이 여러 개면 시작 진열대 번호가 가장 작은 구간을 고릅니다. solution(gems)는 [시작 번호, 끝 번호]를 반환합니다. 진열대 번호는 1부터 시작하고 양 끝을 모두 포함합니다.

- 1 ≤ len(gems) ≤ 100,000
- 각 보석 이름은 길이 1 이상 10 이하의 영문 대문자 문자열입니다.
- 선택한 연속 구간은 gems 전체에 등장하는 모든 종류를 적어도 하나씩 포함해야 합니다.
- 구간 길이가 같으면 시작 진열대 번호가 더 작은 구간을 반환합니다.
- 원래 진열 순서를 유지해야 합니다. 반환할 진열대 번호는 1부터 시작합니다.

```python
def solution(gems):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[["DIA","RUBY","RUBY","DIA","DIA","EMERALD","SAPPHIRE","DIA"]]` | `[3,7]` |
| `[["AA","AB","AC","AA","AC"]]` | `[1,3]` |
| `[["XYZ","XYZ","XYZ"]]` | `[1,1]` |
| `[["ZZZ","YYY","NNNN","YYY","BBB"]]` | `[1,5]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 합 대신 “현재 연속 구간이 모든 종류를 포함하는가”를 관리하세요. 전체 종류 수는 len(set(gems))입니다. gems를 정렬하면 원래 연속 구간이 사라지므로 정렬해서는 안 됩니다.
2. 현재 구간의 종류별 개수를 딕셔너리에 저장하세요. 오른쪽 보석을 넣을 때 개수를 늘리고, 왼쪽 보석을 뺄 때 개수를 줄입니다. 같은 종류가 여러 개 있을 수 있으므로 집합에서 바로 제거하면 남아 있는 보석을 놓칩니다. 개수가 0이 된 키만 삭제하세요.
3. 현재 종류 수가 전체 종류 수와 같을 동안, 먼저 현재 구간을 정답 후보로 기록하고 왼쪽을 한 칸 줄입니다. 더 짧은 구간에서만 정답을 갱신하고, 반환할 때는 left + 1, right + 1로 1부터 시작하는 번호를 만드세요.

기본 문제에서 구간 합을 유지했다면, 이번에는 종류별 개수를 유지합니다. need = len(set(gems))는 전체에서 필요한 종류 수이고, counts는 현재 구간 안의 종류별 개수입니다. 오른쪽에 보석을 하나 넣을 때 counts[gem] = counts.get(gem, 0) + 1로 갱신합니다. 딕셔너리에는 개수가 양수인 종류만 남겨 두므로 len(counts) == need이면 모든 종류를 포함한 구간입니다.

조건을 만족하는 동안 현재 길이를 먼저 확인하고, 왼쪽 보석 하나를 제거합니다. 아직 모든 종류가 남아 있다면 더 짧아진 구간도 후보이므로 while을 계속합니다. 어떤 종류의 마지막 보석을 제거했다면 그 키를 삭제하고 줄이기를 멈춥니다. 다음 오른쪽 보석을 추가하며 빠진 종류를 다시 찾습니다. 단순 집합만 쓰면 같은 보석이 구간에 두 개 있을 때 하나를 빼는 동작과 그 종류가 사라지는 동작을 구별할 수 없습니다.

기본 문제는 합이 너무 클 때 줄였지만, 이 문제는 모든 종류를 포함한 유효한 구간을 더 짧게 만들기 위해 줄입니다. 따라서 왼쪽 값을 빼기 전에 정답 후보를 확인해야 합니다. 길이가 엄격히 짧을 때만 갱신하면 같은 길이의 앞쪽 구간을 유지할 수 있습니다. Python 인덱스는 0부터지만 문제의 진열대 번호는 1부터이므로 정답에는 각 인덱스에 1을 더합니다.

오른쪽과 왼쪽 포인터는 각각 최대 n번 이동합니다. 딕셔너리 연산을 평균 O(1)로 보면 전체 시간 복잡도는 O(n), 추가 공간은 전체 보석 종류 수를 m이라 할 때 O(m)입니다.

```python
def solution(gems):
  need = len(set(gems))
  counts = {}
  left = 0
  best_len = len(gems) + 1
  answer = []

  for right, gem in enumerate(gems):
    counts[gem] = counts.get(gem, 0) + 1

    while len(counts) == need:
      length = right - left + 1
      if length < best_len:
        best_len = length
        answer = [left + 1, right + 1]

      first = gems[left]
      counts[first] -= 1
      if counts[first] == 0:
        del counts[first]
      left += 1

  return answer
```

</details>

## 2026-12-27 · 일요일 전이

### 목표 이상인 가장 짧은 구간

양수 배열에서 합이 target 이상인 연속 구간의 최소 길이를 반환하세요. 없으면 0입니다.

- 1 ≤ 길이 ≤ 100000
- 모든 값은 1 이상
- target은 양수

```python
def solution(values, target):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[2,3,1,2,4,3],7]` | `2` |
| `[[1,1],5]` | `0` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. while total >= target에서 축소합니다.
2. 축소하기 전에 현재 길이를 기록하세요.

양수이므로 오른쪽을 늘리면 합이 커지고 왼쪽을 줄이면 합이 작아집니다. 조건을 만족하는 동안 답을 기록하고 줄입니다.

```python
def solution(values, target):
  left,total = 0,0
  answer = len(values)+1
  for right,value in enumerate(values):
    total += value
    while total >= target:
      answer = min(answer,right-left+1)
      total -= values[left]
      left += 1
  return 0 if answer == len(values)+1 else answer
```

</details>

## 가리고 설명할 질문

모든 종류를 담은 구간에서 왼쪽을 줄이는 이유는?

<details><summary>답 확인</summary>

조건을 유지하는 동안 더 짧은 답을 찾기 위해서입니다. 빠지는 값의 개수가 0이 되면 종류가 사라집니다.

</details>
