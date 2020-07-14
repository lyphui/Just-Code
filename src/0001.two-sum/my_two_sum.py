from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_of_nums=len(nums)
        for i,item in enumerate(nums):
            res=target-item
            for j ,jtem in zip(range(i+1,num_of_nums),nums[i+1:]):
                if res==jtem:
                    return [i,j]

    def twoSum_ref(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, v in enumerate(nums):
            another = target - v
            if another not in dict:
                dict[v] = i
            else:
                return [dict[another],i]

nums = [2, 90,3,65,7, 12, 15]
target = 18
s=Solution()
print(s.twoSum(nums,target))
print(s.twoSum_ref(nums,target))


'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''