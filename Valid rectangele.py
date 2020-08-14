"""
Given four integers A, B, C and D which represents the four angles of a Quadrilateral in degrees. 

The task is to check whether the given quadrilateral is valid or not.

Input:
Input contains 4 angles of quadrilateral

Output:
Print whether it is valid quadrilateral or not

Examples:

Input:
80 70 100 110
Output: Valid

Input: 
70 80 130 60
Output: Invalid

"""
def Valid(a, b, c, d): 
    if (a + b + c + d == 360): 
        return True
      
    return False
a,b,c,d=map(int,input().split())
print("Valid" if Valid(a,b,c,d) else "Invalid")
