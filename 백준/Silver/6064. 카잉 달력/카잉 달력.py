T = int(input())
# print(T)

def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

for _ in range(T):
    M, N, x, y = map(int, input().split())
    nLcm = lcm(M, N)
    answer = -1
    k = x
    while k <= nLcm:
        if (k - 1) % N + 1 == y:
            answer = k
            break
        k += M
    print(answer)