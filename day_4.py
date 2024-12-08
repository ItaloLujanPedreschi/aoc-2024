from input_util import InputUtil
from pos import Pos

class WordSearch:
  DIRS = [
    Pos(0, 1),
    Pos(1, 0),
    Pos(0, -1),
    Pos(-1, 0),
    Pos(1, 1),
    Pos(-1, -1),
    Pos(1, -1),
    Pos(-1, 1)
  ]

  def __init__(self, grid):
    self.grid = grid 

  def is_word_in_direction(self, word, pos, dir):
    curr_pos = pos
    for i in range(len(word)):
      if (not self.grid.is_valid_pos(curr_pos)
          or self.grid.get(curr_pos) != word[i]):
        return False
      curr_pos += dir
    return True

  def word_count_at_pos(self, word, pos):
    count = 0
    for dir in WordSearch.DIRS:
      if self.is_word_in_direction(word, pos, dir):
        count += 1 
    return count 

  def get_num_word_matches(self, word):
    count = 0
    starting_positions = self.grid.find_all(word[0])
    for pos in starting_positions:
      count += self.word_count_at_pos(word, pos)
    return count

def part_1_solution():
  file = open("day_4_input.txt", "r")
  word_search = WordSearch(InputUtil.file_to_matrix(file))
  print(word_search.get_num_word_matches("XMAS"))

def has_xmas(matrix, a_row, a_col):
  top_left = matrix[a_row - 1][a_col - 1]
  top_right = matrix[a_row - 1][a_col + 1]
  bottom_left = matrix[a_row + 1][a_col - 1]
  bottom_right = matrix[a_row + 1][a_col + 1]

  if top_left == bottom_right or top_right == bottom_left:
    return False
  if not ((top_left == 'M' and bottom_right == 'S') or
          (top_left == 'S' and bottom_right == 'M')):
    return False
  if not ((top_right == 'M' and bottom_left == 'S') or
          (top_right == 'S' and bottom_left == 'M')):
    return False

  return True

def part_2_solution():
  file = open("day_4_input.txt", "r")
  word_search = WordSearch(InputUtil.file_to_matrix(file))

  count = 0
  a_positions = word_search.grid.find_all('A', {
    "start_row": 1,
    "end_row": word_search.grid.num_rows - 1,
    "start_col": 1,
    "end_col": word_search.grid.num_cols - 1
  })
  for pos in a_positions:
   if has_xmas(word_search.grid.matrix, pos.row, pos.col):
     count += 1

  print(count) 

part_1_solution()
part_2_solution()

