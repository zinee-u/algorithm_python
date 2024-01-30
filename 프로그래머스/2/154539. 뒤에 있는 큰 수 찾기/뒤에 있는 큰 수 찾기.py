def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    #O(nlogn?)
    i = 0
    st = []
    for i in range(len(numbers)):
        while(st and numbers[st[-1]] < numbers[i]):
            answer[st.pop()] = numbers[i]
        st.append(i)
            
    return answer