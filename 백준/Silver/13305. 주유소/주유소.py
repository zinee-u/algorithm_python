N = int(input())

dist = list(map(int, input().split(' ')))
cost = list(map(int, input().split(' ')))

ans = 0
cur_cost = cost[0]

for i in range(N-1):
    if cost[i] < cur_cost:
        cur_cost = cost[i]
        
    
    ans += cur_cost*dist[i]

print(ans)

