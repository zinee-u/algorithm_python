def solution(n):
    answer = ''
    s_num = [1, 2, 4]
    
    # 10 41
    # 11 42
    # 12 44
    # 13 111 13//3 = 4, 13 % 3 = 1
    lst = []
    cnt = 0
    tmp_n = n
    while n:
        r = n % 3
        if r == 0:
            r = 4
            n -= 1
        lst.append(str(r))
        n //= 3
    for i in range(len(lst)-1, -1, -1):
        answer += lst[i]
    return answer