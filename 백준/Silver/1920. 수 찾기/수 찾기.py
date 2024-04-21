n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()
# print(arr1, arr2)
ans = []


for i in range(m):
  s, e = 0, n-1
  target = arr2[i]
  flag = True
  #print("target=",target)
  while (s<=e):
    mid = (e+s)//2
    # print("arr1[mid]=",arr1[mid])
    if arr1[mid] == target:
      print(1)
      flag = False
      break
    elif arr1[mid] < target:
      s = mid + 1
    else:
      e = mid - 1
  if flag:
    print(0)