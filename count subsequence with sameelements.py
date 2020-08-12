"""
Given an array A[] consisting of N integers, the task is to find the total number of subsequence 

which contain only one distinct number repeated throughout the subsequence.

Input:
First line contains the integer N
Second line contains elements of array A

Output:
Print the count of subarrays that satisfies the condition. 

Examples: 
 
Input:
5
1 2 1 5 2
Output: 7 
Explanation: 
Subsequences {1}, {2}, {1}, {5}, {2}, {1, 1} and {2, 2} satisfy the required conditions.

Input:
6
5 4 4 5 10 4
Output: 11 
Explanation: 
Subsequences {5}, {4}, {4}, {5}, {10}, {4}, {5, 5}, {4, 4}, {4, 4}, {4, 4} and {4, 4, 4} satisfy the required conditions.

Input:
5
2 3 4 1 2
Output:
6

Input:
4
6 4 6 7
Output:
5

Input:
3
1 2 3
Output:
3
"""

import math
def CountSeq(A,N):
    result = 0
    mp = {}
    for i in range(N):
        if A[i] not in mp:
            mp[A[i]]=1
        else:
            mp[A[i]]+=1
  
    for j,it in mp.items():
        result = result + int(math.pow(2, it)-1)
    print(result)
N=int(input())
A=list(map(int,input().split()))
CountSeq(A,N)
