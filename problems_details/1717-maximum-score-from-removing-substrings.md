# 1717. Maximum Score From Removing Substrings

**Source:** [https://leetcode.ca/all/1717.html](https://leetcode.ca/all/1717.html)

**Companies:** Google

## Description

You are given a string

s

and two integers

x

and

y

. You can perform two types of operations any number of times.

Remove substring

"ab"

and gain

x

points.

For example, when removing

"ab"

from

"c

ab

xbae"

it becomes

"cxbae"

.

Remove substring

"ba"

and gain

y

points.

For example, when removing

"ba"

from

"cabx

ba

e"

it becomes

"cabxe"

.

Return

the maximum points you can gain after applying the above operations
                on

s

.

Example 1:

Input:

s = "cdbcbbaaabab", x = 4, y = 5

Output:

19

Explanation:

- Remove the "ba" underlined in "cdbcbbaaa

ba

b". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaa

ab

". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcb

ba

a". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbc

ba

". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

Example 2:

Input:

s = "aabbaaxybbaabb", x = 5, y = 4

Output:

20

Constraints:

1 <= s.length <= 10

5

1 <= x, y <= 10

4

s

consists of lowercase English letters.

Difficulty:

Medium

Lock:

Normal

Company:

Google

Problem Solution

-1717-Maximum-Score-From-Removing-Substrings

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly
        every week. They are for personal study and research only, and should not be used for
        commercial purposes. Thank you for your cooperation.

