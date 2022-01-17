'''
Link: https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1#
Given an unsorted array arr[] of size N having both negative and positive integers. 
The task is place all negative element at the end of array without changing the order of positive element and negative element.
'''
#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        pos=[]
        neg=[]
        for i in range(0,n):
            if(arr[i]>=0):
                pos.append(arr[i])
    
            else:
                neg.append(arr[i])
        x=pos+neg
        for i in range(0,n):
            arr[i]=x[i]
        return arr
            
        
                
            
                
            
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
