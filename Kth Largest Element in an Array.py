# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:22:48 2020

@author: dpatel
"""

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """    
    #nums.sort(reverse=True)
    largest = [ 0 for i in range(k) ] 
    
    for i in range(len(nums)):
        n = k
        for k in range(k):
            if largest[k] <= nums[i]:
                while n > 0:
                    largest[n-1] = largest[n-2]
                    n -= 1
                
                largest[0] = nums[i]
                n = k
                
    print(largest)
    return largest[k-1]
    
if __name__ == "__main__":
    
    #print(findKthLargest([3,2,1,5,6,4], 2))
    #print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    print(findKthLargest([2,1], 2))