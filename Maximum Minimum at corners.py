"""
Given N number of elements, find the minimum number of swaps required so that the maximum element

is at the beginning and the minimum element is at last with the condition that only swapping of adjacent elements is allowed.


Input:
First line contains integer N
Second line contains N integers

Output:
Print minimum number of swaps

Examples:

Input: 
7
3 1 5 3 5 5 2
Output:
6
Step 1: Swap 5 with 1 to make the array as {3, 5, 1, 3, 5, 5, 2}
Step 2: Swap 5 with 3 to make the array as {5, 3, 1, 3, 5, 5, 2}
Step 3: Swap 1 with 3 at its right to make the array as {5, 3, 3, 1, 5, 5, 2}
Step 4: Swap 1 with 5 at its right to make the array as {5, 3, 3, 5, 1, 5, 2}
Step 5: Swap 1 with 5 at its right to make the array as {5, 3, 3, 5, 5, 1, 2}
Step 6: Swap 1 with 2 at its right to make the array as {5, 3, 3, 5, 5, 2, 1}
After performing 6 swapping operations 5 is at the beginning and 1 at the end

Input:
4
5 6 1 3
Output: 
2

Input:
4
4 6 7 5
Output:
4

"""
def minSwaps(arr):
    n = len(arr) 
    maxx, minn, l, r = -1, arr[0], 0, 0
  
    for i in range(n):
        if arr[i] > maxx: 
            maxx = arr[i] 
            l = i
        if arr[i] <= minn: 
            minn = arr[i] 
            r = i 
              
    if r < l:  
        print(l + (n - r - 2)) 
    else: 
        print(l + (n - r - 1))
x=int(input())
n=list(map(int,input().split()))
minSwaps(n)
