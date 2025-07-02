def solution(n, lost, reserve):
    answer = 0
    
    reserve2 = sorted([r for r in reserve if r not in lost])
    lost2 = sorted([l for l in lost if l not in reserve])
    # print(lost2)
    # print(reserve2)
    
    # reserve.sort()
    cnt_no = 0
    cnt_lst = len(lost2)
    cnt_rsv = len(reserve2)
    
    
    for i in range(cnt_lst-1,-1,-1):
        for idx in range(len(reserve2)-1, -1, -1):
            if reserve2[idx] == lost2[i]-1:
                lost2[i] = 0
                reserve2[idx] = -1
                break
            elif reserve2[idx] == lost2[i]+1:
                lost2[i] = 0
                reserve2[idx] = -1
                break
    
    print(lost2)
    print(reserve2)
    cnt_no = sum(i//i for i in lost2 if i > 0)
    # print(cnt_no)

    answer = n - cnt_no
    return answer