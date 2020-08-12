"""
Given a string S of length N consisting of lower-case English albhabets and an integer ‘l’,

The task is to find the number of distinct sub-strings of length ‘l’ of the given string.

Input:
First line indicates string S
Second line indicates integer l

Output:
Print the count of distinct sub strings
Examples:

Input :
abcbab
2
Output : 
4
All distinct sub-strings of length 2
will be {“ab”, “bc”, “cb”, “ba”}
Thus, answer equals 4.

Input :
ababa
2
Output : 
2

Input:
abcdab
3
Output:
4

Input:
aaaa
2
Output:
1

Input:
abcabc
2
Output:
3

"""
x = 26
mod = 3001
def Cntstr(s, l) :
    hash = 0
    for i in range(l) : 
        hash = (hash * x + (ord(s[i]) - 97)) % mod 
    pow_l = 1 
    for i in range(l-1) :  
        pow_l = (pow_l * x) % mod  
    result = set() 
    result.add(hash) 
    for i in range(l,len(s)) : 
        hash = ((hash - pow_l * (ord(s[i - l]) - 97)+ 2 * mod) * x + (ord(s[i]) - 97)) % mod 
          
        result.add(hash)  
    print(len(result))
s=input()
l=int(input())
Cntstr(s,l)
