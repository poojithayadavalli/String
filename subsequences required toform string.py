"""
Given two strings A and B consisting of only lowercase letters, the task is to find the minimum number of subsequences required from A to form B.

Print -1 if subsequences of A cannot form B.

Input:
First line contains string A
Second line contains string B

Output:
print minimum subsequences of A required to form string B

Examples:

Input:
abbace
acebbaae
Output: 
3
Explanation:
Sub-sequences “ace”, “bba”, “ae” from string A used to form string B

Input:
abc
cbacbacba
Output:
7

Input:
abbad
badabab
Output:
3

Input:
abcd
htbdvb
Output:
-1

Input:
abbad
badab
Output:
2

"""

from bisect import bisect as upper_bound
def minSubsequences(A, B): 
    v = [[] for i in range(26)] 
    minIndex = -1
    cnt = 1
    j = 0
    flag = 0
  
    for i in range(len(A)):
        p = ord(A[i]) - 97
        v[p].append(i) 
  
    while (j < len(B)): 
        p = ord(B[j]) - 97
        k = upper_bound(v[p], minIndex)
        if (len(v[p]) == 0): 
            flag = 1
            break
        if (k != len(v[p])):
            minIndex = v[p][k] 
            j = j + 1
        else:
            cnt = cnt + 1
            minIndex = -1
    if (flag == 1): 
        return -1
    return cnt
A=input()
B=input()
print(minSubsequences(A,B))
