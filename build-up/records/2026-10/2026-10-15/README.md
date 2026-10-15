# 2026-10-15 Python 30분 학습

학습 기록일: 2026-10-15 (Asia/Seoul)

학습 점수: 30 XP (자가 학습 기록이며 공식 시험 점수가 아닙니다.)

## 자리 번호와 카드 번호

- 오늘 검사: 4/4
- 힌트: 0회 · 해설 확인: 없음
- 학습 시간: 4분 0초

### 회고

복습 완료 했습니다.

### 시도한 코드

````python
def solution(brightness, path):
  card = 0
  for i, val in enumerate(path, start=1):
    card+=brightness[val]*i
  return card

````

