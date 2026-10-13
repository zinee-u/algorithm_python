# 12주차 · 스택과 연쇄 변화

마지막에 남은 것부터 다시 비교해야 하는 상황을 찾습니다.

각 날짜의 전체 학습은 30분입니다. 풀이를 끝내지 못해도 마지막 5분에 회고하고 마칩니다.

## 2026-12-28 · 기본 기술

### 괄호 짝 확인

소괄호만 있는 문자열이 올바르게 닫혔으면 True, 아니면 False를 반환하세요.

- 0 ≤ 길이 ≤ 100000

```python
def solution(text):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `["(()())"]` | `true` |
| `["())("]` | `false` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 여는 괄호는 append, 닫는 괄호는 pop입니다.
2. 스택이 비었는데 닫는 괄호가 나오면 실패입니다.

닫는 괄호는 가장 최근의 아직 닫히지 않은 여는 괄호를 없앱니다.

```python
def solution(text):
  stack = []
  for ch in text:
    if ch == '(':
      stack.append(ch)
    else:
      if not stack: return False
      stack.pop()
  return not stack
```

</details>

## 2026-12-29 · 기본 기술

### 이웃한 같은 문자 지우기

왼쪽부터 문자를 처리하며 마지막에 남은 문자와 새 문자가 같으면 둘을 지웁니다. 모두 처리한 뒤 남은 문자열을 반환하세요.

- 0 ≤ 길이 ≤ 100000
- 영문 대문자

```python
def solution(text):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `["ABBA"]` | `""` |
| `["ABCCBA"]` | `""` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. stack and stack[-1] == ch를 검사하세요.
2. 아니면 ch를 append합니다.

지운 뒤 새로 이웃한 문자도 처리되어야 하므로 남은 결과를 스택에 보관합니다.

```python
def solution(text):
  stack = []
  for ch in text:
    if stack and stack[-1] == ch: stack.pop()
    else: stack.append(ch)
  return ''.join(stack)
```

</details>

## 2026-12-30 · 기본 기술

### 연쇄 충돌 처리

양수는 오른쪽, 음수는 왼쪽으로 같은 속도로 움직입니다. 마주치는 둘 중 절댓값이 작은 것이 사라지고 같으면 둘 다 사라집니다. 격자 규칙 없이 서로 마주쳐 지나가려 하면 충돌합니다. 최종 남은 값을 순서대로 반환하세요.

- 0 ≤ 길이 ≤ 100000
- 0은 입력되지 않음
- 절댓값 ≤ 10000

```python
def solution(values):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[5,10,-5]]` | `[5,10]` |
| `[[8,-8]]` | `[]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 충돌은 if 한 번이 아니라 while로 이어집니다.
2. 합쳐서 더하는 시험 복원 규칙과 구분하세요.

스택 끝의 양수와 새 음수만 충돌합니다. 앞의 양수가 없어지면 새 음수를 더 앞과 다시 비교합니다.

```python
def solution(values):
  stack = []
  for value in values:
    alive = True
    while alive and stack and stack[-1] > 0 and value < 0:
      if stack[-1] < -value: stack.pop()
      elif stack[-1] == -value:
        stack.pop()
        alive = False
      else: alive = False
    if alive: stack.append(value)
  return stack
```

</details>

## 2026-12-31 · 기본 기술

### 동시 이동 한 번만 계산

양수는 오른쪽, 음수는 왼쪽으로 한 칸 동시에 이동합니다. 0은 빈칸입니다. 이동 후 같은 칸에 온 값은 더합니다. 배열 밖으로 나간 것은 버립니다. 한 번 이동한 배열을 반환하세요.

- 1 ≤ 길이 ≤ 10000
- 값은 -100~100

```python
def solution(values):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[3,0,-2]]` | `[0,1,0]` |
| `[[3,-2]]` | `[-2,3]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. nxt는 0으로 시작합니다.
2. 음수의 목적지는 i-1, 양수는 i+1입니다.

원본에서 방향을 읽고 새 배열의 목적지에 +=로 더합니다. 서로 엇갈리면 같은 칸에 도착하지 않으므로 합쳐지지 않습니다.

```python
def solution(values):
  nxt = [0]*len(values)
  for i,value in enumerate(values):
    if value == 0: continue
    dest = i+1 if value > 0 else i-1
    if 0 <= dest < len(values): nxt[dest] += value
  return nxt
```

</details>

## 2027-01-01 · 가리고 다시 풀기

### 이웃한 같은 문자 지우기

왼쪽부터 문자를 처리하며 마지막에 남은 문자와 새 문자가 같으면 둘을 지웁니다. 모두 처리한 뒤 남은 문자열을 반환하세요.

- 0 ≤ 길이 ≤ 100000
- 영문 대문자

```python
def solution(text):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `["ABBA"]` | `""` |
| `["ABCCBA"]` | `""` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. stack and stack[-1] == ch를 검사하세요.
2. 아니면 ch를 append합니다.

지운 뒤 새로 이웃한 문자도 처리되어야 하므로 남은 결과를 스택에 보관합니다.

```python
def solution(text):
  stack = []
  for ch in text:
    if stack and stack[-1] == ch: stack.pop()
    else: stack.append(ch)
  return ''.join(stack)
```

</details>

## 2027-01-02 · 토요일 응용

### 시험 복원 2 · 숫자의 이동과 합치기

일렬로 놓인 N개 칸의 상태 numbers가 주어집니다. 매 시간 모든 양수는 오른쪽으로 한 칸, 모든 음수는 왼쪽으로 한 칸 동시에 이동합니다. 이동을 마친 뒤 같은 칸에 도착한 숫자들은 합쳐져 합을 값으로 갖는 숫자 하나가 됩니다. 합이 0이면 사라지고, 0이 아니면 다음 시간부터 합의 부호에 따라 이동합니다. 이동 중 서로 엇갈려 지나간 숫자는 합쳐지지 않습니다. 경계를 넘어간 숫자는 사라집니다. 모든 숫자가 사라질 때까지 진행한 뒤 [왼쪽으로 나간 숫자의 개수, 오른쪽으로 나간 숫자의 개수]를 반환하세요. 합쳐진 숫자가 탈출하면 크기나 원래 숫자 수와 관계없이 하나로 셉니다. 처음부터 모두 0이면 [0, 0]입니다.

- 연습용 입력 범위: 1 ≤ len(numbers) ≤ 100,000, -10^9 ≤ numbers[i] ≤ 10^9. 원래 시험의 입력 상한은 확인되지 않았습니다.
- 모든 숫자는 동시에 이동하며, 이동 후 같은 칸에서만 합쳐집니다. 이 규칙은 공유 대화에서 사용자가 정정·확인했습니다.
- 0은 움직이는 숫자가 아니라 빈 칸입니다. 합이 0인 충돌은 탈출 개수에 포함하지 않습니다.
- 반환 순서 [왼쪽, 오른쪽]과 개수 기준은 공유 대화의 제출 코드 해석을 채택한 복원 조건입니다.
- 기억한 시험 제한은 10초·2GB입니다. 시간 단위로 전체 배열을 반복 갱신하면 큰 입력에서 느릴 수 있습니다.

```python
def solution(numbers):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[3,0,-1]]` | `[0,1]` |
| `[[1,0,-1]]` | `[0,0]` |
| `[[1,-1]]` | `[1,1]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. [1, -1]은 서로 지나가지만 [1, 0, -1]은 만나서 사라집니다. 시작 위치 차이가 홀수인 두 숫자가 같은 시간에 같은 칸에 있을 수 있을까요?
2. 매 시간 위치의 홀짝이 뒤집히므로 처음 인덱스의 홀짝이 같은 숫자끼리만 합쳐집니다. 짝수 위치와 홀수 위치를 나누어 처리하세요.
3. 각 홀짝 그룹을 왼쪽부터 스택에 넣습니다. 스택 끝이 양수이고 새 값이 음수일 때만 만납니다. 두 값을 더하고, 합이 음수라면 앞의 양수와 계속 합칩니다. 0이면 사라집니다.

t번 이동한 숫자의 위치 홀짝은 시작 인덱스+t의 홀짝입니다. 합쳐진 숫자도 이 성질을 유지하므로 짝수·홀수 시작 그룹은 서로 독립입니다. 같은 그룹에서는 오른쪽으로 가는 양수와 그 오른쪽에서 왼쪽으로 오는 음수만 만납니다. 스택에 아직 처리할 숫자를 넣고, 새 음수와 스택 끝의 양수를 합칩니다. 합이 음수면 앞의 양수와 연쇄적으로 합치고, 양수면 스택에 남기며, 0이면 사라집니다. 이웃한 서로 마주 보는 숫자는 두 위치 사이에서 만나므로 경계 탈출보다 먼저 충돌합니다. 같은 방향 숫자는 속도가 같아 따라잡지 않습니다. 남은 음수와 양수의 개수가 각각 왼쪽·오른쪽 탈출 개수입니다. 각 값이 스택에 최대 한 번 들어가고 한 번 나오므로 시간 O(N), 공간 O(N)입니다. 절댓값이 큰 숫자를 그대로 남기는 충돌 규칙과 달리 여기서는 반드시 두 값을 더합니다.

```python
def solution(numbers):
  left = right = 0
  for parity in range(2):
    stack = []
    for i in range(parity, len(numbers), 2):
      value = numbers[i]
      if value == 0:
        continue
      while stack and stack[-1] > 0 and value < 0:
        value += stack.pop()
      if value != 0:
        stack.append(value)
    for value in stack:
      if value < 0:
        left += 1
      else:
        right += 1
  return [left, right]
```

</details>

## 2027-01-03 · 일요일 전이

### 연쇄 충돌 처리

양수는 오른쪽, 음수는 왼쪽으로 같은 속도로 움직입니다. 마주치는 둘 중 절댓값이 작은 것이 사라지고 같으면 둘 다 사라집니다. 격자 규칙 없이 서로 마주쳐 지나가려 하면 충돌합니다. 최종 남은 값을 순서대로 반환하세요.

- 0 ≤ 길이 ≤ 100000
- 0은 입력되지 않음
- 절댓값 ≤ 10000

```python
def solution(values):
  pass
```

| 함수 인자 (순서대로) | 결과 |
|---|---|
| `[[5,10,-5]]` | `[5,10]` |
| `[[8,-8]]` | `[]` |

<details><summary>막혔을 때만: 힌트와 해설</summary>

1. 충돌은 if 한 번이 아니라 while로 이어집니다.
2. 합쳐서 더하는 시험 복원 규칙과 구분하세요.

스택 끝의 양수와 새 음수만 충돌합니다. 앞의 양수가 없어지면 새 음수를 더 앞과 다시 비교합니다.

```python
def solution(values):
  stack = []
  for value in values:
    alive = True
    while alive and stack and stack[-1] > 0 and value < 0:
      if stack[-1] < -value: stack.pop()
      elif stack[-1] == -value:
        stack.pop()
        alive = False
      else: alive = False
    if alive: stack.append(value)
  return stack
```

</details>

## 가리고 설명할 질문

스택 충돌 처리가 if 한 번이 아니라 while인 이유는?

<details><summary>답 확인</summary>

마지막 원소가 사라지면 더 앞 원소와도 새 충돌이 생길 수 있기 때문입니다.

</details>
