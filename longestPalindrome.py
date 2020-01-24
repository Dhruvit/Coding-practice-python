# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:49:19 2020

@author: dpatel
"""

def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        
        table = [[0 for i in range(len(s))] for i in range(len(s))]
        start = 0
        maxlength = 1
         
        for i in range(0, len(s)): # only one character is by default palindrome
            table[i][i] = 1
            
        for i in range(0, len(s)-1): # for length of 2
            if s[i] == s[i+1]:
                table[i][i+1] = 1
                start = i
                maxlength = 2
                
        for k in range(3, len(s)): #for length more than 3
            for i in range(0, len(s)-k+1):
                j = i + k - 1
                
                if table[i+1][j-1] and s[i] == s[j]:
                    table[i][j] = 1
                    
                    if k > maxlength:
                        maxlength = k
                        start = i
                   
        return s[start: start+maxlength]
    
if __name__ == "__main__":
    
    #print(longestPalindrome('cbbd'))
    print(longestPalindrome('babad'))
                
