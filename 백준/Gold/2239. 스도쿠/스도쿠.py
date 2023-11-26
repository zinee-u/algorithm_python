import sys
arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if arr[i][j] == '0':
            zero.append([i, j])


def chkNums(R, C, num):
    j = 0
    for i in range(9):
        if arr[i][C] == num:
            return False

        if arr[R][i] == num:
            return False

        if arr[j+(R//3)*3][(i%3)+(C//3)*3] == num:
            return False
        if i % 3 == 2: j += 1
    return True

def dfs(idx):
    if idx == len(zero):
        answer = ''
        for i in range(9):
            for j in range(9):
                answer += arr[i][j]
            print(answer)
            answer = ''
        exit(0)
    r, c = zero[idx]

    for i in range(1, 10):
        if chkNums(r, c, str(i)):
            arr[r][c] = str(i)
            dfs(idx + 1)
            arr[r][c] = '0'

dfs(0)