"""
Surya is learning about anagrams and he found a task as follows:

Given two strings s1 and s2, the task is to find the minimum number of steps required to convert s1 into s2. 

The only operation allowed is to swap adjacent elements in the first string. Every swap is counted as a single step.

Input:
First line contains string s1
Second line contains string s2

Output:
Print the minimum steps required to convert s1 to s2

Examples:

Input:
abcd
cdab
Output:
4
Swap 2nd and 3rd element, abcd => acbd
Swap 1st and 2nd element, acbd => cabd
Swap 3rd and 4th element, cabd => cadb
Swap 2nd and 3rd element, cadb => cdab
Minimum 4 swaps are required.

Input:
abcfdegji
fjiacbdge
Output:
17

Input:
abcd
cdef
Output:
-1

Input:
abcde
deabc
Output:
6

Input:
hello
leloh
Output:
5

"""
def isAnagram(s1, s2) :  
    s1 = list(s1)
    s2 = list(s2) 
    s1 = s1.sort() 
    s2 = s2.sort() 
      
    if (s1 == s2) : 
        return 1 
          
    return 0
def countSteps(s1, s2, size) :  
    s1 = list(s1)
    s2 = list(s2)
      
    i = 0
    j = 0
    result = 0
    while (i < size) : 
        j = i
        while (s1[j] != s2[i]) : 
            j += 1 
        while (i < j) :
            temp = s1[j]
            s1[j] = s1[j - 1] 
            s1[j - 1] = temp 
            j -= 1
            result += 1      
        i += 1       
    return result
st1=input()
st2=input()
if isAnagram(st1,st2):
    print(countSteps(st1,st2,len(st1)))
else:
    print(-1)
