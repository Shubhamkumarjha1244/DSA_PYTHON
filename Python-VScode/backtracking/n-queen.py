def safe_to_go(row,col,n,board):
    i=row-1
    while i >=0:
        if board[i][col]==1:
            return False
        i -=1
    i=row-1
    j=col-1
    while j>=0 and i >=0 :
        if board[i][j]==1:
            return False
        i -=1
        j -=1
    i=row-1
    j=col+1
    while j< n and i >=0 :
        if board[i][j]==1:
            return False
        i -=1
        j +=1
    return True




def print_n_queen(row,n,board):
    if row==n:
        # print(board)
        # return
        for i in range(n):
                print(board[i],end='\n')
        print()
    for col in range(n):
        if safe_to_go(row,col,n,board):
            board[row][col]=1
            print_n_queen(row+1,n,board)
            board[row][col]=0
    return



def n_queen(n):
    board=[[0 for i in range(n)] for i in range(n)]
    print_n_queen(0,n,board)


n=int(input("size of chess board--"))
n_queen(n)