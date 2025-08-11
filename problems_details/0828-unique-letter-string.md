# 828. Unique Letter String

**Source:** [https://leetcode.ca/all/828.html](https://leetcode.ca/all/828.html)

**Companies:** ForUsAll, Twitch

## Description

A character is unique in string

S

if it occurs exactly once in it.

For example, in string

S = "LETTER"

, the only unique characters are

"L"

and

"R"

.

Let's define

UNIQ(S)

as the number of unique characters in string

S

.

For example,

UNIQ("LETTER") =  2

.

Given a string

S

with only uppercases, calculate the sum of

UNIQ(substring)

over all non-empty substrings of

S

.

If there are two or more equal substrings at different positions in

S

, we
        consider them different.

Since the answer can be very large, return the answer modulo

10 ^ 9 +
        7

.

Example 1:

Input:

"ABC"

Output:

10

Explanation:

All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:

Input:

"ABA"

Output:

8

Explanation:

The same as example 1, except uni("ABA") = 1.

Note:

0 <= S.length <= 10000

.

Difficulty:

Hard

Lock:

Normal

Company:

ForUsAll

Twitch

Problem Solution

828-Count-Unique-Characters-of-All-Substrings-of-a-Given-String

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

