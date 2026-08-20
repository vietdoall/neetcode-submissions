class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seem = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in seem:
                return [seem[x],i]
            seem[nums[i]]= i

           
        