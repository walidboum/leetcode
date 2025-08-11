# 1684. Count the Number of Consistent Strings

**Source:** [https://leetcode.ca/all/1684.html](https://leetcode.ca/all/1684.html)

**Companies:** Robinhood

## Description

You are given a string

allowed

consisting of

distinct

characters and an array of strings

words

. A string is

consistent

if all characters in the string appear in the string

allowed

.

Return

the number of

consistent

strings in the array

words

.

Example 1:

Input:

allowed = "ab", words = ["ad","bd","aaab","baa","badab"]

Output:

2

Explanation:

Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:

Input:

allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]

Output:

7

Explanation:

All strings are consistent.

Example 3:

Input:

allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]

Output:

4

Explanation:

Strings "cc", "acd", "ac", and "d" are consistent.

Constraints:

1 <= words.length <= 10

4

1 <= allowed.length <=

26

1 <= words[i].length <= 10

The characters in

allowed

are

distinct

.

words[i]

and

allowed

contain only lowercase English
                    letters.

Difficulty:

Easy

Lock:

Normal

Company:

Robinhood

Problem Solution

1684-Count-the-Number-of-Consistent-Strings

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

