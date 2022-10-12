#!/usr/bin/env python
# coding: utf-8

# In[35]:


class SudukoSolver():
    def __init__(self, matrix):
        self.matrix = matrix
        
    def print_board(self):
        for i in range(9):
            for j in range(9):
                print('%2d ' % self.matrix[i][j], end='')
            print()
    
    def check_row(self, row, num):
        for i in range(9):
            if self.matrix[row][i]==num:
                return False
        return True
    
    def check_col(self, col, num):
        for i in range(9):
            if self.matrix[i][col]==num:
                return False
        return True
    
    def check_box(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if self.matrix[row+i][col+j]==num:
                    return False
        return True
    
    def is_move_safe(self, row, col, num):
        if self.check_row(row, num) and self.check_col(col, num) and self.check_box(row-row%3, col-col%3, num):
            return True
        return False
    
    def main(self, row=0, col=0):
        n=9
        if row==n-1 and col==n:
            return True
        if col==n:
            row+=1
            col=0
        if self.matrix[row][col]!=0:
            return self.main(row, col+1)
        for num in range(1, n+1):
            if self.is_move_safe(row, col, num):
                self.matrix[row][col]=num
                if self.main(row, col+1):
                    return True
            self.matrix[row][col]=0
        return False

    def solve_suduko(self):
        if self.main():
            self.print_board()
        else:
            print('cannot solve this sudoko')
    


# In[36]:


suduko = [[0, 2, 0, 0, 0, 0, 0, 5, 0],
        [8, 5, 4, 0, 0, 0, 1, 0, 0],
        [9, 0, 0, 6, 5, 8, 3, 4, 2],
        [4, 0, 0, 5, 8, 2, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 9, 6, 0, 0, 4],
        [1, 4, 2, 8, 6, 3, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 4, 6, 1],
        [0, 6, 0, 0, 0, 0, 0, 2, 0]]


# In[37]:


suduko_solver = SudukoSolver(suduko)


# In[38]:


suduko_solver.solve_suduko()

