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

