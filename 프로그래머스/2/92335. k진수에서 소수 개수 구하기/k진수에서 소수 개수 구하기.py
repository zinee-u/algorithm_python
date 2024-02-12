from collections import deque

def isPrime(e):
    if e == 2 or e == 3:
        return True
    if e % 2 == 0 or e < 2:
        return False
    for i in range(3, int(e ** 0.5) + 1, 2):
        if e % i == 0:
            return False
    return True

def k_nums(n, k):
    q = deque()
    res = 0
    lst_num = []
    st = []
    while n > 0:
        q.append(n % k)
        n //= k
    # print(q)
    i = 0
    while q:
        num = q.popleft()
        if num == 0:
            lst_num.append(res)
            i = 0
            res = 0
            # print(lst_num)
        else:
            num *= 10**(i)
            res += num
            i += 1
    lst_num.append(res)
    for e in lst_num:
        if e != 0:
            st.append(e)
    return st

def solution(n, k):
    answer = 0
    lst_num = k_nums(n, k)

    for e in lst_num:
        if e == "":
            continue
        if isPrime(e):
            answer += 1
            
    return answer