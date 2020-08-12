"""
Given a binary string str of length N, the task is to find the count of subsequences of str which are divisible by 2. Leading zeros in a sub-sequence is allowed.

Input:
First line contains integer N
Second line contains binary string

Output:
Print the count of subsequences divisible by 2

Examples:

Input:
3
101
Output:
2
“0” and “10” are the only subsequences
which are divisible by 2.

Input:
5
10010
Output: 
22

Input:

"""
def countSubSeq(strr, lenn):
    ans = 0
    mul = 1 
    for i in range(lenn):
        if (strr[i] == '0'): 
            ans += mul
        mul *= 2
    return ans
n=int(input())
s=input()
print(countSubSeq(s,n))
