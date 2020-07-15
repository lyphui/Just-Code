from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        first_invalid_index=0
        while i <len(nums):
            if nums[i]!=val:
                nums[first_invalid_index] = nums[i]
                first_invalid_index+=1
            i+=1
        return first_invalid_index

    def removeElement_ref(self, nums: List[int], val: int) -> int:
        if not nums:
            return None
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx

nums = [3,2,2,3]
val = 3
s=Solution()
print(s.removeElement(nums,val))