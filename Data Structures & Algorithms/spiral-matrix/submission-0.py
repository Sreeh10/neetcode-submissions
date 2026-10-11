class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        move = "right"
        # whenever a switch goes from True to False
        # we decrease the corresponding dimension by 1
        h_switch = True
        w_switch = True
        h = len(matrix)
        w = len(matrix[0])
        h_space = [0,h-1] # both inclusive
        w_space = [0,w-1]

        while h_space[0] <= h_space[1] and w_space[0] <= w_space[1]:
            # print(f"{move=}   \t{h_space=}{w_space=}{ans=}")
            if move == "right":
                for j in range(w_space[0], w_space[1]+1, 1):
                    ans.append(matrix[h_space[0]][j])
                h_space[0] += 1
                move = "down"
            elif move == "down":
                for i in range(h_space[0], h_space[1]+1, 1):
                    ans.append(matrix[i][w_space[1]])
                w_space[1] -= 1
                move = "left"
            elif move == "left":
                for j in range(w_space[1], w_space[0]-1, -1):
                    ans.append(matrix[h_space[1]][j])
                h_space[1] -= 1
                move = "up"
            elif move == "up":
                for i in range(h_space[1], h_space[0]-1, -1):
                    ans.append(matrix[i][w_space[0]])
                w_space[0] += 1
                move = "right"

        return ans


        # 1  2  3  4 
        # 5  6  7  8 
        # 9  10 11 12

