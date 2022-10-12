import numpy as np

class KnightTour:
    def __init__(self, n):
        self.row_move = [-2, -2, -1, -1, 1, 1, 2, 2]
        self.col_move = [-1, 1, -2, 2, -2, 2, -1, 1]
        self.board = [[0 for i in range(n)] for j in range(n)]
        
    def is_valid_move(self, n, x, y):
        if x<0 or x>=n or y<0 or y>=n or self.board[y][x]!=0:
            return False
        return True

    def start_knight_tour(self, n, x, y, i):
        if i==n*n:
            print(np.array(self.board))
            return True
            
        if self.is_valid_move(n, x, y)==False:
            return False
        
        self.board[y][x] = i

        for x_move, y_move in zip(self.row_move, self.col_move):
            if self.start_knight_tour(n, x + x_move, y + y_move, i+1):
                return True

        self.board[y][x] = 0
        return False

    
n = int(input("Enter board length: "))
script = KnightTour(n)
script.start_knight_tour(n, 0, 0, 0)