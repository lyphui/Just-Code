class Solution:
    def search(self, nums, target):
        left_index,right_index=0,len(nums)-1
        while left_index<right_index-1:
            mid_index=(left_index+right_index)//2
            if (mid_index-left_index)<=1 or ((nums[left_index+1]>nums[left_index] ^ nums[mid_index]<nums[mid_index-1])):
                if (target>=nums[left_index] and target <=nums[mid_index]) or (target<=nums[left_index] and target >=nums[mid_index]):
                    right_index=mid_index
                else:
                    left_index=mid_index
            elif (right_index-mid_index)<=1 or ((nums[mid_index+1]>nums[mid_index] ^ nums[right_index]<nums[right_index-1])):
                if (target>=nums[mid_index] and target <=nums[right_index]) or (target<=nums[mid_index] and target >=nums[right_index]):
                    left_index=mid_index
                else:
                    right_index = mid_index
            if target==nums[right_index]:
                return right_index
            elif target==nums[left_index]:
                return left_index
        if target == nums[right_index]:
            return right_index
        elif target == nums[left_index]:
            return left_index
        else:
            return -1

        def search_ref(self, nums, target):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                    lo = mid + 1
                else:
                    hi = mid
            return lo if lo == hi and target == nums[lo] else -1

nums =  [4,5,6,7,0,1,2]
target = 3
s=Solution()
print(s.search(nums,target))