import sys

N, M, R = map(int, sys.stdin.readline().split(' '))
arr = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
# print(arr)
# K = int(input())

def copyArr(arr):
    tmp = [[0] * len(arr[0]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            tmp[i][j] = arr[i][j]
    return tmp

def upDown(arr):
    n, m = len(arr), len(arr[0])
    tmp = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            tmp[n-r-1][c] = arr[r][c]
    return tmp

def mirroring(arr):
    n, m = len(arr), len(arr[0])
    tmp = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            tmp[r][m-c-1] = arr[r][c]
    return tmp

def cw(arr):
    n, m = len(arr), len(arr[0])
    tmp = [[0] * n for _ in range(m)]
    for c in range(m):
        for r in range(n):
            tmp[c][n-r-1] = arr[r][c]
    return tmp

def ccw(arr):
    n, m = len(arr), len(arr[0])
    tmp = [[0] * n for _ in range(m)]
    for c in range(m):
        for r in range(n):
            tmp[m-1-c][r] = arr[r][c]
    return tmp

def halfCw(arr):
    n, m = len(arr), len(arr[0])
    tmp = [[0] * m for _ in range(n)]
    hr, hc = n//2, m//2
    sr1, sc1 = 0, 0
    sr2, sc2 = sr1, sc1+hc
    sr3, sc3 = sr1+hr, sc1+hc
    sr4, sc4 = sr1+hr, sc1
    #4->1
    for r in range(sr4, sr4+hr):
        for c in range(sc4, sc4+hc):
            tmp[r-hr][c] = arr[r][c]
    #1->2
    for r in range(sr1, sr1+hr):
        for c in range(sc1, sc1+hc):
            tmp[r][c+hc] = arr[r][c]
    #2->3
    for r in range(sr2,sr2+hr):
        for c in range(sc2,sc2+hc):
            tmp[r+hr][c] = arr[r][c]
    #3->4
    for r in range(sr3, sr3+hr):
        for c in range(sc3, sc3+hc):
            tmp[r][c-hc] = arr[r][c]
    return tmp

def halfCcw(arr):
    n = len(arr)
    m = len(arr[0])
    tmp = [[0] * m for _ in range(n)]
    hr, hc = n//2, m//2
    sr1, sc1 = 0, 0
    sr2, sc2 = sr1, sc1+hc
    sr3, sc3 = sr1+hr, sc1+hc
    sr4, sc4 = sr1+hr, sc1
    #1->4
    for r in range(sr4, sr4+hr):
        for c in range(sc4, sc4+hc):
            tmp[r][c] = arr[r-hr][c]
    #2->1
    for r in range(sr1, sr1+hr):
        for c in range(sc1, sc1+hc):
            tmp[r][c] = arr[r][c+hc]
    
    #3->2
    for r in range(sr2,sr2+hr):
        for c in range(sc2,sc2+hc):
            tmp[r][c] = arr[r+hr][c]
    
    #4->3
    for r in range(sr3, sr3+hr):
        for c in range(sc3, sc3+hc):
            tmp[r][c] = arr[r][c-hc]
    return tmp


def printArr(arr):
    for row in arr:
        print(*row)

cmd = map(int, input().split(' '))

for op in cmd:
    if op == 1:
        ret = upDown(arr)
    elif op == 2:
        ret = mirroring(arr)
    elif op == 3:
        ret = cw(arr)
    elif op == 4:
        ret = ccw(arr)
    elif op == 5:
        ret = halfCw(arr)
    elif op == 6:
        ret = halfCcw(arr)
    arr = copyArr(ret)

printArr(arr)