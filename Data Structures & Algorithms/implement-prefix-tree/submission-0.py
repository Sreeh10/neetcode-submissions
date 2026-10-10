class Node():
    is_word_end : bool
    child : dict[Node]   
    def __init__(self):
        self.is_word_end = False
        self.child = {}
        return

class PrefixTree:

    root : Node # root is empty always
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        offset = 0
        while offset <= len(word):
            if offset == len(word):
                node.is_word_end = True
                break
            
            if word[offset] not in node.child:
                node.child[word[offset]] = Node()
            
            node = node.child[word[offset]]
            offset += 1
        return

    def search(self, word: str) -> bool:
        node = self.root
        offset = 0
        while offset <= len(word):
            if offset == len(word):
                if node.is_word_end :
                    return True
                else:
                    return False
            
            if word[offset] not in node.child:
                return False
            
            node = node.child[word[offset]]
            offset += 1
        return False


        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        offset = 0
        while offset < len(prefix):
            if prefix[offset] not in node.child:
                return False
            node = node.child[prefix[offset]]
            offset += 1
        return True
        
        