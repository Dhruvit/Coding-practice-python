# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:37:16 2020

@author: dpatel
"""

def climbStairs(n):
    
        dp = [0] * (n + 1)
        
        dp [0] = 1
        dp [1] = 1
        
        if n > 1:
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]
                
        print(dp)    
        return dp[n]
    
if __name__ == "__main__":
    print(climbStairs(4))