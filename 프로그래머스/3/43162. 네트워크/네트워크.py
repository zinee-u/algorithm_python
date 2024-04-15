
def solution(n, computers):
    answer = 0
    
    visited = [0] * n

    def dfs(computers, visited, now):
        visited[now] = 1
        for v in range(len(computers)):
            if visited[v] == 0 and computers[now][v] == 1:
                dfs(computers, visited, v)
    
    while False in visited:
        for i in range(n):
            if visited[i] == 0:
                dfs(computers, visited, i)
                answer += 1
            
    return answer