"""
Given a string S containing only uppercase English characters. The task is to find whether S is the same as its reflection in a mirror.

For example A's mirror image is A then it can be said as reflection.Print YES if S is same as its reflection else Print NO.

Input:
Input contains string S
Output:
Print whether it is reflection or no
Examples:

Input:
AMA
Output: 
YES
AMA is same as its reflection in the mirror.

Input:
ZXZ
Output: 
NO
"""
def isReflectionEqual(s):
    str1 = "AHIMOTUVWXY"
    n = len(s)
    for i in range(n):
        if s[i] not in str1: 
            return False
    rev = s[::-1]
    if (rev == s): 
        return True
    else: 
        return False
s=input()
print("Yes" if isReflectionEqual(s) else "No")
