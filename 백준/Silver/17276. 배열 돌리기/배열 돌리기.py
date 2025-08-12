T = int(input())

def cw45(N):
    global arr
    tmp = [[0] * N for _ in range(N)]
    half = (N-1)//2

    for i in range(N):
        for j in range(N):
            tmp[i][j] = arr[i][j]
    
    for i in range(N):
        arr[i][i] = tmp[half][i]

    for i in range(N):
        arr[i][half] = tmp[i][i]
    
    for i in range(N):
        arr[i][N-i-1] = tmp[i][half]
    
    for i in range(N):
        arr[half][i] = tmp[N-i-1][i]

for _ in range(T):
    N, D = map(int, input().split(' '))
    arr = []
    
    for _ in range(N):
        arr.append(list(map(int, input().split(' '))))
    
    D = ((D+360)%360)
    cnt = D//45
    for _ in range(cnt):
        cw45(N)
    
    for row in arr:
        print(*row)