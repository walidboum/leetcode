# 899. Orderly Queue

**Source:** [https://leetcode.ca/all/899.html](https://leetcode.ca/all/899.html)

**Companies:** Amazon

## Description

A string

S

of lowercase letters is given.  Then, we may make any number of

moves

.

In each move, we choose one of the first

K

letters (starting from the
        left), remove it, and place it at the end of the string.

Return the lexicographically smallest string we could have after any number of moves.

Example 1:

Input:

S =

"cba"

, K =

1

Output:

"acb"

Explanation:

In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".

Example 2:

Input:

S =

"baaca"

, K =

3

Output:

"aaabc"

Explanation:

In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".

Note:

1 <= K <= S.length <= 1000

S

consists of lowercase letters only.

Difficulty:

Hard

Lock:

Normal

Company:

Amazon

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

