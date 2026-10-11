class DSU:
    parent : list[int] # not necessarily the root of the label, just any ancestor
    # if parent[k] == k, then k is a root label 

    def __init__(self):
        self.parent = []
        
    def insert(self, x: int):
        self.parent.append(x)

    def union(self, a:int, b:int):
        minn = min(self.parent[a], self.parent[b])
        self.parent[self.parent[a]] = minn
        self.parent[self.parent[b]] = minn

    
    def find(self, x: int):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def count_roots(self):
        count = 0
        for x in range(len(self.parent)):
            if self.parent[x] == x:
                count += 1
        return count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # union find
        count = 0
        d = DSU()
        labels = [[None for j in range(len(grid[0]) )] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue

                up = True # true if water, false if land
                left = True

                if i > 0:
                    up = True if grid[i-1][j] == "0" else False
                if j > 0:
                    left = True if grid[i][j-1] == "0" else False
                
                
                if up and left: # water up, water left -> new top-left corner
                    labels[i][j] = count
                    d.insert(labels[i][j])
                    count += 1

                if up and (not left) : # water up , land left 
                    labels[i][j] = labels[i][j-1] # copy label of left 
                if (not up) and left: # land up, water left
                    labels[i][j] = labels[i-1][j] # copy label of up
                if (not up) and (not left):
                    d.union(labels[i-1][j], labels[i][j-1])
                    labels[i][j] = d.find(labels[i-1][j])

        return d.count_roots()

                

