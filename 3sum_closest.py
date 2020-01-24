# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:29:17 2020

@author: dpatel
"""

def threeSumClosest(nums, target):
        print(nums)
        nums.sort()
        #print(nums)
        #print('\n')
        result = float('inf')        
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                '''
                print(nums[i],nums[left],nums[right])
                print((result, total), abs(target-total), abs(target-result), [abs(target-total) <= abs(target-result)])
                print((result, total)[abs(target-total) <= abs(target-result)])
                '''
                
                #if we found 
                result = (result, total)[abs(target-total) <= abs(target-result)]
                
                if result == target:
                    return result
                
                #print((total < target),(total > target))
                #print(left, right)
                left += (total < target)
                right -= (total > target)
                #print(left, right)
                #print('\n')
        return result
        
if __name__ == "__main__":
    #print(threeSumClosest([-1, 2, 1, -4], 1))
    #print(threeSumClosest([1, 1, 1, 0], 100))
    print(threeSumClosest([0, 2, 1, -3], 1))
    #print(threeSumClosest([0,1,2], 3))