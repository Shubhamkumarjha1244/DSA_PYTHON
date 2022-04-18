def finder(row,col,board,word):
        if len(word)==0:
            for ele in range(len(board)):
                print(board[ele])
            print()
            return
        if row > (len(board)-1) or col > (len(board[0])-1) or col < 0 or row < 0 or board[row][col]!=word[0] or board[row][col]=='#':
            return
        temp=board[row][col]
        board[row][col]='#'
        res=finder(row+1,col,board,word[1:]) or finder(row,col+1,board,word[1:]) or finder(row-1,col,board,word[1:]) or finder(row,col-1,board,word[1:])
        board[row][col]=temp
        return res
def exist( board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
               finder(i,j,board,word)

board=[["A","B","C"],["D","E","F"]]
word='ABE'
print(exist(board,word))