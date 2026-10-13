# 13주차 · 모든 경우 대신 필요한 정보

입력 제한을 보고 순열 대신 개수·경계 정보를 남깁니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2027-01-04 · 기본 기술

### 곱이 큰 양수 묶음

합이 s인 자연수 n개의 곱이 최대가 되도록 오름차순 목록을 반환하세요. 만들 수 없으면 [-1]입니다.

- 1 ≤ n ≤ 10000
- 1 ≤ s ≤ 100000000

```python
def solution(n, s):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[2,9]` | `[4,5]` |
| `[3,2]` | `[-1]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. s < n이면 모두 1 이상으로 만들 수 없습니다.
2. 몫과 나머지로 작은 값과 큰 값의 개수를 구합니다.

두 값의 차이가 2 이상이면 큰 쪽에서 1을 작은 쪽으로 옮겨 곱을 키울 수 있습니다. 가능한 한 고르게 나눕니다.

```python
def solution(n, s):
  if s < n: return [-1]
  value,extra = divmod(s,n)
  return [value]*(n-extra)+[value+1]*extra
```

</details>

## 2027-01-05 · 기본 기술

### 연결 순서 비교

모든 수를 문자열 조각으로 한 번씩 사용해 가장 큰 수를 만들어 문자열로 반환하세요. 결과가 0만 있으면 "0"입니다.

- 1 ≤ 길이 ≤ 10000
- 0 ≤ 각 수 ≤ 1000

```python
def solution(numbers):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[3,30,34,5,9]]` | `"9534330"` |
| `[[0,0]]` | `"0"` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 3과 30은 330과 303을 비교합니다.
2. cmp_to_key로 두 항목 비교 함수를 정렬에 넘길 수 있습니다.

두 조각 a,b는 a+b와 b+a를 비교해 순서를 정합니다. 길이나 첫 숫자만으로는 충분하지 않습니다.

```python
from functools import cmp_to_key
def solution(numbers):
  def compare(a,b):
    if a+b > b+a: return -1
    if a+b < b+a: return 1
    return 0
  parts = sorted([str(n) for n in numbers],key=cmp_to_key(compare))
  return '0' if parts[0] == '0' else ''.join(parts)
```

</details>

## 2027-01-06 · 기본 기술

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

## 2027-01-07 · 기본 기술

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

## 2027-01-08 · 가리고 다시 풀기

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

## 2027-01-09 · 토요일 응용

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

## 2027-01-10 · 일요일 전이

### 곱이 큰 양수 묶음

합이 s인 자연수 n개의 곱이 최대가 되도록 오름차순 목록을 반환하세요. 만들 수 없으면 [-1]입니다.

- 1 ≤ n ≤ 10000
- 1 ≤ s ≤ 100000000

```python
def solution(n, s):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[2,9]` | `[4,5]` |
| `[3,2]` | `[-1]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. s < n이면 모두 1 이상으로 만들 수 없습니다.
2. 몫과 나머지로 작은 값과 큰 값의 개수를 구합니다.

두 값의 차이가 2 이상이면 큰 쪽에서 1을 작은 쪽으로 옮겨 곱을 키울 수 있습니다. 가능한 한 고르게 나눕니다.

```python
def solution(n, s):
  if s < n: return [-1]
  value,extra = divmod(s,n)
  return [value]*(n-extra)+[value+1]*extra
```

</details>

## 가리고 설명할 질문

문자열을 재배치할 때 큰 연속 구간은 어떤 모양인가요?

<details><summary>답 확인</summary>

한 조각의 접미사+같은 문자만인 조각들+다른 조각의 접두사입니다. 내부 최대도 비교하며 한 조각을 두 번 쓰지 않습니다.

</details>
