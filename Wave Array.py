'''
Link: https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1/?category[]=Arrays&category[]=Strings&category[]=Arrays&category[]=Strings&company[]=Google&company[]=Samsung&company[]=Google&company[]=Samsung&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&page=1&query=category[]Arrayscategory[]Stringscompany[]Googlecompany[]Samsungdifficulty[]-2difficulty[]-1difficulty[]0page1company[]Googlecompany[]Samsungcategory[]Arrayscategory[]Strings
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it
In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
If there are multiple solutions, find the lexicographically smallest one.
'''
#User function Template for python3


class Solution:
    #Complete this function
    #Function to sort the array into a wave-like array.
    def convertToWave(self,arr,N):
        i,j=0,1
        while(j<N):
            arr[i],arr[j]=arr[j],arr[i]
            j+=2
            i+=2
        return arr
            
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().split()]
        ob=Solution()
        ob.convertToWave(A,N)
        for i in A:
            print(i,end=" ")
        
        
        print()
        
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
