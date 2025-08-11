# 1593. Split a String Into the Max Number of Unique Substrings

**Source:** [https://leetcode.ca/all/1593.html](https://leetcode.ca/all/1593.html)

**Companies:** Google

## Description

Given a string

s

,

return

the maximum number
            of unique substrings that the given string can be split into

.

You can split string

s

into any list of

non-empty
                substrings

, where the concatenation of the substrings forms the original
                string. However, you must split the substrings such that all of them are

unique

.

A

substring

is a contiguous sequence of characters within a string.

Example 1:

Input:

s = "ababccc"

Output:

5

Explanation

: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:

Input:

s = "aba"

Output:

2

Explanation

: One way to split maximally is ['a', 'ba'].

Example 3:

Input:

s = "aa"

Output:

1

Explanation

: It is impossible to split the string any further.

Constraints:

1 <= s.length <= 16

s

contains only lower case English letters.

Difficulty:

Medium

Lock:

Normal

Company:

Google

Problem Solution

1593-Split-a-String-Into-the-Max-Number-of-Unique-Substrings

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

