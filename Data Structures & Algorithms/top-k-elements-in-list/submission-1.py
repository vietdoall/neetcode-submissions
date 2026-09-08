class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums = [1,2,2,3,3,3], k = 2
       count = Counter(nums)
       return [num for num,_ in count.most_common(k)]