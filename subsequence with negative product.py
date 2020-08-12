"""
Given an array arr[] of N integers, the task is to find the count of all the subsequences of the array that have a negative products.

Input:
First line contains integer N
Second line contains elements of array

Output:
Print the count of subsequences with negative product

Examples:

Input:
3
1 -5 -6
Output: 
4
Explanation
{-5}, {-6}, {1, -5} and {1, -6} are the only possible subsequences

Input:
3
2 3 1
Output:
0
Explanation
There is no such possible subsequence with negative product

Input:
5
1 -1 -5 7 8
Output:
16

Input:
4
-1 -2 -3 -4
Output:
8

Input:
2
-1 2
Output:
2

"""
import math   
def cntseq(arr, n):
    pos_count = 0 
    neg_count = 0
  
    for i in range (n):
        if (arr[i] > 0) :  
            pos_count += 1
        if (arr[i] < 0):  
            neg_count += 1 
    result = int(math.pow(2, pos_count))
    
    if (neg_count > 0):  
        result *= int(math.pow(2, neg_count - 1))  
    else: 
        result = 0
  
    return result
n=int(input())
arr=list(map(int,input().split()))
print(cntseq(arr,n))
