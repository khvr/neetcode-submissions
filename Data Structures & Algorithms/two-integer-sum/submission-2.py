class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        com = {}
        for i in range(0, len(nums)):
            if nums[i] not in com:
                com[target-nums[i]] = i
            else:
                return [com[nums[i]],i] 