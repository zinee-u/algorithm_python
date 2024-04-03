def solution(array, commands):
    answer = []
    lst_tmp = []
    for i, j, k in commands:
        lst_tmp = array[i-1:j]
        lst_tmp.sort()
        # print(lst_tmp)
        e = lst_tmp[k-1]
        answer.append(e)
        
    return answer