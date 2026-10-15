def solution(brightness, path):
  card = 0
  for i, val in enumerate(path, start=1):
    card+=brightness[val]*i
  return card

