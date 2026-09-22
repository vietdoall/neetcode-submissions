class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        long = 0 
        for x in num_set: 
            if x-1 not in num_set:
                len = 1
                while x + len in num_set:
                    len +=1
                long = max(len,long)
        return long 