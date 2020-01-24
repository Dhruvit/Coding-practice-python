# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:57:44 2020

@author: dpatel
"""

def coinChange(coins, amount):
    
    if not amount: return 0
    
    dp = [amount + 1] * (amount+1)
    
    for i in range(amount+1):
        if i in coins:
            dp[i] = 1
            continue
        
        candidates = [dp[i-coin]+1 for coin in coins if i-coin > 0]
        if candidates:
            dp[i] = min(candidates)
        
    return -1 if dp[amount] > amount else dp[amount]
    
if __name__ == "__main__":
    print(coinChange([1,2,5],11))