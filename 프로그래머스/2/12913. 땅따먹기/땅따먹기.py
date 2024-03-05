def solution(land):
    answer = 0
    if len(land) == 1:
        return max(land)
    
    for r in range(1, len(land)):
        for c in range(4):
            cur = land[r][c]
            for i in range(4):
                if c == i: continue
                land[r][c] = max(land[r][c], cur + land[r-1][i])

    answer = max(map(max, land))
    
    return answer