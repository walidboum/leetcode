# 761. Special Binary String

**Source:** [https://leetcode.ca/all/761.html](https://leetcode.ca/all/761.html)

**Companies:** Citrix, Coursera, Quip (Salesforce), Visa

## Description

Special

binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.

Every prefix of the binary string has at least as many 1's as 0's.

Given a special string

S

, a

move

consists of choosing two consecutive,
    non-empty, special substrings of

S

, and swapping them.

(Two strings are
    consecutive if the last character of the first string is exactly one index before the first
    character of the second string.)

At the end of any number of moves, what is the lexicographically largest resulting string
        possible?

Example 1:

Input:

S = "11011000"

Output:

"11100100"

Explanation:

The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.

Note:

S

has length at most

50

.

S

is guaranteed to be a

special

binary string as defined above.

Difficulty:

Hard

Lock:

Normal

Company:

Citrix

Coursera

Quip (Salesforce)

Visa

Problem Solution

761-Special-Binary-String

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

