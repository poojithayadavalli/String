"""
Given a string str, the task is to check if the string is a valid identifier or not. In order to qualify as a valid identifier, the string must satisfy the following conditions:

It must start with either underscore(_) or any of the characters from the ranges [‘a’, ‘z’] and [‘A’, ‘Z’].
There must not be any white space in the string.
And, all the subsequent characters after the first character must not consist of any special characters like $, #, % etc.
Examples:

Input: str= “_geeks123”
Output: Valid

Input: str = “123geeks_”
Output: Invalid

"""
