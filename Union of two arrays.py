'''
Link:https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1
Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.
Union of the two arrays can be defined as the set containing distinct elements from both the arrays.
If there are repetitions, then only one occurrence of element should be printed in the union.
'''

#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    
    def doUnion(self,a,n,b,m):
        dic={}
        for i in range(n):
            if a[i] in dic:
                dic[a[i]]+=1
            else:
                dic[a[i]]=1
        for j in range(m):
            if b[j] in dic:
                dic[b[j]]+=1
            else:
                dic[b[j]]=1
        count=0
        for i in dic:
            count+=1
        return count
        
            
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends
