nums = [list(map(int, input().split(' '))) for _ in range(5)]
# print(nums)

callNums = [list(map(int, input().split(' '))) for _ in range(5)]
# print(callNums)
cnt_num = 0

def check_bingo(nums):
    cnt_bingo = 0
    
    # 행 체크
    for row in nums:
        if sum(row) == 0:
            cnt_bingo += 1
    
    # 열 체크
    for col in range(5):
        if sum(nums[row][col] for row in range(5)) == 0:
            cnt_bingo += 1

    # 대각선 체크
    if sum(nums[i][i] for i in range(5)) == 0:
        cnt_bingo += 1
    if sum(nums[i][4-i] for i in range(5)) == 0:
        cnt_bingo += 1

    return cnt_bingo

# 호출 숫자 처리
for i in range(5):
    for j in range(5):
        cnt_num += 1
        num = callNums[i][j]
        
        # 호출된 숫자를 0으로 표시
        for x in range(5):
            for y in range(5):
                if nums[x][y] == num:
                    nums[x][y] = 0
        
        # 빙고 확인
        if check_bingo(nums) >= 3:
            print(cnt_num)
            exit()