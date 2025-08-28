import sys

N, R = map(int, input().split(' '))
# print(N, R)
N = 1 << N
# print(N, R)
arr = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
# print(arr)

def printArr(arr):
    for row in arr:
        print(*row)
    

def upDownStep(si, sj, size):
    tmp = [[0] * size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            tmp[r][c] = arr[si+r][sj+c]

    for r in range(size):
        for c in range(size):
            arr[si+r][sj+c] = tmp[size-r-1][c]


def upDown(size):
    for si in range(0, N, size):
        for sj in range(0, N, size):
            upDownStep(si, sj, size)


def mirroringStep(si, sj, size):
    tmp = [[0] * size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            tmp[r][c] = arr[si+r][sj+c]    
    for r in range(size):
        for c in range(size):
            arr[si+r][sj+c] = tmp[r][size-c-1]


def mirroring(size):
    for si in range(0, N, size):
        for sj in range(0, N, size):
            mirroringStep(si, sj, size)


def cwStep(si, sj, size):
    tmp = [[0] * size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            tmp[r][c] = arr[si+r][sj+c]    
    for r in range(size):
        for c in range(size):
            arr[si+r][sj+c] = tmp[size-c-1][r]


def cw(size):
    for si in range(0, N, size):
        for sj in range(0, N, size):
            cwStep(si, sj, size)


def ccwStep(si, sj, size):
    tmp = [[0] * size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            tmp[r][c] = arr[si+r][sj+c]
    for r in range(size):
        for c in range(size):
            arr[si+r][sj+c] = tmp[c][size-r-1]


def ccw(size):
    for si in range(0, N, size):
        for sj in range(0, N, size):
            ccwStep(si, sj, size)


def splitUpdown(l):
    upDown(N)
    upDown(l)

def splitMirror(l):
    mirroring(N)
    mirroring(l)

def splitCw(l):
    cw(N)
    ccw(l)

def splitCcw(l):
    ccw(N)
    cw(l)


for _ in range(R):
    k, l = map(int, input().split(' '))
    # print(k, l)
    l = 1<<l
    if k == 1:
        upDown(l)
    elif k == 2:
        mirroring(l)
    elif k == 3:
        cw(l)
    elif k == 4:
        ccw(l)
    elif k == 5:
        splitUpdown(l)
    elif k == 6:
        splitMirror(l)
    elif k == 7:
        splitCw(l)
    elif k == 8:
        splitCcw(l)
        

printArr(arr)