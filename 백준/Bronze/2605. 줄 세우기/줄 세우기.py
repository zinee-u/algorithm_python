n = int(input())  # 학생 수
picks = list(map(int, input().split()))  # 학생들의 수백

line = []  # 학생들이 세워지는 순서

for i in range(n):
    # 번호에 따라 받은 좌석에 들여넣기
    line.insert(len(line) - picks[i], i + 1)

print(*line)  # 결과 출력