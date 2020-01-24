# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:22:40 2020

@author: dpatel
"""


def maxArea(height):    
    maxArea = 0
    
    right = 0
    left = len(height)-1
    
    while(right < left):
        new_area = min(height[right], height[left]) * (left - right)
        maxArea = max(maxArea, new_area)
        
        if height[right] < height[left]:
            right += 1
        else:
            left -= 1
    return maxArea

if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))