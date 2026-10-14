# 2026-10-14 Python 30분 학습

학습 기록일: 2026-10-14 (Asia/Seoul)

학습 점수: 30 XP (자가 학습 기록이며 공식 시험 점수가 아닙니다.)

## 자리 번호와 카드 번호

- 오늘 검사: 4/4
- 힌트: 0회 · 해설 확인: 없음
- 학습 시간: 11분 4초

### 회고

for pos, idx in enumerate(path):

### 시도한 코드

````python
def solution(brightness, path):
  sum_card = 0
  for i, val in enumerate(path):
    sum_card += brightness[val] * (i+1)
  return sum_card

````

## 원본을 지키는 수정본

- 오늘 검사: 4/4
- 힌트: 0회 · 해설 확인: 있음
- 학습 시간: 19분 16초

### 회고

board r/c 중 changes에 해당하는 r/c의 값을 바꾸는 방법

### 시도한 코드

````python
def solution(board, changes):
  nxt = [row[:] for row in board]
  for r, c, val in changes:
    nxt[r][c] = val
  return nxt
````

