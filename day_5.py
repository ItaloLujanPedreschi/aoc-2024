from graph_util import GraphUtil
from collections import defaultdict

file = open("day_5_input.txt", "r")

def setup():
  edge_lines = []
  page_lines = []
  adding_edges = True
  for line in file:
    if line.strip() == '':
      adding_edges = False 
      continue
    if adding_edges:
      edge_lines.append(line.strip())
    else:
      page_lines.append(line.strip())
  return edge_lines, page_lines

def validate_nums(adj_list, nums):
  seen = set()
  for num in nums:
    for prereq in adj_list[num]:
      if prereq in nums and prereq not in seen:
        return False
      seen.add(num)
  return True

def part_1_solution():
  edge_lines, page_lines = setup() 
  adj_list = GraphUtil.create_adj_list(
    edge_lines,
    lambda line: (int(line.split('|')[1]), int(line.split('|')[0]))
  )
  output = 0

  for line in page_lines:
    nums = [int(num) for num in line.split(',')]
    if validate_nums(adj_list, nums):
      output += nums[len(nums) // 2]

  print(output)

def part_2_solution():
  edge_lines, page_lines = setup()
  adj_list = GraphUtil.create_adj_list(
    edge_lines,
    lambda line: (int(line.split('|')[1]), int(line.split('|')[0]))
  )
  rev_adj_list = GraphUtil.create_adj_list(
    edge_lines,
    lambda line: (int(line.split('|')[0]), int(line.split('|')[1]))
  )
  output = 0

  invalid_lines = []
  for line in page_lines:
    nums = [int(num) for num in line.split(',')]
    if not validate_nums(adj_list, nums):
      invalid_lines.append(nums)
  for nums in invalid_lines:
    local_prereqs = defaultdict(list)
    for num in nums:
      for pre in rev_adj_list[num]:
        if pre in nums:
          local_prereqs[pre].append(num)

    fixed_nums = GraphUtil.topo_sort(local_prereqs)
    output += fixed_nums[len(fixed_nums) // 2]

  print(output)

# part_1_solution()
part_2_solution()

