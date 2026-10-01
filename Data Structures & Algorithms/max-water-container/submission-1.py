class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l ,r = 0 , len(heights)-1 
        max_con= 0
        while l < r : 
            weight = r - l
            h = min(heights[l],heights[r])
            con= h * weight
            max_con =max (con, max_con)
            if heights[r]> heights[l]:
                l+=1
            else : 
                r-=1

        return max_con