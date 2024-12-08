file = open("input.txt", "r")

def is_valid(nums):
  is_increasing = False
  if nums[1] > nums[0]:
    is_increasing = True
  for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]: return False
    diff = abs(nums[i] - nums[i - 1])
    if diff < 1 or diff > 3: return False
    if is_increasing:
      if not nums[i] > nums[i - 1]: return False
      else: continue
    else:
      if not nums[i] < nums[i - 1]: return False
      else: continue
  return True
        

safe_reports_count = 0
for line in file:
  if is_valid([int(num) for num in line.split()]):
    safe_reports_count += 1

print(safe_reports_count)

'''

How the validation check will be done...

The validation can be brute forced in O(n^2) but O(n) is possible as well

We are going to check every possibility of paths to a successful "report"
If any of those paths are successful then the report is valid

We know that a successful report has an increasing or decreasing trend,
and it has at most a single error

If we encounter an error, that error must be resolved so we can be greedy here

We will run 2 checks...
 - The first assumes that the trend is increasing
 - The second assumes that the trend is decreasing

When either of these checks encounters an error we will begin 2 more checks
 - The first will skip the index at which we found the error
 - The second will skip the index before the error

Given the example 1,3,2,6,7
As we make our way through this report, the error we find is that while we
expect the numbers to be increasing, we find a 2 after 3
If we skip the 3, the 2 will be greater than 3 from the following number and
we will get an invalid report
This is why we must check both paths

This method will also handle the cases where we get repeated numbers back to
back or we find a gap larger than the allowed 3

'''
file = open("input.txt", "r")

def is_valid_r(nums, prev_index, index, increasing, contains_error):
  if index == len(nums): return True
  if prev_index == -1:
    return is_valid_r(nums, index, index + 1, increasing, contains_error)

  curr_error = False
  if increasing:
    if nums[index] <= nums[prev_index] or nums[index] > nums[prev_index] + 3:
      curr_error = True
  else:
    if nums[index] >= nums[prev_index] or nums[index] < nums[prev_index] - 3:
      curr_error = True

  if contains_error and curr_error: return False
  if curr_error:
    return (is_valid_r(nums, prev_index, index + 1, increasing, True) or
            is_valid_r(nums, prev_index - 1, index, increasing, True))
  else:
    return is_valid_r(nums, index, index + 1, increasing, contains_error)


def is_valid(nums):
  return (is_valid_r(nums, 0, 1, True, False) or
          is_valid_r(nums, 0, 1, False, False))

count = 0

for line in file:
  if is_valid([int(num) for num in line.split()]):
    count += 1
  else:
    print(line)

print(count)
