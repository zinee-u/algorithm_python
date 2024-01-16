cnt_zero = 0

def cnt_one(s):
    global cnt_zero
    cnt1 = 0
    for e in s:
        if e != '0':
            cnt1 += 1
        else:
            cnt_zero += 1
    return cnt1

def make_bin(n):
    tmp, res_bin = str(), str()
    while n != 0:
        if n % 2 == 0: tmp += '0'
        else: tmp += '1' 
        n //= 2
    
    for i in range(len(tmp) -1, -1, -1):
        res_bin += tmp[i]
        
    
    return [res_bin]
        
    
def solution(s):
    answer, cnt_bin = [], 1
    tmp_bin = str()
    
    tmp_one = cnt_one(s)
    
    while tmp_one > 1 :
        tmp_bin = make_bin(tmp_one)
        # print(tmp_bin[0])
        tmp_one = cnt_one(str(tmp_bin[0]))
        print(tmp_one)
        cnt_bin += 1
        
        
    
    answer = [cnt_bin, cnt_zero]
    return answer