import numpy as np

class nQ:
    def __init__(self, n):
        self.board = [[0 for i in range(n)] for j in range(n)]
    
    def is_move_safe(self, n, row, col):
        for i in range(col):
            if self.board[row][i]:
                return False
        
        i=row
        j=col
        
        while(i>=0 and j>=0):
            if self.board[i][j]:
                return False
            i-=1
            j-=1
            
        i=row
        j=col
        while(i<n and j>=0):
            if self.board[i][j]:
                return False
            i+=1
            j-=1
            
        return True
    
    def solve(self, n, col):
        if col>=n:
            print(np.array(self.board))
            return True
        
        for i in range(n):
            if self.is_move_safe(n, i, col):
                self.board[i][col]=1
            
                if self.solve(n, col+1):
                    return True

                self.board[i][col]=0
        return False


n = int(input("Enter board length: "))
script = nQ(n)
script.solve(n, 0)