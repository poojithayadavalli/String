"""
Minimum number of adjacent swaps to convert a string into its given anagram
Last Updated: 10-07-2019
Given two strings s1 and s2, the task is to find the minimum number of steps required to convert s1 into s2. The only operation allowed is to swap adjacent elements in the first string. Every swap is counted as a single step.

Examples:

Input: s1 = “abcd”, s2 = “cdab”
Output: 4
Swap 2nd and 3rd element, abcd => acbd
Swap 1st and 2nd element, acbd => cabd
Swap 3rd and 4th element, cabd => cadb
Swap 2nd and 3rd element, cadb => cdab
Minimum 4 swaps are required.

Input: s1 = “abcfdegji”, s2 = “fjiacbdge”
Output:17
"""
