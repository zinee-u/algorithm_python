def solution(brightness, path):
  sum_card = 0
  for i, val in enumerate(path):
    sum_card += brightness[val] * (i+1)
  return sum_card

