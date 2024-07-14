import sys, heapq
input = sys.stdin.readline

V,E = map(int,input().split()) # 노드와 간선
k=int(input()) # 시작 노드

# 그래프 그리기
graph=[[] for _ in range(V+1)]
for _ in range(E):
    e,v,w=map(int,input().split())
    graph[e].append([w,v]) # [가중치, 노드]

def dijkstra(start):
    INF=1e9
    visited=[INF]*(V+1) # 무한으로 초기화
    visited[start]=0 # 시작 노드 가중치는 0
    q=[[0,start]] # [가중치, 노드]
    while q:
        cost,node=heapq.heappop(q)
        if cost > visited[node]: # 현재 이동하고자 하는 경로의 비용이 이전 비용보다 크다면 가지않음
            continue
        for k,u in graph[node]:
            if visited[u] > visited[node]+k: # 이동 비용이 작다면
                visited[u] = visited[node]+k # 그렇게 이동
                heapq.heappush(q,[visited[u], u]) # 우큐에 삽입
    return visited[1:] # 0번째 인덱스 제외

for ans in dijkstra(k):
    print(ans if ans!=1e9 else 'INF')