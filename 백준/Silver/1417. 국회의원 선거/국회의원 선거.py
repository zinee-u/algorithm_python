N = int(input())

# nums[i] = [후보번호, 표수]
nums = []
for i in range(1, N+1):
    v = int(input())
    nums.append([i, v])

ans = 0

# 계속 반복하며 1번 후보가 단독 1위가 될 때까지
while True:
    if N == 1:
        ans = 0
        break
    dasom = nums[0][1]
    # 1번 후보 외의 후보 중 가장 표 많은 값 구하기
    max_comp = max(nums[i][1] for i in range(1, N))
    # 만약 이미 1번 후보가 단독 1위라면 종료
    if dasom > max_comp:
        break

    # 가장 표 많은 경쟁자(인덱스) 찾기
    for idx in range(1, N):
        if nums[idx][1] == max_comp:
            nums[idx][1] -= 1  # 경쟁자로부터 1표 빼앗기
            nums[0][1] += 1    # 1번 후보에게 1표 추가
            ans += 1           # 연산 횟수 늘리기
            break

print(ans)