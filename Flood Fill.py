# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:00:38 2020

@author: dpatel
"""

#we can solve through recursive neighbour coloring
def floodFill(image, sr, sc, newColor):   
    
    if image[sr][sc] == newColor:
        return image
    
    #do coloring for connected neighbour
    doFloodFill(image, sr, sc, image[sr][sc], newColor) #left
    
    return image

def doFloodFill(image, sr, sc, curColor, newColor):
    if(sr<0 or sr>len(image)-1 or sc<0 or sc>len(image[sr])-1 or image[sr][sc] == newColor or image[sr][sc] != curColor):
        return image
    else:
        image[sr][sc] = newColor
    
    doFloodFill(image, sr-1, sc, curColor, newColor) #left
    doFloodFill(image, sr+1, sc, curColor, newColor) #right
    doFloodFill(image, sr, sc-1, curColor, newColor) #up
    doFloodFill(image, sr, sc+1, curColor, newColor) #down
    
    return image
    
if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    print(floodFill(image, sr, sc, newColor))