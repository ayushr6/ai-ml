#!/usr/bin/env python
# coding: utf-8

# ### 1. The position of next number is calculated by decrementing row number of the previous number by 1, and incrementing the column number of the previous number by 1. At any time, if the calculated row position becomes -1, it will wrap around to n-1. Similarly, if the calculated column position becomes n, it will wrap around to 0.
# 
# ### 2. If the magic square already contains a number at the calculated position, calculated column position will be decremented by 2, and calculated row position will be incremented by 1.
# 
# ### 3. If the calculated row position is -1 & calculated column position is n, the new position would be: (0, n-2). 

# In[15]:


class MagicSquare:
    def print_magic_square(self, n, magic_square):
        for i in range(n):
            for j in range(n):
                print('%2d ' % magic_square[i][j], end='| ')
            print()
            if i!=n-1:
                print('-'*n*5)
    
    def get_magic_square(self, n):
        magic_square = [[0 for i in range(n)] for j in range(n)]
        i = n//2
        j = n-1
        num = 1
        while num <= (n*n):
            if i==-1 and j==n:
                i=0
                j=n-2
            else:
                if i<0:
                    i=n-1
                if j==n:
                    j=0
            if magic_square[i][j]:
                i+=1
                j-=2
                continue
            else:
                magic_square[i][j] = num
                num+=1
            i-=1
            j+=1
            
        self.print_magic_square(n, magic_square)


# In[16]:


generator = MagicSquare()


# In[17]:


generator.get_magic_square(9)

