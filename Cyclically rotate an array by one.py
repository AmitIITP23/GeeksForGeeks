'''
Link: https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1#
Given an array, rotate the array by one position in clock-wise direction.
'''

#User function Template for python3

def rotate( arr, n):
    temp=arr[n-1]
    for i in range(n-1,0,-1):
        if(i>0):
            arr[i]=arr[i-1]
    arr[0]=temp
    return arr
        
        
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
