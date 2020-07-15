from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water_volum=0
        left_h=0
        right_h=0
        range_list=[]
        for i,h in enumerate(height):
            if h>left_h:
                if len(range_list)>0:
                    water_volum+=sum([left_h-_i for _i in range_list])
                left_h=h
                range_list=[]
            else:
                right_h=max(right_h,0)