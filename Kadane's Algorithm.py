'''
Link: https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
Given an array Arr[] of N integers. 
Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
'''
#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        maxSoFar=0
        ans=-(10**9)+7
        for i in range(N):
            maxSoFar+=arr[i]
            if (maxSoFar > ans):
                ans=maxSoFar
            if(maxSoFar<0):
                maxSoFar=0
        return ans
        
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
