# 1074. Number of Submatrices That Sum to Target

**Source:** [https://leetcode.ca/all/1074.html](https://leetcode.ca/all/1074.html)

**Companies:** Amazon, Google

## Description

Given a

matrix

, and a

target

, return the number of non-empty
        submatrices that sum to

target

.

A submatrix

x1, y1, x2, y2

is the set of all cells

matrix[x][y]

with

x1 <= x <= x2

and

y1 <= y <= y2

.

Two submatrices

(x1, y1, x2, y2)

and

(x1', y1', x2',
        y2')

are different if they have some coordinate that is different: for
        example, if

x1 != x1'

.

Example 1:

Input:

matrix =

[[0,1,0],[1,1,1],[0,1,0]]

, target =

0

Output:

4

Explanation:

The four 1x1 submatrices that only contain 0.

Example 2:

Input:

matrix =

[[1,-1],[-1,1]]

, target =

0

Output:

5

Explanation:

The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Difficulty:

Hard

Lock:

Normal

Company:

Amazon

Google

Problem Solution

1074-Number-of-Submatrices-That-Sum-to-Target

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

