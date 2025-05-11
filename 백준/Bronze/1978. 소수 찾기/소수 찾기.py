N = int(input())
arr = list(map(int, input().split()))
# print(N)
# print(arr)

cnt = N

for i in range(N):
    num = arr[i]
    j = 2
    if(num < 2):
        cnt -= 1
    while(j*j < num+1):
        if(num % j == 0):
            cnt-=1
            break
        j += 1

print(cnt)