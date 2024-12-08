from matrix import Matrix

class InputUtil:
  def file_to_matrix(file, substitutes={}):
    matrix = []
    for line in file:
      row = []
      for char in line:
        if char in substitutes:
          row.append(substitutes[char])
        else:
          row.append(char)
      matrix.append(row)

    return Matrix(matrix)
