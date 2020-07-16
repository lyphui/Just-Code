class Solution:
    def firstMissingPositive(self, nums):

        for i in range(len(nums)):
            print(i,nums)
            while 0<nums[i]<=len(nums) and nums[i]!=i+1:
                index_tmp=nums[i]-1
                nums[i],nums[index_tmp] = nums[index_tmp],nums[i]
            print(nums)
        for i,n in enumerate(nums):
            if i!=n-1:
                return i+1

    def firstMissingPositive_ref(self, nums):

        for i in range(len(nums)):
            while 0 <= nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
                print(nums)
        print(nums)
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
        return len(nums) + 1

s=Solution()
print(s.firstMissingPositive([3,4,0,5,2,1]))