class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest = 1
        current = 1

        for i in range(1, len(nums)):
            # skip duplicates
            if nums[i] == nums[i - 1]:
                continue

            # consecutive: increase current streak
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                # break in sequence: reset current streak
                current = 1

            # update longest streak
            longest = max(longest, current)

        return longest