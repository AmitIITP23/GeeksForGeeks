'''
Link: https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1#
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
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

