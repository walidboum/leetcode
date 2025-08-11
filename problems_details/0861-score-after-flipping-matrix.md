# 861. Score After Flipping Matrix

**Source:** [https://leetcode.ca/all/861.html](https://leetcode.ca/all/861.html)

**Companies:** IIT Bombay

## Description

We have a two dimensional matrix

A

where each value is

0

or

1

.

A move consists of choosing any row or column, and toggling each value in that row or column:
        changing all

0

s to

1

s, and all

1

s to

0

s.

After making any number of moves, every row of this matrix is interpreted as a binary number,
        and the score of the matrix is the sum of these numbers.

Return the highest possible score.

Example 1:

Input:

[[0,0,1,1],[1,0,1,0],[1,1,0,0]]

Output:

39

Explanation:

Toggled to

[[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Note:

1 <= A.length <= 20

1 <= A[0].length <= 20

A[i][j]

is

0

or

1

.

Difficulty:

Medium

Lock:

Normal

Company:

IIT Bombay

Problem Solution

861-Score-After-Flipping-Matrix

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

