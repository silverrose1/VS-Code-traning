row, column, block = [[] for i in range(9)], [[] for i in range(9)], [[] for i in range(9)]

#create list of row #####
for i in range(9):
    a=input('enter valid row ' + str(i+1) + ' with 9 digits:')
    for j in range(9):
        row[i].append(a[j])
# create list of column #####
for i in range(9):
    for j in range (9):
        column[i].append(row[j][i])
# create list of block  #####
for i in range(9):
    for j in range(9):
        block_row = i // 3  # Determine which block row (0, 1, or 2)
        block_col = j // 3  # Determine which block column (0, 1, or 2)
        block_index = block_row * 3 + block_col  # Calculate the block index (0-8)
        block[block_index].append(row[i][j])

def check(lst):
    for i in range(9):
        for j in range (1, 10):
            if str(j) not in lst[i]:
                # isSudoku=False
                return False
                break
    return True

if check(row) and check(column) and check(block):
    print('This is a valid sudoku')
else:
    print('This is not a valid sudoku')
