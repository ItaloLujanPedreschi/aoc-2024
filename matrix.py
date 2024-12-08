from pos import Pos

class Matrix:
  def __init__(self, matrix=[]):
    self.matrix = matrix
    self.num_rows = len(matrix)
    self.num_cols = len(matrix[0]) if len(matrix) > 0 else 0

  def get(self, pos):
    if not self.is_valid_pos(pos):
      return None
    return self.matrix[pos.row][pos.col]

  def set(self, pos, val):
    if not self.is_valid_pos(pos):
      return
    self.matrix[pos.row][pos.col] = val

  def find(self, target):
    if self.num_rows == 0: return Pos(-1, -1)
    for row in range(self.num_rows):
      for col in range(self.num_cols):
        if self.matrix[row][col] == target:
          return Pos(row, col)
    return Pos(-1, -1) 
  
  def find_all(self, target, options={}):
    start_row = options.get('start_row', 0)
    end_row = options.get('end_row', self.num_rows - 1)
    start_col = options.get('start_col', 0)
    end_col = options.get('end_col', self.num_cols - 1)

    positions = []
    if self.num_rows == 0: return positions
    for row in range(start_row, end_row):
      for col in range(start_col, end_col):
        if self.matrix[row][col] == target:
          positions.append(Pos(row, col))
    return positions

  def count(self, target):
    count = 0
    for row in range(self.num_rows):
      for col in range(self.num_cols):
        if self.matrix[row][col] == target:
          count += 1
    return count

  def is_valid_pos(self, pos):
    return 0 <= pos.row < self.num_rows and 0 <= pos.col < self.num_cols
