"""
International Mobile Equipment Identity (IMEI) is a number, usually unique, to identify mobile phones, as well as some satellite phones.

The task is to validate the IMEI number.

The IMEI is validated in following steps:

1.Starting from the rightmost digit, double the value of every second digit (e.g., 7 becomes 14).

2.If doubling of a number results in a two digits number i.e greater than 9(e.g., 7 × 2 = 14), then add the digits of the product 
(e.g., 14: 1 + 4 = 5), to get a single digit number.

3.Now take the sum of all the digits.

4.Check if the sum is divisible by 10 i.e.(total modulo 10 is equal to 0) then the IMEI number is valid; else it is not valid.

Example:
Input:
490154203237518
Output:
Valid
Explanation:
IMEI:  4 9  0 1 5  4 2 0 3 2 3 7  5 1 8
Double:4 18 0 2 10 8 2 0 3 4 3 14 5 2 8
alternate
Sum  :4+9+0+2+1+8+2+0+3+4+3+5+5+2+8=60
Since 60 is divisible by 10 It is a valid IMEI number.

Input:
695154204233518
Output:
Invalid

Input:
596154604273518
output:
Invalid

Input:
870154203237518
Output:
Valid

Input:
597154203237538
Output:
Invalid

"""
def sumDig( n ): 
    a = 0
    while n > 0: 
        a = a + n % 10
        n = int(n / 10) 
  
    return a 
def isValidIMEI(n):
    s = str(n) 
    l = len(s) 
    if l != 15: 
        return False
  
    d = 0
    sum = 0
    for i in range(15, 0, -1): 
        d = (int)(n % 10) 
        if i % 2 == 0:
            d = 2 * d
        sum = sum + sumDig(d) 
        n = n / 10
    return (sum % 10 == 0)
x=int(input())
if isValidIMEI(x):
    print("Valid")
else:
    print("Invalid")
