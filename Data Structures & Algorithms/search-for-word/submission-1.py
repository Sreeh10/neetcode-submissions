# from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # q = deque() # (end_of_string_prefix, size)
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] == word[0]:
        #             q.append(((i,j), 1))

        # while len(q) > 0:
        #     pos, size = q.popleft()
        #     left = 
        #     right =
        #     up = 
        #     down = 

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         dfs(i,j,indx=0)

        path = set()
        def dfs(i,j,word_index):
            if board[i][j] == word[word_index]:
                if word_index == len(word)-1:
                    return True
                else:
                    path.add((i,j))
                    up = False
                    down = False
                    left = False
                    right = False
                    if i > 0 and ((i-1,j) not in path):
                        up = dfs(i-1,j,word_index+1)
                    if i < len(board)-1 and ((i+1,j) not in path):
                        down = dfs(i+1, j, word_index+1)
                    if j > 0 and ((i,j-1) not in path):
                        left = dfs(i,j-1,word_index+1)
                    if j < len(board[0])-1 and ((i,j+1) not in path):
                        right = dfs(i,j+1,word_index+1)
                    
                    path.remove((i,j))
                    return up or down or left or right
            else:
                return False
        
        ans = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ans = ans or dfs(i,j,word_index=0)
            
        return ans
