# count the number of digits in an integer...
def cnt_dgts(int):
    cnt = 0
    while int > 0:
        cnt += 1
        int //= 10

    return cnt