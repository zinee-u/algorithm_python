import sys
import copy

N = int(input())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
K = int(input())

#1 keep
#2 mirroring (좌우 반전)
#3 up-down (상하 반전)

tmp = [[''] * N for _ in range(N)]

if K == 3:
    # 상하 반전: i행 -> (N-1-i)행
    for i in range(N):
        for j in range(N):
            tmp[i][j] = arr[N-1-i][j]
elif K == 2:
    # 좌우 반전: j열 -> (N-1-j)열
    for i in range(N):
        for j in range(N):
            tmp[i][j] = arr[i][N-1-j]
else:
    tmp = copy.deepcopy(arr)

for i in range(N):
    tmp_str = str()
    for j in range(N):
        # print(i, j)
        # print(tmp[i][j])
        tmp_str += tmp[i][j]
    print(tmp_str)
