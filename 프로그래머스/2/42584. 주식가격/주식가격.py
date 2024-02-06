def solution(prices):
    len_prices = len(prices)
    answer = [0 for _ in range(len_prices)]
    # answer[-1] = 0
    st = []
    j = 0
    for i in range(len_prices):
        while st and (prices[st[-1]]> prices[i]):
            j = st.pop()
            answer[j] = i - j
        
        st.append(i)
        # print(st)
    
    while st:
        j = st.pop()
        answer[j] = len_prices - 1 - j
    
    return answer