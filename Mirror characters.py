"""
Given a string A and a number N, we need to mirror the characters from N-th position up to the length of the string in the alphabetical order.

In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.

Input:
First line contains integer N
Second line contains the string A

Output:
Print the string after performing mirror operation.
Examples:

Input : 
3
paradox
Output :
paizwlc
We mirror characters from position 3 to end.

Input :
4
pneumonia
Output : 
pnefnlmrz

"""
def compute(st, n): 
    reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba"
    l = len(st) 
    answer = "" 
    for i in range(0, n): 
        answer = answer + st[i] 
              
    for i in range(n, l): 
        answer = (answer + 
        reverseAlphabet[ord(st[i]) - ord('a')])
          
    return answer
n=int(input())
st=input()
print(compute(st,n-1))


