import sys

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(n)]
ret = 1

path = set()
path.add(arr[0][0])


def dfs(r, c):
	global ret, arr
	for d in range(4):
		prev = arr[r][c]
		nr, nc = r + dr[d], c + dc[d]
		if (-1 < nr < n) and (-1 < nc < m):
			cur = arr[nr][nc]
			if(prev != cur):
				if cur not in path:
					path.add(cur)
					dfs(nr, nc)
					path.remove(cur)
				else:
					ret = max(len(path), ret)

	return ret


print(dfs(0, 0))
