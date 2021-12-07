"Bingo with a squid"

file=open("numbers.txt")
lines=file.readlines()
lines[0]=lines[0].strip()
all_numbers=lines[0].split(",")
boards=[]
numbers=[]
winner=False

# checks all the rows on a board, then if it didn't win, checks columns
def check_for_bingo(board,num):
    check_rows(board,num)
    if not winner:
        check_columns(board,num)

def check_rows(board,num):
    for row in board:
        row_count=0
        for n in row:
            if n in numbers:
                row_count+=1
        if row_count==5:
            print(f"Row complete on board!")
            global winner
            winner=True
            count_it_up(board,int(num))

def check_columns(board,num):
    for column in range(5):
        col_count=0
        for row in range(5):
            if board[row][column] in numbers:
                col_count+=1
        if col_count==5:
            print(f"Column complete on board!")
            count_it_up(board,int(num))


def check_diagonals(board,num):
    diag_count=0
    for i in range(5):
        if board[i][i] in numbers:
            diag_count+=1
    if diag_count==5:
        count_it_up(board,int(num))
    diag_count=0
    for i in range(5):
        if board[i][4-i] in numbers:
            diag_count+=1
    if diag_count==5:
        count_it_up(board,int(num))
    
# if a board wins, the 'score' is tallied, then the board is removed from the game
def count_it_up(board,num):
    print()
    print(board)
    total=0
    for row in board:
        for n in row:
            if n not in numbers:
                total+=int(n)
    print(f"total is {total}, last number is {num}.\nThe answer is {total*num}")
    boards.remove(board)
    


#test=[['1','2','3','4','5'],['6','7','8','9','10'],['11','12','13','14','15'],['16','17','18','19','20'],['21','22','23','24','25']]
#numbers=['1','7','13','19','25']
#check_diagonals(test,'25')


# construct boards
for i in range(1,len(lines)): #len(lines)
    bs=-1
    if lines[i]=="\n":
        boards.append([])
        bs+=1
    else:
        #print(len(boards))
        row=lines[i].strip()
        row=row.split(" ")
        for i,n in enumerate(row):
            if n=='':
                row.pop(i)
        #if '' in row:
        #    row.remove('')
        boards[bs].append(row)

# "call" a number and check all the boards
for n in range(len(all_numbers)):
    numbers.append(all_numbers[n])
    for board in boards:
        winner=False
        check_for_bingo(board,all_numbers[n])

