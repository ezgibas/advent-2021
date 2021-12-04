a_file = open("advent4input.txt", "r")
#a_file = open("advent4test.txt", "r")

inpt = []

for line in a_file:

  stripped_line = line.strip()

  line_list = stripped_line.split()

  inpt.append(line_list)


a_file.close()

#numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
numbers = [15,62,2,39,49,25,65,28,84,59,75,24,20,76,60,55,17,7,93,69,32,23,44,81,8,67,41,56,43,89,95,97,61,77,64,37,29,10,79,26,51,48,5,86,71,58,78,90,57,82,45,70,11,14,13,50,68,94,99,22,47,12,1,74,18,46,4,6,88,54,83,96,63,66,35,27,36,72,42,98,0,52,40,91,33,21,34,85,3,38,31,92,9,87,19,73,30,16,53,80]
numbers = list(map(str, numbers))


def make_boards(list_of_lists):
    list_of_boards = []
    for l in list_of_lists:
        if not l:
            list_of_boards.append([])
    list_of_boards.append([])
    i = 0
    for l in list_of_lists:
        if l:
            list_of_boards[i].append(l)
        else:
            i += 1
    return list_of_boards


list_of_boards = make_boards(inpt)

def mark_board(board, num):
    for line in board:
        for i in range(len(line)):
            if line[i] == num:
                line[i] = "X"
    return board

def mark_all_boards(boards, num):
    return list(map(lambda b: mark_board(b, num), boards))

# determines if any board has completed bingo
def any_bingo(boards):
    return any(map(bingo, boards))

def bingo(board):
    b = horiz_bingo(board) or vert_bingo(board)
    return b

# determines if at least one row has been completed
def horiz_bingo(board):
    return any(map(row_complete, board))

# determines if a row is complete
def row_complete(row):
    return all(map(lambda val:  val == 'X', row))

# determines if at least one column has been completed
def vert_bingo(board):
    columns = []
    for i in range(len(board[0])):
        column = list(map(lambda l: ith_index(l, i), board))
        columns.append(column)
    return any(map(row_complete, columns))

def ith_index(list, i):
    return list[i]

i = 0
cur_num = 0
while not any_bingo(list_of_boards):
    cur_num = numbers[i]
    list_of_boards = mark_all_boards(list_of_boards, cur_num)
    i += 1

for board in list_of_boards:
    if bingo(board):
        bingo_board = board

def find_unmarked(board):
    unmarked = []
    for line in board:
        for val in line:
            if not val == 'X':
                unmarked.append(val)
    return unmarked

unmarked_list = find_unmarked(bingo_board)
unmarked_sum = sum(map(int, unmarked_list))

#print(unmarked_sum)
#print(cur_num)


"""PART 2"""

list_of_boards = make_boards(inpt)

def find_bingo(boards):
    for board in boards:
        if bingo(board):
            bingo_board = board
    return bingo_board

i = 0
while len(list_of_boards) > 1:
    cur_num = numbers[i]
    list_of_boards = mark_all_boards(list_of_boards, cur_num)
    if any_bingo(list_of_boards):
        list_of_boards = [board for board in list_of_boards if not bingo(board)]
    i += 1
    
    

last_winner = list_of_boards[0]
while not bingo(last_winner):
    cur_num = numbers[i]
    last_winner = mark_board(last_winner, cur_num)
    i += 1
    


#print(list_of_boards)
print(sum(map(int, find_unmarked(last_winner))))
print(cur_num)
#print(last_winner)










