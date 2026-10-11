class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # if an element is zero, 
        # mark its row first and column-first as zero

        # but how to know if the zero in the first row or first column
        # was pre-existent or came due to our overwrite?

        # if it was pre-existent, then m[0][0] will be marked zero
        # just save the m[0][0] in a separate element

        m_0_0 = matrix[0][0]
        zero_in_first_row = False
        zero_in_first_col = False
        
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                zero_in_first_row = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zero_in_first_col = True

        for i in range(1,len(matrix)):
            if matrix[i][0] == 0:
                matrix[0][0] = 0
                break # already set zero, no use pursuing

        for j in range(1,len(matrix[0])):
            if matrix[0][j] == 0:
                matrix[0][0] = 0
                break
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,len(matrix)): # go to each row head
            if matrix[i][0] == 0: # if head is zero, set entire row zero
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        for j in range (1,len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        if zero_in_first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if zero_in_first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                

        return