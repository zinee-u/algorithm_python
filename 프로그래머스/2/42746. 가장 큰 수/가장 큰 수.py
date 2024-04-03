def solution(numbers):    
    s = list(map(str,numbers))
    # print(s)
    # 사전순
    # for c in s:
    #     print(c*3)
    c = sorted(s,key=lambda x: x*3,reverse=True)
    # print(c)
    return str(int("".join(c)))