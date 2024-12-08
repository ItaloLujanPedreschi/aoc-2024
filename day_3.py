file = open("input.txt")

contents = file.read()

def check_substring(s, i, sub):
  for j in range(len(sub)):
    if not s[i + j] == sub[j]:
      return False
  return True

total = 0
i = 0
enabled = True

while i < len(contents) - 7:
  if check_substring(contents, i, "do()"):
    enabled = True
  if check_substring(contents, i, "don't()"):
    enabled = False
  if check_substring(contents, i, "mul("):
    j = i + 4
    first_num_invalid = False
    first_num = 0
    while j < len(contents):
      if contents[j].isdigit():
        first_num *= 10
        first_num += int(contents[j])
      elif contents[j] == ",":
        break
      else:
        first_num_invalid = True
        break
      j += 1
 
    k = j + 1
    second_num_invalid = False
    second_num = 0
    while k < len(contents):
      if contents[k].isdigit():
        second_num *= 10
        second_num += int(contents[k])
      elif contents[k] == ")":
        break
      else:
        second_num_invalid = True
        break
      k += 1

    if not first_num_invalid and not second_num_invalid and enabled:
      total += first_num * second_num 
  i += 1

print(total)
