lst = list(map(int, input().split(' ')))

lst.sort()
# c > b > a; 1 <= a, b ,c <= 100
a, b, c = lst

# 삼각형 특) a + b > c
# 막대 길이 감소 가능
if a + b <= c:
    c = a + b - 1

print(a + b + c)