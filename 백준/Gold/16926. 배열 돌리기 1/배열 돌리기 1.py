import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

layers = min(N, M) // 2

for s in range(layers):
    top, left = s, s
    bottom, right = N - 1 - s, M - 1 - s

    ring = []
    # 위쪽 행 (left -> right)
    for c in range(left, right + 1):
        ring.append(A[top][c])
    # 오른쪽 열 (top+1 -> bottom-1)
    for r in range(top + 1, bottom):
        ring.append(A[r][right])
    # 아래쪽 행 (right -> left)
    for c in range(right, left - 1, -1):
        ring.append(A[bottom][c])
    # 왼쪽 열 (bottom-1 -> top+1)
    for r in range(bottom - 1, top, -1):
        ring.append(A[r][left])

    L = len(ring)
    k = R % L
    if k:
        ring = ring[k:] + ring[:k]   # 둘레를 한 번에 R칸 회전(반시계)

    # 회전된 ring을 다시 채워 넣기 (같은 경로로)
    idx = 0
    for c in range(left, right + 1):
        A[top][c] = ring[idx]; idx += 1
    for r in range(top + 1, bottom):
        A[r][right] = ring[idx]; idx += 1
    for c in range(right, left - 1, -1):
        A[bottom][c] = ring[idx]; idx += 1
    for r in range(bottom - 1, top, -1):
        A[r][left] = ring[idx]; idx += 1

for row in A:
    print(*row)