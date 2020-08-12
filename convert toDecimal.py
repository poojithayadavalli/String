"""
A string defining a valid number is given.Also two integers k and b are given.

The task is given as follows:

Output all the base conversions of substrings(in a sequence) of length ‘k’ from base ‘b’ to base 10.

Input:
First line indicates string with digits
Second line contains integer k and integer b.

Output:
print the decimal conversions

Examples:

Input :
12212
3 3
Output :
17 25 23

Explanation :
All the substrings of length 'k' are : 122, 221, 212.
Base conversion can be computed using the formula.

Input:
1234
3 2
Output:
11 18 

Input:
65743
3 1
Output:
18 16 14 

Input:
38659
4 3
Output:
176 294 

Input:
46532
2 3
Output:
18 23 18 11 

"""
import math as mt 
  
def decConv(str1, k, b):
    for i in range(0, len(str1) - k + 1): 
        sub = str1[i:k + i]
        Sum = 0
        counter = 0
        for i in range(len(sub) - 1, -1, -1): 
            Sum = (Sum + ((ord(sub[i]) - ord('0')) * pow(b, counter))) 
            counter += 1
        print(Sum,end = " ")
st=input()
k,b=map(int,input().split())
decConv(st,k,b)

