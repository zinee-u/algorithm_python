import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

tree = dict()
is_child = [False] * (N + 1)
for a, l, r in arr:
    tree[a] = (l, r)
    if l != -1:
        is_child[l] = True
    if r != -1:
        is_child[r] = True

root = -1
for i in range(1, N + 1):
    if not is_child[i]:
        root = i
        break

level_min = dict()
level_max = dict()
cnt = 1

def inorder(node, level):
    global cnt
    if node == -1:
        return

    left, right = tree[node]
    inorder(left, level + 1)

    if level not in level_min:
        level_min[level] = cnt
    else:
        level_min[level] = min(level_min[level], cnt)

    if level not in level_max:
        level_max[level] = cnt
    else:
        level_max[level] = max(level_max[level], cnt)

    cnt += 1

    inorder(right, level + 1)

inorder(root, 1)

max_width = 0
res_level = 0
for level in level_min:
    width = level_max[level] - level_min[level] + 1
    if width > max_width:
        max_width = width
        res_level = level
    elif width == max_width:
        res_level = min(res_level, level)

print(res_level, max_width)