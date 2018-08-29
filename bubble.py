# -*- Bubble Sort -*-
"""
Created on Thu Aug 16 22:20:38 2018

@author: SHLOK KASHYAP
"""

def Bubble(l):
    for j in range (0,len(l)-1):
        for i in range (0,len(l)-j-1):
            if l[i+1]<l[i]:
                l[i],l[i+1]=l[i+1],l[i]
    return(l)