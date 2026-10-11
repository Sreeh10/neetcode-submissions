class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # rotate (90deg clockwise)= transpose + "vertical mirror" image
        # rotate (-90deg clockwise)= transpose + "horizontal mirror" image
        # abc adg gda
        # def beh heb
        # ghi cfi ifc

        n = len(matrix)
        # ---- transpose ----
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # ---- vertical mirror image---
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-(j+1)] = matrix[i][n-(j+1)], matrix[i][j]

        return