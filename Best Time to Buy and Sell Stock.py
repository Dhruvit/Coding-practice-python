# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:54:06 2020

@author: dpatel
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # for maximum profit buy should be minimum and sell would be maximum
    
    if len(prices) < 2:
            return 0
        
    p = prices[1] - prices[0]
    b = prices[0]
    for i in range(1,len(prices)):
        p = max(prices[i] - b, p)
        b = min(prices[i],b)
    return max(p,0)

if __name__ == "__main__":
    
    print(maxProfit([7,1,5,3,6,4]))