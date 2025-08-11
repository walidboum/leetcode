# 1698. Number of Distinct Substrings in a String

**Source:** [https://leetcode.ca/all/1698.html](https://leetcode.ca/all/1698.html)

**Companies:** Dunzo, Intuit

## Description

Given a string

s

, return

the number of

distinct

substrings of

s

.

A

substring

of a string is obtained by deleting any number of
                characters (possibly zero) from the front of the string and any number (possibly
                zero) from the back of the string.

Example 1:

Input:

s = "aabbaba"

Output:

21

Explanation:

The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]

Example 2:

Input:

s = "abcdefg"

Output:

28

Constraints:

1 <= s.length <= 500

s

consists of lowercase English letters.

Follow up:

Can you solve this problem in

O(n)

time
            complexity?

Hints:

Hint 1

Calculate the prefix hashing array for s.

Hint 2

Use the prefix hashing array to calculate the hashing value of each substring.

Hint 3

Compare the hashing values to determine the unique substrings.

Hint 4

There could be collisions if you use hashing, what about double hashing.

Difficulty:

Medium

Lock:

Prime

Company:

Dunzo

Intuit

Problem Solution

1698-Number-of-Distinct-Substrings-in-a-String

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

