def tokenize_line(line):
  target, nums = line.split(':')
  return int(target), [int(num) for num in nums.strip().split(' ')]

def can_make_equation(nums, target):
  def dfs(curr_total, i):
    if i == len(nums):
      return curr_total == target
    return dfs(curr_total * nums[i], i + 1) or dfs(curr_total + nums[i], i + 1)

  return dfs(nums[0], 1)

def can_make_equation_2(nums, target):
  def dfs(curr_total, i):
    if i == len(nums):
      return curr_total == target
    return (dfs(curr_total * nums[i], i + 1)
         or dfs(curr_total + nums[i], i + 1)
         or dfs(int(str(curr_total) + str(nums[i])), i + 1))

  return dfs(nums[0], 1)

def part_1_solution():
  file = open("day_7_input.txt", "r")
  count = 0

  for line in file:
    target, nums = tokenize_line(line)
    if can_make_equation(nums, target):
      count += target 

  print(count)

def part_2_solution():
  file = open("day_7_input.txt", "r")
  count = 0

  for line in file:
    target, nums = tokenize_line(line)
    if can_make_equation_2(nums, target):
      count += target

  print(count)

part_1_solution()
part_2_solution()
