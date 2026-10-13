# 18주차 · 구간과 경계 복습 주

비슷한 문자열 문제에서도 허용 연산을 먼저 읽습니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2027-02-08 · 기본 기술

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

## 2027-02-09 · 기본 기술

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

## 2027-02-10 · 기본 기술

### 문자열의 시작·끝·내부 요약

text에서 ch로 시작하는 연속 길이, ch로 끝나는 연속 길이, 내부 ch의 최대 연속 길이를 [시작,끝,최대]로 반환하세요.

- 0 ≤ 길이 ≤ 100000
- text와 ch는 A,B,C 사용
- ch는 한 글자

```python
def solution(text, ch):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `["AABAAA","A"]` | `[2,3,3]` |
| `["AAAA","A"]` | `[4,4,4]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 시작과 끝에서 각각 ch가 아닌 문자를 만나면 멈춥니다.
2. 내부 최대는 현재 연속 길이를 늘리거나 0으로 초기화합니다.

다른 문자열과 이어질 수 있는 부분은 시작과 끝입니다. 내부의 긴 구간은 별도 후보로 남깁니다.

```python
def solution(text, ch):
  prefix = 0
  while prefix < len(text) and text[prefix] == ch: prefix += 1
  suffix = 0
  while suffix < len(text) and text[len(text)-1-suffix] == ch: suffix += 1
  current,best = 0,0
  for value in text:
    current = current+1 if value == ch else 0
    best = max(best,current)
  return [prefix,suffix,best]
```

</details>

## 2027-02-11 · 기본 기술

### 처음으로 기준 이상인 위치

오름차순 values에서 target 이상인 첫 위치를 반환하세요. 없으면 len(values)입니다. 위치는 0부터입니다.

- 0 ≤ 길이 ≤ 100000
- 중복 값이 있을 수 있습니다.

```python
def solution(values, target):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[1,2,2,4],2]` | `1` |
| `[[1,2],3]` | `2` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. right의 초기값은 len(values)입니다.
2. left < right 동안 검사하세요.

가능한 답의 구간을 [left,right)로 유지합니다. 값이 target 이상이면 mid도 후보이므로 right=mid입니다.

```python
def solution(values, target):
  left,right = 0,len(values)
  while left < right:
    mid = (left+right)//2
    if values[mid] >= target: right = mid
    else: left = mid+1
  return left
```

</details>

## 2027-02-12 · 가리고 다시 풀기

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

## 2027-02-13 · 토요일 응용

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

## 2027-02-14 · 일요일 전이

### 시험 복원 3 · 문자열 배치의 최대 연속 길이

문자 A, B, C로만 이루어진 문자열들이 중첩 리스트 strings로 주어집니다. 이 복원안에서는 strings[i][0]이 i번째 문자열입니다. 모든 문자열을 각각 정확히 한 번씩 사용하여 원하는 순서로 이어 붙이세요. 각 문자열 내부의 문자 순서는 바꿀 수 없습니다. 이어 붙인 결과에서 같은 문자 하나가 연속해서 나타나는 구간의 최대 길이를 구합니다. 가능한 배치 전체에서 얻을 수 있는 가장 큰 길이를 정수로 반환하세요. 같은 내용의 문자열도 서로 다른 입력 원소라면 각각 한 번씩 사용합니다. 완성된 문자열이나 순열 목록을 반환하지 않습니다.

- 입력은 리스트 안에 리스트가 있는 형태입니다. 연습용으로 각 내부 리스트의 길이는 1이고, 그 원소는 비어 있지 않은 문자열로 정합니다.
- 모든 문자열은 문자 A, B, C만 포함합니다. 내부 문자를 정렬하거나 문자열을 뒤집을 수 없습니다.
- 연습용 범위: 1 ≤ len(strings), 모든 문자열 길이의 합 ≤ 2,000,000.
- 기억한 숫자 2,000,000이 문자열 개수, 개별 길이, 전체 길이 중 무엇의 상한인지는 미확인입니다. 위 범위는 연습용 선택입니다.
- 문자열 재배치 후보는 모든 순열이지만 실제로 순열을 전부 생성할 필요는 없습니다.
- 기억한 시험 환경은 10초·2GB이며 실제 시험 데이터나 제한을 그대로 재현한 것은 아닙니다.

```python
def solution(strings):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[["ABC"],["AAC"],["BBC"]]]` | `2` |
| `[[["BAA"],["AAA"],["AAC"]]]` | `7` |
| `[[["AABAA"]]]` | `2` |
| `[[["AABB"],["ABAC"],["CCBA"],["AAAA"]]]` | `7` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 연속 구간이 한 문자열 안에서 끝나는 경우와 여러 문자열 경계를 넘는 경우를 나누어 보세요. 경계를 넘을 때 중간에 놓인 문자열에는 다른 문자가 있을 수 있을까요?
2. 문자 c에 대해 c로만 된 문자열의 길이 합, 혼합 문자열의 앞쪽 c 길이와 뒤쪽 c 길이, 내부 최대 연속 길이를 기록하세요. 뒤쪽 구간 + 순수 문자열 전부 + 앞쪽 구간을 만들 수 있습니다.
3. 양 끝에 같은 입력 원소를 두 번 쓸 수 없습니다. 앞쪽·뒤쪽 길이 각각 상위 두 개를 문자열 번호와 함께 저장하면, 서로 다른 번호인 조합을 상수 개만 비교할 수 있습니다. 한쪽 끝이 없는 경우도 포함하세요.

각 문자열 내부의 최대 연속 길이를 먼저 기록합니다. 특정 문자 c의 연속 구간이 문자열 경계를 넘으면, 왼쪽 끝 문자열의 접미 구간과 오른쪽 끝 문자열의 접두 구간 사이에는 c로만 이루어진 문자열들만 올 수 있습니다. c로만 된 문자열은 전부 모아 가운데 넣는 것이 유리합니다. 나머지 혼합 문자열에서 접미 길이와 접두 길이를 고르되 서로 다른 문자열 번호를 사용합니다. 한쪽 후보를 고정했을 때 금지되는 번호는 하나뿐이므로 반대쪽의 상위 두 후보면 충분합니다. 각 방향의 상위 두 개와 길이 0인 가상 후보를 비교하면 양쪽·한쪽·순수 문자열만 사용하는 경우를 모두 처리할 수 있습니다. 남은 문자열은 이 구간 바깥에 배치하여 모든 입력을 정확히 한 번씩 사용할 수 있습니다. 같은 혼합 문자열의 양 끝을 동시에 사용하는 오류와 순수 문자열 중복 합산에 주의하세요. 전체 문자 수 L에 대해 시간 O(L), 입력 외 추가 공간 O(1)입니다. 투 포인터로 한 배치의 연속 길이를 구하는 것만으로는 최적의 배치까지 선택할 수 없습니다. 사용자 예시 AABB, ABAC, CCBA, AAAA는 CCBA | AAAA | AABB | ABAC 순서에서 A가 1+4+2=7개 이어집니다. 입력 순서대로 붙이면 최댓값은 5이므로 순서 선택이 중요합니다. 투 포인터는 배치 하나가 정해졌을 때 연속 구간 길이를 O(L)에 셀 수 있지만, 모든 배치를 검사하면 문자열 수 T에 대해 O(T!·L)이 됩니다. 위 풀이는 배치의 최적값을 접두·접미 정보로 구하므로 순열 생성이 필요 없습니다. 문자열 내부 연속 구간을 세는 부분은 투 포인터로 바꾸어도 됩니다. 다만 실제 원문에서 순서 변경 대신 다른 연산을 요구했다면 풀이도 달라지므로, 현재 해설은 모든 문자열을 한 번씩 재배치한다는 복원 조건을 기준으로 합니다.

```python
def solution(strings):
  pure = {ch: 0 for ch in "ABC"}
  prefixes = {ch: [] for ch in "ABC"}
  suffixes = {ch: [] for ch in "ABC"}
  answer = 0

  def keep_two(records, length, index):
    records.append((length, index))
    records.sort(reverse=True)
    if len(records) > 2:
      records.pop()

  for index, row in enumerate(strings):
    text = row[0]
    run = 0
    previous = None
    for ch in text:
      run = run + 1 if ch == previous else 1
      previous = ch
      answer = max(answer, run)

    size = len(text)
    prefix = 1
    while prefix < size and text[prefix] == text[0]:
      prefix += 1

    if prefix == size:
      pure[text[0]] += size
      continue

    suffix = 1
    while suffix < size and text[size - 1 - suffix] == text[-1]:
      suffix += 1

    keep_two(prefixes[text[0]], prefix, index)
    keep_two(suffixes[text[-1]], suffix, index)

  for ch in "ABC":
    # 양 끝 중 한쪽을 사용하지 않는 경우도 비교합니다.
    for left_length, left_id in suffixes[ch] + [(0, -1)]:
      for right_length, right_id in prefixes[ch] + [(0, -2)]:
        if left_id == right_id:
          continue
        answer = max(answer, left_length + pure[ch] + right_length)

  return answer
```

</details>

## 가리고 설명할 질문

연속 구간과 임의 선택의 차이는?

<details><summary>답 확인</summary>

연속 구간은 원래 순서에서 중간을 건너뛸 수 없습니다. 문자열 조각 재배치는 순서를 선택하는 별도 최적화입니다.

</details>
