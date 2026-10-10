from collections import deque

class Node:
    is_word_end : bool
    child : dict
    def __init__(self):
        self.is_word_end = False
        self.child = {}

class WordDictionary:

    root : Node
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        offset = 0
        while offset < len(word):
            if word[offset] not in node.child:
                node.child[word[offset]] = Node()
            node = node.child[word[offset]]
            offset += 1
        node.is_word_end = True

    def search(self, word: str) -> bool:
        q = deque()
        q.append((self.root, 0)) # node, offset
        while len(q) > 0:
            node, offset = q.popleft()
            if offset == len(word):
                if node.is_word_end:
                    return True
                else:
                    return False
            
            elif offset < len(word):
                if word[offset] == ".":
                    for k,v in node.child.items():
                        q.append((v,offset+1))
                elif word[offset] in node.child:
                    q.append((node.child[word[offset]], offset+1))
                else:
                    pass # skip the children of this node
            else: # we are doing BFS, so all the shorter words are already done
                return False # this line never executes, because we break on or before len(word)
        return False
