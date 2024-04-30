class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == ".":
                    for c in range(1,10):
                        if (self.isValid(board,i,j,c)):
                            board[i][j] = str(c)
                            
                            if self.solveSudoku(board) == True:
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    
    def isValid(self,board, row,col,c):
        for temp in range(0,9):
            if board[row][temp] == str(c): #check all the elements in a row
                return False
            if board[temp][col] == str(c): # check all column elements
                return False
            #print("checking element for i,j",row,col,"elements checked",board[3 * (row//3) + i//3][3 * (col//3) + i%3], "indexes",3 * (row//3) + i//3, 3 * (col//3) + i%3)
            if board[3 * (row//3) + temp//3][3 * (col//3) + temp%3] == str(c):
                return False
        return True
        
