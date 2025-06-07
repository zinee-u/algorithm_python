arr = list(map(str, input().rstrip()))
# print(arr)
target = ['M','O','B','I','S']
st = []

for i, s in enumerate(target):
  for c in arr:
    if (c == target[i]) and (c not in st):
      st.append(c)

# print(st, len(st))

if len(st) == 5:
  print("YES")
else:
  print("NO")