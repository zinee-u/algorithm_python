import math

a, b, h = map(int, input().split())

if a == b:
  print(-1)
elif a == 0:
  print((b**2 + h**2) * math.pi)
else:
  if a > b:
    a, b = b, a
  x = b*h / (b-a) # a : b = (x - h) : x => b(x-h) = ax => bx-bh = ax => (b-a)x = bh
  r_big = (x**2 + b**2)
  r_small = ((x-h)**2 + a**2)
  print((r_big - r_small)*math.pi)