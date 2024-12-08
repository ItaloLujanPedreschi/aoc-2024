from input_util import InputUtil
from pos import Pos

class Lab:
  DIRS = {
    "UP": Pos(-1, 0),
    "RIGHT": Pos(0, 1),
    "LEFT": Pos(0, -1),
    "DOWN": Pos(1, 0)
  }
  GUARD = '^'
  OBSTRUCTION = '#'
  CLEAR = '.'

  def __init__(self, floor):
    self.floor = floor
    self.guard_starting_pos = floor.find(Lab.GUARD)
    self.guard_pos = self.guard_starting_pos
    self.guard_dir = "UP"

  def move_guard(self):
    next_pos = self.guard_pos + Lab.DIRS[self.guard_dir] 
    if self.floor.get(next_pos) == Lab.OBSTRUCTION:
      self.rotate_guard()
    else:
      self.guard_pos = next_pos

  def rotate_guard(self):
    if self.guard_dir == "UP":
      self.guard_dir = "RIGHT"
    elif self.guard_dir == "RIGHT":
      self.guard_dir = "DOWN"
    elif self.guard_dir == "DOWN":
      self.guard_dir = "LEFT"
    elif self.guard_dir == "LEFT":
      self.guard_dir = "UP"

  def is_guard_in_lab(self):
    return self.floor.is_valid_pos(self.guard_pos)

  def reset_guard(self):
    self.guard_pos = self.guard_starting_pos
    self.guard_dir = "UP"

def part_1_solution():
  file = open("day_6_input.txt")
  lab = Lab(InputUtil.file_to_matrix(file))
  visited_positions = set()

  while lab.is_guard_in_lab():
    visited_positions.add(lab.guard_pos)
    lab.move_guard()
    
  print(len(visited_positions))

def part_2_solution():
  file = open("day_6_input.txt")
  lab = Lab(InputUtil.file_to_matrix(file))
  visited_positions = set()
  max_moves = lab.floor.num_rows * lab.floor.num_cols * 2

  while lab.is_guard_in_lab():
    visited_positions.add(lab.guard_pos)
    lab.move_guard()

  visited_positions.remove(lab.guard_starting_pos)

  count = 0
  for pos in visited_positions:
    lab.reset_guard()
    lab.floor.set(pos, Lab.OBSTRUCTION)
    num_moves = 0
    while lab.is_guard_in_lab() and num_moves < max_moves:
      lab.move_guard()
      num_moves += 1
 
    if num_moves == max_moves:
      count += 1
    lab.floor.set(pos, Lab.CLEAR)

  print(count)

part_1_solution()
part_2_solution()
