from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:        
        left_index,right_index=0,len(nums)-1
        while left_index<right_index:
            mid_index=(left_index+right_index)//2
            if nums[mid_index]>target:
                right_index=mid_index
            elif nums[mid_index]==target:
                return mid_index
            else:
                left_index=mid_index+1
        return left_index

    def searchInsert_ref(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                return mid
            else:
                left = mid
        return right





nums = [1,3,5,6]
target = 0
s = Solution()
print(s.searchInsert(nums, target))