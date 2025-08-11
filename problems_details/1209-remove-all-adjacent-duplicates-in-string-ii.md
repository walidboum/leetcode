# 1209. Remove All Adjacent Duplicates in String II

**Source:** [https://leetcode.ca/all/1209.html](https://leetcode.ca/all/1209.html)

**Companies:** Bloomberg, FactSet, Google, VMware

## Description

Given a string

s

, a

k

duplicate removal

consists
        of choosing

k

adjacent and equal letters from

s

and
        removing them causing the left and the right side of the deleted substring to
        concatenate together.

We repeatedly make

k

duplicate removals on

s

until we no longer
        can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

Example 1:

Input:

s = "abcd", k = 2

Output:

"abcd"

Explanation:

There's nothing to delete.

Example 2:

Input:

s = "deeedbbcccbdaa", k = 3

Output:

"aa"

Explanation:

First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:

Input:

s = "pbbcggttciiippooaais", k = 2

Output:

"ps"

Constraints:

1 <= s.length <= 10^5

2 <= k <= 10^4

s

only contains lower case English letters.

Difficulty:

Medium

Lock:

Normal

Company:

Bloomberg

FactSet

Google

VMware

Problem Solution

1209-Remove-All-Adjacent-Duplicates-in-String-II

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

