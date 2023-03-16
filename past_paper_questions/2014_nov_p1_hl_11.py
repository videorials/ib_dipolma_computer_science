def duplicates(array):
    duplicates = False
    unique_values = []
    for row in array:
        for col in row:
            if col not in unique_values:
                unique_values.append(col)
            else:
                return True
    return duplicates

def valid(n, array):
    valid = True
    if duplicates(array):
        return False

    # check rows
    for row in range(n):
        sum = 0
        for col in range(n):
            sum += array[row][col]
        if sum != 175:
            return False

    # check columns
    for col in range(n):
        sum = 0
        for row in range(n):
            sum += array[row][col]
        if sum != 175:
            return False        

    # check diagonal down
    sum = 0
    index = 0
    while index < len(array[0]):
        sum += array[index][index]
        index += 1
    if sum != 175:
        return False

    # check diagonal up
    sum = 0
    row = n-1
    for col in range(0, n):
        sum += array[row][col]
        row -= 1
    if sum != 175:
        return False
    return valid

magic_square = [[30,39,48,1 ,10,19,28], #[30,39,48,1 ,10,19,28],
                [38,47,7 ,9 ,18,27,29],
                [46,6 ,8 ,17,26,35,37],
                [5,14 ,16,25,34,36,45],
                [13,15,24,33,42,44,4 ],
                [21,23,32,41,43,3 ,12],
                [22,31,40,49,2 ,11,20]] #[22,31,40,49,2 ,11,20]

print(valid(len(magic_square), magic_square))