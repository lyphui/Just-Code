class Solution:
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            if nums[i]>0 and nums[i]<len(nums):continue
