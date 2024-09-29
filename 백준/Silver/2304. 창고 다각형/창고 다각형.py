N = int(input())

info = [0] * 1001
max_height = 0
max_height_index = 0
end_index = 0
for _ in range(N):
    l, h = map(int, input().split())
    info[l] = h
    if max_height < h:
        max_height = h
        max_height_index = l
    end_index = max(end_index, l)

stack = []
area = 0
for i in range(0, max_height_index + 1):
    if not stack:
        stack.append(info[i])
    else:
        if stack[-1] < info[i]:
            stack.pop()
            stack.append(info[i])
    area += stack[-1]

stack = []
for j in range(end_index, max_height_index, -1):
    if not stack:
        stack.append(info[j])
    else:
        if stack[-1] < info[j]:
            stack.pop()
            stack.append(info[j])
    area += stack[-1]

print(area)