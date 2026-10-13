# 15주차 · 조건의 경계를 찾기

가능 여부가 한 방향으로 바뀌는 조건을 찾습니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2027-01-18 · 기본 기술

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

## 2027-01-19 · 기본 기술

### 정렬 배열의 등장 횟수

오름차순 values에서 target의 등장 횟수를 반환하세요. 선형으로 세지 않고 두 경계를 찾아 연습하세요.

- 0 ≤ 길이 ≤ 100000
- 값은 정수

```python
def solution(values, target):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[1,2,2,2,4],2]` | `3` |
| `[[1,3],2]` | `0` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. bisect_left와 bisect_right의 차이를 확인하세요.
2. target이 없어도 두 위치는 같아서 결과가 0입니다.

처음 target 이상인 위치와 처음 target 초과인 위치의 차이가 개수입니다.

```python
from bisect import bisect_left,bisect_right
def solution(values, target):
  return bisect_right(values,target)-bisect_left(values,target)
```

</details>

## 2027-01-20 · 기본 기술

### 가능한 최대 조각 길이

여러 줄을 같은 정수 길이로 잘라 need개 이상 만들려고 합니다. 남는 부분은 버립니다. 가능한 최대 길이를 반환하고 길이 1도 불가능하면 0입니다.

- 1 ≤ 줄 수 ≤ 10000
- 각 길이와 need는 1~1000000000

```python
def solution(lengths, need):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[8,5],3]` | `4` |
| `[[1],2]` | `0` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 후보 길이 mid에서 개수는 sum(length//mid)입니다.
2. mid가 0이 되지 않게 left=1로 시작하세요.

길이가 커질수록 만들 수 있는 개수는 줄어듭니다. 가능한 길이면 더 긴 쪽을 탐색합니다.

```python
def solution(lengths, need):
  left,right = 1,max(lengths)
  answer = 0
  while left <= right:
    mid = (left+right)//2
    count = sum(length//mid for length in lengths)
    if count >= need:
      answer = mid
      left = mid+1
    else: right = mid-1
  return answer
```

</details>

## 2027-01-21 · 기본 기술

### 주말 · 순서를 지키는 배송

weights 순서대로 짐을 배송합니다. 하루 총무게는 용량을 넘을 수 없고 짐을 나눌 수 없습니다. days일 이내에 끝낼 수 있는 최소 정수 용량을 반환하세요.

- 1 ≤ days ≤ 짐 수 ≤ 10000
- 각 무게는 1~10000

```python
def solution(weights, days):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[1,2,3,4,5],3]` | `6` |
| `[[3,2,2,4,1,4],3]` | `6` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 용량의 하한은 max(weights), 상한은 sum(weights)입니다.
2. 현재 날에 못 넣으면 다음 날을 시작합니다.

용량 하나를 정하면 앞에서부터 채우는 시뮬레이션으로 필요한 날짜를 구합니다. 용량이 커지면 필요한 날은 늘지 않습니다.

```python
def solution(weights, days):
  left,right = max(weights),sum(weights)
  while left < right:
    mid = (left+right)//2
    used,load = 1,0
    for weight in weights:
      if load+weight > mid:
        used += 1
        load = 0
      load += weight
    if used <= days: right = mid
    else: left = mid+1
  return left
```

</details>

## 2027-01-22 · 가리고 다시 풀기

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

## 2027-01-23 · 토요일 응용

### 주말 · 정해진 시간에 처리 가능한가

각 심사대는 times[i]분에 한 명씩 처리하고 동시에 일합니다. n명을 모두 처리할 수 있는 최소 시간을 반환하세요.

- 1 ≤ n ≤ 1000000000
- 1 ≤ 심사대 수 ≤ 10000
- 각 시간은 1~1000000000

```python
def solution(n, times):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[6,[7,10]]` | `28` |
| `[1,[3,5]]` | `3` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 상한은 가장 빠른 심사대가 모두 처리하는 시간입니다.
2. 가능하면 더 짧은 시간으로 범위를 줄이세요.

시간 t에 처리할 수 있는 사람 수는 sum(t//time)입니다. 답을 직접 구성하지 않고 가능 여부를 이분 탐색합니다.

```python
def solution(n, times):
  left,right = 0,min(times)*n
  while left < right:
    mid = (left+right)//2
    count = sum(mid//time for time in times)
    if count >= n: right = mid
    else: left = mid+1
  return left
```

</details>

## 2027-01-24 · 일요일 전이

### 주말 · 순서를 지키는 배송

weights 순서대로 짐을 배송합니다. 하루 총무게는 용량을 넘을 수 없고 짐을 나눌 수 없습니다. days일 이내에 끝낼 수 있는 최소 정수 용량을 반환하세요.

- 1 ≤ days ≤ 짐 수 ≤ 10000
- 각 무게는 1~10000

```python
def solution(weights, days):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[1,2,3,4,5],3]` | `6` |
| `[[3,2,2,4,1,4],3]` | `6` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 용량의 하한은 max(weights), 상한은 sum(weights)입니다.
2. 현재 날에 못 넣으면 다음 날을 시작합니다.

용량 하나를 정하면 앞에서부터 채우는 시뮬레이션으로 필요한 날짜를 구합니다. 용량이 커지면 필요한 날은 늘지 않습니다.

```python
def solution(weights, days):
  left,right = max(weights),sum(weights)
  while left < right:
    mid = (left+right)//2
    used,load = 1,0
    for weight in weights:
      if load+weight > mid:
        used += 1
        load = 0
      load += weight
    if used <= days: right = mid
    else: left = mid+1
  return left
```

</details>

## 가리고 설명할 질문

이분 탐색을 쓸 수 있는 가능 여부의 성질은?

<details><summary>답 확인</summary>

후보가 커질 때 가능→불가능 또는 불가능→가능처럼 한 번만 바뀌어야 합니다.

</details>
