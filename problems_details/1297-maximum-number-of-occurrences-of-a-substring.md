# 1297. Maximum Number of Occurrences of a Substring

**Source:** [https://leetcode.ca/all/1297.html](https://leetcode.ca/all/1297.html)

**Companies:** Roblox

## Description

Given a string

s

, return the maximum number of ocurrences of

any

substring under the following rules:

The number of unique characters in the substring must be less than or equal to

maxLetters

.

The substring size must be between

minSize

and

maxSize

inclusive.

Example 1:

Input:

s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4

Output:

2

Explanation:

Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

Example 2:

Input:

s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3

Output:

2

Explanation:

Substring "aaa" occur 2 times in the string. It can overlap.

Example 3:

Input:

s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3

Output:

3

Example 4:

Input:

s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3

Output:

0

Constraints:

1 <= s.length <= 10^5

1 <= maxLetters <= 26

1 <= minSize <= maxSize <= min(26, s.length)

s

only contains lowercase English letters.

Difficulty:

Medium

Lock:

Normal

Company:

Roblox

Problem Solution

1297-Maximum-Number-of-Occurrences-of-a-Substring

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

