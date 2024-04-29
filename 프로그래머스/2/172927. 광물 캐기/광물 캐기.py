from collections import Counter

def solution(picks, minerals):
    answer = []
    p = {"diamond": [1,5,25], "iron": [1,1,5], "stone": [1,1,1]}
    
    
    def dfs(picks, minerals, cnt):
        if sum(picks) == 0 or not minerals:
            answer.append(cnt)
            return answer
        
        cnt_mine = Counter(minerals[:5])
        
        tools = []
        for i, n_tool in enumerate(picks):
            if n_tool:
                tools.append(i)
        
        for i in tools:
            tmp = 0
            for m, cost in cnt_mine.items():
                tmp = tmp + cost*p[m][i]
            picks[i] -= 1
            dfs(picks, minerals[5:], tmp + cnt)
            picks[i] += 1
        
    # main
    dfs(picks, minerals, 0)

    return min(answer)