import math

def solution(r1, r2):
    answer = 0
    # r1 ** 1 <= x ** 2 + y ** 2 <= r2 ** 2
    # x = sqrt(r2**2 - y**2)
    # y = sqrt(r2**2 - x**2)
    for i in range(1, r2+1):
        if i > r1:
            x = 0
        else:
            x = math.sqrt(r1**2 - i**2)
        y = math.sqrt(r2**2 - i**2)
        # 범위 내 정수인 x, y 개수
        answer += math.floor(y) - math.ceil(x) + 1
    return answer*4