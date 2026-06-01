class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in complement:
                return [complement[diff],i]
            else:
                complement[nums[i]]=i
        return