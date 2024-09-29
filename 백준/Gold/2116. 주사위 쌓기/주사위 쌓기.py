def opposite_face(face):
  return {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}[face]

def max_visible_sum(dice):
  N = len(dice)
  max_sum = 0
  
  for bottom in range(6):
    total_sum = 0
    current_bottom = bottom
    
    for i in range(N):
      current_top = opposite_face(current_bottom)
      visible_faces = [dice[i][j] for j in range(6) if j != current_bottom and j != current_top]
      total_sum += max(visible_faces)
      
      if i < N - 1:
        current_bottom = dice[i + 1].index(dice[i][current_top])
    
    max_sum = max(max_sum, total_sum)
  
  return max_sum


n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
print(max_visible_sum(dice))