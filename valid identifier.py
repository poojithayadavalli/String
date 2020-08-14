"""
Given a string str of length N, the task is to check if the string is a valid identifier or not.

In order to qualify as a valid identifier, the string must satisfy the following conditions:

1.It must start with either underscore(_) or any of the characters from the ranges [‘a’, ‘z’] and [‘A’, ‘Z’].
2.There must not be any white space in the string.
3.And, all the subsequent characters after the first character must not consist of any special characters like $, #, % etc.

Input:
Firstline indicates the integer N.
Second line contains the string str

Output:
Print whether it is valid identifier or not

Examples:

Input:
geeks123
Output:
Valid

Input:
123geeks
Output:
Invalid

"""
def isValid(str1, n):
    if (((ord(str1[0]) >= ord('a') and
          ord(str1[0]) <= ord('z')) or 
         (ord(str1[0]) >= ord('A') and 
          ord(str1[1]) <= ord('Z')) or 
          ord(str1[0]) == ord('_')) == False): 
        return False
    for i in range(1, len(str1)): 
        if (((ord(str1[i]) >= ord('a') and 
              ord(str1[i]) <= ord('z')) or 
             (ord(str1[i]) >= ord('A') and 
              ord(str1[i]) <= ord('Z')) or 
             (ord(str1[i]) >= ord('0') and
              ord(str1[i]) <= ord('9')) or 
              ord(str1[i]) == ord('_')) == False): 
            return False 
    return True
n=int(input())
arr=input()
if isValid(arr,n):
    print("Valid")
else:
    print("Invalid")
