N = int(input())
cmds = list(map(str, input().rstrip()))
# print(cmds)
cnt = 0
ans = str("No")
for cmd in cmds:
    if cmd == 'O':
        cnt += 1
    if N%2==0:
        if cnt >= (N//2):
            ans = str("Yes")
            break
    else:
        if cnt >= (N//2+1):
            ans = str("Yes")
            break

print(ans)