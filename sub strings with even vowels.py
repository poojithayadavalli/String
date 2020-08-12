"""
Kunal is fond of vowels and he came across a task as follows:

Given a string S of length N, the task is to find the number of non-empty substrings having even number of vowels.

Input:
First line contains integer N
Second line contains the string S

Print count of substrings with even number of vowels.

Examples:

Input:
5
abcde
Output: 
7
Explanation: 
All possible substrings with even number of vowels are:
({abcde} ,2),({b}, 0),({bc} ,0),({bcd},0),({c},0),({cd},0),({d},0).

Input:
4
geeks
Ouput: 
6

Input:
5
hello
Output:
6

Input:
7
avengar
Output:
12

Input:
3
bcd
Output:
6
"""
def isVowel(c):
    if (c == 'a'or c == 'e'or c == 'i'or c == 'o'or c == 'u'): 
        return True
    return False

def countst(s, n):
    result = 0
  
    for i in range(n): 
        count = 0
        for j in range(i, n):
            if (isVowel(s[j])):
                count += 1 
            if (count % 2 == 0):
                result += 1
    print(result)
n=int(input())
s=input()
countst(s,n)
