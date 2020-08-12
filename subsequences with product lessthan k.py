"""
Given a non negative array A with N integers, The task is given as follows:

find the number of subsequences having product smaller than K.

Input:
First line indicates integer N
Second line contains elements of array A
Third line contains the integer k

Output:
Print the count of subsequences with product less than k

Examples:

Input :
4
1 2 3 4
10
Output :
11 
The subsequences are {1}, {2}, {3}, {4}, 
{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, 
{1, 2, 3}, {1, 2, 4}

Input  : 
4
4 8 7 2 
50
Output :
9

Input:
5
1 2 3 4 5
6
Output:
11

Input:
5
6 4 8 3 5
2
Output:
0

Input:
3
1 2 3
1
Output:
1

"""

def proCount(arr, k): 
    n = len(arr) 
    dp = [[0 for i in range(n + 1)] 
             for j in range(k + 1)] 
    for i in range(1, k + 1): 
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j - 1] 
            if arr[j - 1] <= i and arr[j - 1] > 0:
                dp[i][j] += dp[i // arr[j - 1]][j - 1] + 1
    return dp[k][n]
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
print(proCount(arr,k))
