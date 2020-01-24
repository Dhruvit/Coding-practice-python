# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:52:28 2020

@author: dpatel
"""
def getUniquePaths(m, n, memo):
    
    if m >= 0 and n >= 0:
        if memo[m][n] == 0:
            memo[m][n] = getUniquePaths(m, n-1, memo) + getUniquePaths(m-1, n, memo)
        return memo[m][n]
    else:
        return 0
    
def uniquePaths(m, n):
    
    memo = [[0 for i in range(n)] for i in range(m)]
    
    m -= 1
    n -= 1
    
    memo[0][0] = 1
    if n >= 1 : memo[0][1] = 1
    if m >= 1 : memo[1][0] = 1
    
    if memo[m][n] == 0:
        memo[m][n] = getUniquePaths(m, n-1, memo) + getUniquePaths(m-1, n, memo)
    return memo[m][n]
    
if __name__ == "__main__":
    #print(uniquePaths(23, 12))
    print(uniquePaths(3, 2))
    #print(uniquePaths(1, 1))
