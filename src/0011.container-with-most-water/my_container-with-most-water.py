from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        num_bin=len(height)
        max_water=0
        for i in range(num_bin-1):
            l_num=height[i]
            r_num=height[num_bin-1]
            if l_num > r_num:
                max_water = max(max_water, r_num * (num_bin - 1 - i))
                for j in range(num_bin-2,i,-1):
                    if height[j]>r_num:
                        r_num=height[j]
                        if l_num > r_num:
                            max_water = max(max_water, r_num * ( j- i))
                        else:
                            max_water=max(max_water, l_num * (j - i))
                            break
            else:
                max_water = max(max_water, l_num * (num_bin - 1 - i))

        return max_water




s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))