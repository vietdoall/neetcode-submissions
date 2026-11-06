class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = 0 
        r= row*col-1  #index
        while l<=r:
            mid = (l+r)//2
            #chuyen doi thanh 2d
            l_2d = mid // col
            r_2d = mid % col
            result = matrix[l_2d][r_2d]
            if result == target:
                return True
            elif result < target : 
                l = mid +1
            else : 
                r= mid-1
        return False 
