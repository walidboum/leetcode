# 1794. Count Pairs of Equal Substrings With Minimum Difference

**Source:** [https://leetcode.ca/all/1794.html](https://leetcode.ca/all/1794.html)

**Companies:** Google

## Description

You are given two strings

firstString

and

secondString

that are

0-indexed

and consist only of lowercase English letters. Count the number of index quadruples

(i,j,a,b)

that satisfy the following conditions:

0 <= i <= j < firstString.length

0 <= a <= b < secondString.length

The substring of

firstString

that starts at the

i

th

character and ends at the

j

th

character (inclusive) is

equal

to the substring of

secondString

that starts at the

a

th

character and ends at the

b

th

character (inclusive).

j - a

is the

minimum

possible value among all quadruples that satisfy the previous conditions.

Return

the

number

of such quadruples

.

Example 1:

Input:

firstString = "abcd", secondString = "bccda"

Output:

1

Explanation:

The quadruple (0,0,4,4) is the only one that satisfies all the conditions and minimizes j - a.

Example 2:

Input:

firstString = "ab", secondString = "cd"

Output:

0

Explanation:

There are no quadruples satisfying all the conditions.

Constraints:

1 <= firstString.length, secondString.length <= 2 * 10

5

Both strings consist only of lowercase English letters.

Difficulty:

Medium

Lock:

Prime

Company:

Google

Problem Solution

Leetcode Solutions Java Python C++

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

