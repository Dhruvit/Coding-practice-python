# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:20:20 2020

@author: dpatel
"""

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    
    str_dict = {}
    
    for each_str in strs:    
        sort_str =  ''.join(sorted(each_str))
        if sort_str not in str_dict:
            str_dict[sort_str] = [each_str]
        else:
            str_dict[sort_str].append(each_str)
    result = []
    for k, v in str_dict.items():
        result.append(v)
        
    return result
if __name__ == "__main__":
    
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))