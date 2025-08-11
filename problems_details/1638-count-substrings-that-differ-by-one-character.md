# 1638. Count Substrings That Differ by One Character

**Source:** [https://leetcode.ca/all/1638.html](https://leetcode.ca/all/1638.html)

**Companies:** Microsoft

## Description

Given two strings

s

and

t

, find the number of ways you can
            choose a non-empty substring of

s

and replace a

single
                character

by a different character such that the resulting substring is a
            substring of

t

. In other words, find the number of substrings in

s

that differ from some substring in

t

by

exactly

one character.

For example, the underlined substrings in

"

compute

r"

and

"

computa

tion"

only differ by the

'e'

/

'a'

, so this is a valid way.

Return

the number of substrings that satisfy the condition above.

A

substring

is a contiguous sequence of characters within a string.

Example 1:

Input:

s = "aba", t = "baba"

Output:

6

Explanation:

The following are the pairs of substrings from s and t that differ by exactly 1 character:
("

a

ba", "

b

aba")
("

a

ba", "ba

b

a")
("ab

a

", "

b

aba")
("ab

a

", "ba

b

a")
("a

b

a", "b

a

ba")
("a

b

a", "bab

a

")
The underlined portions are the substrings that are chosen from s and t.

ââ

Example 2:

Input:

s = "ab", t = "bb"

Output:

3

Explanation:

The following are the pairs of substrings from s and t that differ by 1 character:
("

a

b", "

b

b")
("

a

b", "b

b

")
("

ab

", "

bb

")
ââââThe underlined portions are the substrings that are chosen from s and t.

Example 3:

Input:

s = "a", t = "a"

Output:

0

Example 4:

Input:

s = "abe", t = "bbc"

Output:

10

Constraints:

1 <= s.length, t.length <= 100

s

and

t

consist of lowercase English letters only.

Difficulty:

Medium

Lock:

Normal

Company:

Microsoft

Problem Solution

1638-Count-Substrings-That-Differ-by-One-Character

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

