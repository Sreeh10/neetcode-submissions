class Node:
    is_word_end : bool
    child : dict[Node]
    def __init__(self):
        self.is_word_end = False
        self.child = {}

class Trie:
    root : Node
    def __init__ (self):
        self.root = Node()
    
    def insert (self, word: str):
        node = self.root
        offset = 0
        while offset < len(word):
            if word[offset] not in node.child:
                node.child[word[offset]] = Node()
            node = node.child[word[offset]]
            offset += 1
        node.is_word_end = True
        return
    
    def search (self, word: str):
        node = self.root
        offset = 0
        while offset < len(word):
            if word[offset] not in node.child:
                return False, False
            node = node.child[word[offset]]
            offset += 1
        
        return True, node.is_word_end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        ans = set() # set of words found in the board
        trie = Trie()
        for word in words:
            trie.insert(word)

        # if curr in prefx, explore neighbours
        # if curr is word (means its a prefix too), append curr to answer, explore neighbours
        # if curr is neither, dont pursue this path
        
        def dfs(i,j): # need not return anything, just keep noting the words
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0:
                return
            if board[i][j] == '#':
                return
            
            nonlocal curr_word
            curr_word += board[i][j]
            board[i][j] = '#'
            
            nonlocal trie
            is_prefix, is_word = trie.search(curr_word)
            
            if is_word:
                ans.add(curr_word)

            if is_prefix:
                dfs(i-1,j) # up
                dfs(i+1,j) # down
                dfs(i,j+1) # right
                dfs(i,j-1) # left
            
            board[i][j] = curr_word[-1]
            curr_word = curr_word[:-1]
            return


        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_word = ""
                dfs(i,j)

        return list(ans)
        