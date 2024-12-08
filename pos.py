class Pos:
  def __init__(self, row, col):
    self.row = row
    self.col = col

  def __eq__(self, other_pos):
    return self.row == other_pos.row and self.col == other_pos.col

  def __add__(self, move):
    return Pos(self.row + move.row, self.col + move.col)

  def __hash__(self):
    return hash(f"{self.row} {self.col}")

