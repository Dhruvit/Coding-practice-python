# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:37:46 2020

@author: dpatel
"""

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    # the length of the input array
    length = len(nums)
    
    #the answer array to be returened
    answer = [0]*length
    
    print(answer)
    
    answer[0] = 1
    
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]
        
    R = 1
    
    for i in reversed(range(length)):
        answer[i] = answer[i] * R
        R *= nums[i]
    
    return answer

if __name__ == "__main__":
    
    print(productExceptSelf([1,2,3,4,5]))