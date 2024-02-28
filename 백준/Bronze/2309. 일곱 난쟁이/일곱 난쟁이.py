lst_num = []
for _ in range(9):
    lst_num.append(int(input()))
lst_num.sort()

visited = [0 for _ in range(9)]


def dfs(dep, lst_answer):
    if len(lst_answer) == 2:
        # print(lst_answer)
        if sum(lst_num) - sum(lst_answer) == 100:
            for ans in lst_num:
                if ans not in lst_answer:
                    print(ans)
            exit()
            return lst_answer
    else:
        for i in range(dep+1, 9):
            if visited[i] == 0:
                visited[i] = 1
                dfs(i, lst_answer+[lst_num[i]])
                visited[i] = 0

dfs(-1, [])