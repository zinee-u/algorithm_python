def solution(n, times):
    answer = 0
    t_s, t_e = 1, max(times) * n
    while t_e >= t_s:
        t_mid = (t_s+t_e)//2
        n_peo = 0
        for t in times:
            n_peo += t_mid // t
            if n_peo >= n:
                break
        
        if n_peo >= n:
            t_e = t_mid - 1
            answer = t_mid
        else:
            t_s = t_mid + 1
    
    return answer