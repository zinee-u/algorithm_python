# 8주차 · 힙과 작업의 도착 시각

도착 순서와 처리 우선순위를 다른 자료구조로 관리합니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-11-30 · 기본 기술

### 요청 도착 순서 정리

jobs의 [요청시각,소요시간]에 입력 순서의 번호를 붙여 [요청시각,소요시간,번호] 목록을 반환하세요. 요청시각,소요시간,번호 순으로 오름차순입니다.

- 1 ≤ 작업 수 ≤ 1000
- 요청시각 0~10000, 소요시간 1~1000

```python
def solution(jobs):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[2,1],[0,4],[0,2]]]` | `[[0,2,2],[0,4,1],[2,1,0]]` |
| `[[[0,1],[0,1]]]` | `[[0,1,0],[0,1,1]]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. enumerate(jobs)의 번호를 보관하세요.
2. 리스트는 첫 값부터 차례대로 비교됩니다.

아직 도착하지 않은 작업을 보관하는 목록은 요청 시각이 먼저입니다. 실행할 작업의 우선순위와 다릅니다.

```python
def solution(jobs):
  pending = []
  for job_id, job in enumerate(jobs):
    request,load = job
    pending.append([request,load,job_id])
  return sorted(pending)
```

</details>

## 2026-12-01 · 기본 기술

### 처리 시간이 짧은 순서

모든 작업이 이미 대기 중입니다. [요청시각,소요시간] 작업들을 소요시간,요청시각,입력 번호 순으로 처리했을 때 번호 목록을 반환하세요. heapq를 사용해 연습하세요.

- 1 ≤ 작업 수 ≤ 1000
- 요청시각 0~1000, 소요시간 1~1000

```python
def solution(jobs):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,4],[2,1],[1,1]]]` | `[2,1,0]` |
| `[[[0,2],[0,2]]]` | `[0,1]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. [load, request, job_id] 순서로 넣으세요.
2. 반환하는 것은 load가 아니라 job_id입니다.

힙에 넣는 첫 값이 최우선 비교 기준입니다. 꺼낼 때도 넣었던 필드 순서를 유지합니다.

```python
import heapq
def solution(jobs):
  heap = []
  for job_id, job in enumerate(jobs):
    request,load = job
    heapq.heappush(heap,[load,request,job_id])
  res = []
  while heap:
    load,request,job_id = heapq.heappop(heap)
    res.append(job_id)
  return res
```

</details>

## 2026-12-02 · 기본 기술

### 현재 고를 수 있는 작업

아직 처리하지 않은 작업 중 요청 시각이 now 이하인 것만 후보입니다. 소요시간,요청시각,입력 번호 순서로 가장 앞선 작업 번호를 반환하세요. 후보가 없으면 -1입니다.

- 0 ≤ 작업 수 ≤ 1000
- 요청 시각과 now는 0 이상
- 소요시간은 양수

```python
def solution(jobs, now):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,9],[10,1],[2,4]],3]` | `2` |
| `[[[5,1]],4]` | `-1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 먼저 request <= now로 걸러냅니다.
2. 후보의 정렬 키는 처리 순서를 사용합니다.

짧은 작업이어도 미래에 요청되면 후보에 넣지 않습니다.

```python
def solution(jobs, now):
  ready = []
  for job_id,job in enumerate(jobs):
    request,load = job
    if request <= now:
      ready.append([load,request,job_id])
  if not ready:
    return -1
  ready.sort()
  return ready[0][2]
```

</details>

## 2026-12-03 · 기본 기술

### 주말 · 도착 목록과 대기 힙 합치기

한 번에 작업 하나를 중단 없이 처리합니다. 작업이 끝날 때 도착한 작업 중 소요시간,요청시각,입력 번호 순으로 고릅니다. 대기 작업이 없으면 다음 요청까지 쉽니다. 요청부터 종료까지 시간의 평균을 내림해 반환하세요.

- 1 ≤ 작업 수 ≤ 1000
- 요청 시각 0~100000, 소요시간 1~1000

```python
def solution(jobs):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,3],[1,9],[2,6]]]` | `9` |
| `[[[5,2],[20,1]]]` | `1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 힙이 비면 now를 다음 요청까지 올립니다.
2. 현재 now까지 도착한 작업을 모두 힙에 넣은 뒤 하나 꺼냅니다.

pending은 도착 순서, heap은 처리 우선순위입니다. 누적 시간에는 방금 힙에서 꺼낸 요청 시각을 사용합니다.

```python
import heapq
def solution(jobs):
  pending = sorted([[s,load,i] for i,(s,load) in enumerate(jobs)])
  heap = []
  now,total,idx = 0,0,0
  while idx < len(jobs) or heap:
    if not heap:
      now = max(now,pending[idx][0])
    while idx < len(jobs) and pending[idx][0] <= now:
      request,load,job_id = pending[idx]
      heapq.heappush(heap,[load,request,job_id])
      idx += 1
    load,request,job_id = heapq.heappop(heap)
    now += load
    total += now-request
  return total//len(jobs)
```

</details>

## 2026-12-04 · 가리고 다시 풀기

### 현재 고를 수 있는 작업

아직 처리하지 않은 작업 중 요청 시각이 now 이하인 것만 후보입니다. 소요시간,요청시각,입력 번호 순서로 가장 앞선 작업 번호를 반환하세요. 후보가 없으면 -1입니다.

- 0 ≤ 작업 수 ≤ 1000
- 요청 시각과 now는 0 이상
- 소요시간은 양수

```python
def solution(jobs, now):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,9],[10,1],[2,4]],3]` | `2` |
| `[[[5,1]],4]` | `-1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 먼저 request <= now로 걸러냅니다.
2. 후보의 정렬 키는 처리 순서를 사용합니다.

짧은 작업이어도 미래에 요청되면 후보에 넣지 않습니다.

```python
def solution(jobs, now):
  ready = []
  for job_id,job in enumerate(jobs):
    request,load = job
    if request <= now:
      ready.append([load,request,job_id])
  if not ready:
    return -1
  ready.sort()
  return ready[0][2]
```

</details>

## 2026-12-05 · 토요일 응용

### 주말 · 도착 목록과 대기 힙 합치기

한 번에 작업 하나를 중단 없이 처리합니다. 작업이 끝날 때 도착한 작업 중 소요시간,요청시각,입력 번호 순으로 고릅니다. 대기 작업이 없으면 다음 요청까지 쉽니다. 요청부터 종료까지 시간의 평균을 내림해 반환하세요.

- 1 ≤ 작업 수 ≤ 1000
- 요청 시각 0~100000, 소요시간 1~1000

```python
def solution(jobs):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,3],[1,9],[2,6]]]` | `9` |
| `[[[5,2],[20,1]]]` | `1` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 힙이 비면 now를 다음 요청까지 올립니다.
2. 현재 now까지 도착한 작업을 모두 힙에 넣은 뒤 하나 꺼냅니다.

pending은 도착 순서, heap은 처리 우선순위입니다. 누적 시간에는 방금 힙에서 꺼낸 요청 시각을 사용합니다.

```python
import heapq
def solution(jobs):
  pending = sorted([[s,load,i] for i,(s,load) in enumerate(jobs)])
  heap = []
  now,total,idx = 0,0,0
  while idx < len(jobs) or heap:
    if not heap:
      now = max(now,pending[idx][0])
    while idx < len(jobs) and pending[idx][0] <= now:
      request,load,job_id = pending[idx]
      heapq.heappush(heap,[load,request,job_id])
      idx += 1
    load,request,job_id = heapq.heappop(heap)
    now += load
    total += now-request
  return total//len(jobs)
```

</details>

## 2026-12-06 · 일요일 전이

### 처리 시간이 짧은 순서

모든 작업이 이미 대기 중입니다. [요청시각,소요시간] 작업들을 소요시간,요청시각,입력 번호 순으로 처리했을 때 번호 목록을 반환하세요. heapq를 사용해 연습하세요.

- 1 ≤ 작업 수 ≤ 1000
- 요청시각 0~1000, 소요시간 1~1000

```python
def solution(jobs):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[[0,4],[2,1],[1,1]]]` | `[2,1,0]` |
| `[[[0,2],[0,2]]]` | `[0,1]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. [load, request, job_id] 순서로 넣으세요.
2. 반환하는 것은 load가 아니라 job_id입니다.

힙에 넣는 첫 값이 최우선 비교 기준입니다. 꺼낼 때도 넣었던 필드 순서를 유지합니다.

```python
import heapq
def solution(jobs):
  heap = []
  for job_id, job in enumerate(jobs):
    request,load = job
    heapq.heappush(heap,[load,request,job_id])
  res = []
  while heap:
    load,request,job_id = heapq.heappop(heap)
    res.append(job_id)
  return res
```

</details>

## 가리고 설명할 질문

pending과 heap의 첫 정렬 기준은 각각 무엇인가요?

<details><summary>답 확인</summary>

pending은 요청 시각, 이미 도착한 작업의 heap은 소요시간입니다. 미래 작업은 아직 후보가 아닙니다.

</details>
