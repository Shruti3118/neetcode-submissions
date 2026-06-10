class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        low = 0
        high = len(matrix[0])-1
        while low < high:
            for i in range(len(matrix)):
                matrix[i][low], matrix[i][high] = matrix[i][high], matrix[i][low]
            low += 1
            high -= 1

        

        