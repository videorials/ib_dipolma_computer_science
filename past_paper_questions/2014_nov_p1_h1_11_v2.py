n = 7
magic_square = [[30,39,48,1 ,10,19,28], #[30,39,48,1 ,10,19,28],
                [38,47,7 ,9 ,18,27,29],
                [46,6 ,8 ,17,26,35,37],
                [5,14 ,16,25,34,36,45],
                [13,15,24,33,42,44,4 ],
                [21,23,32,41,43,3 ,12],
                [22,31,40,49,2 ,11,20]] #[22,31,40,49,2 ,11,20]

magic = True
# sum of diagonals
dia_dn, dia_up = 0, 0
for i in range(n):
    #print(magic_square[i][i], magic_square[(n - 1) - i][i])
    dia_dn += magic_square[i][i]
    dia_up += magic_square[(n - 1) - i][i]
if dia_dn != dia_up:
    magic = False

# sum rows and columns
index_1 = 0
while index_1 < n and magic:
    row_sum, col_sum = 0, 0
    for index_2 in range(n):
        row_sum += magic_square[index_1][index_2]
        col_sum += magic_square[(n - 1) - index_2][index_1]
    if row_sum != dia_dn or col_sum != dia_dn:
        magic = False
    index_1 += 1
if magic:
    print("The array is a magic square.")
else:
    print("The array is not a magic square.")