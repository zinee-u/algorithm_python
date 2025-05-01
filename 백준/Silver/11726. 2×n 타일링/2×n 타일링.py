n = int(input())
arr = [0 for _ in range(n+2)]
arr[1], arr[2] = 1, 2

for i in range(3, n+1):
    arr[i] = (arr[i-2] + arr[i-1])%10007
        

print(arr[n]%10007)
