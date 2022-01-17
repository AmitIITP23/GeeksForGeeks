'''
Link: https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
'''
#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        countZero=0
        countOne=0
        countTwo=0
        i=0
        while(i<n):
            if(arr[i]==0):
                countZero+=1
            elif(arr[i]==1):
                countOne+=1
            else:
                countTwo+=1
            i+=1
        for i in range(n):
            if(countZero>0):
                arr[i]=0
                countZero-=1
            elif(countOne>0):
                arr[i]=1
                countOne-=1
            else:
                arr[i]=2
                countTwo-=1
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
