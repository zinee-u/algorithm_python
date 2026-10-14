def solution(board, changes):
  nxt = [row[:] for row in board]
  for r, c, val in changes:
    nxt[r][c] = val
  return nxt
