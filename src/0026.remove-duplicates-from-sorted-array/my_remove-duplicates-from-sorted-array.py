from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_zero_index=0
        last_num=0.1
        i=0
        while i<len(nums):
            if nums[i]==last_num:
                i+=1
            else:
                if last_zero_index!=i:
                    nums[last_zero_index]=nums[i]
                last_zero_index+=1
                last_num=nums[i]
                i+=1
        print(nums)
        return last_zero_index
    def removeDuplicates_simplified(self, nums: List[int]) -> int:
        last_zero_index=0
        last_num=0.1
        i=0
        while i<len(nums):
            if nums[i]!=last_num:
                nums[last_zero_index]=nums[i]
                last_zero_index+=1
                last_num=nums[i]
            i += 1
        print(nums)
        return last_zero_index

    def removeDuplicates_ref(self, nums: List[int]) -> int:
        if not nums:
            return None
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1
nums = [0,0,0,1,1,1,1,2,2,3,3,4,5,7,7,9]
s=Solution()
print(s.removeDuplicates(nums))