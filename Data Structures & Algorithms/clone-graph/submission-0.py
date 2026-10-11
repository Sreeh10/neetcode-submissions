"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # maintain a mapping of prevNode to currentNode
        d = {None:None}
        def dfs(card: Node): # updates the oldcard to newcard mapping for the entire descendandts of given node
            if card in d:
                return d[card]
            d[card] = Node()
            newneighbors = [dfs(n) for n in card.neighbors]
            d[card].val = card.val
            d[card].neighbors = [dfs(n) for n in card.neighbors]
            return
        
        dfs(node)
        return d.get(node, None)