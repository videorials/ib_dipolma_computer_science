def isValidMatrix(N,A):
  valid = True

  '''
  Returns True if all elements below the subdiagonal and all
  elements above the superdiagonal are zeros and all elements
  on three diagonals are non-zeroes; otherwise it returns False.
  '''

  sup = -1
  dia = 0
  sub = 1

  for row in MAT:
    for col in row:
      None
      # test something

    print(sup, dia, sub)
    sup += 1
    dia += 1
    sub += 1

  return valid
  

MAT = [[7, 7, 0, 0, 0, 0],
       [1, 2, 1, 0, 0, 0],
       [0, 9,-3, 5, 0, 0],
       [0, 0,-5, 6, 4, 0],
       [0, 0, 0, 7, 7, 2],
       [0, 0, 0, 0, 5, 1]]

print(isValidMatrix(len(MAT),MAT))
