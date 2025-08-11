# 1091. Shortest Path in Binary Matrix

**Source:** [https://leetcode.ca/all/1091.html](https://leetcode.ca/all/1091.html)

**Companies:** Amazon, Facebook, Google, Uber

## Description

In an N by N square grid, each cell is either empty (0) or blocked (1).

A

clear path from top-left to bottom-right

has length

k

if and only if it is composed of cells

C_1, C_2, ..., C_k

such that:

Adjacent cells

C_i

and

C_{i+1}

are connected 8-directionally
            (ie., they are different and share an edge or corner)

C_1

is at location

(0, 0)

(ie. has value

grid[0][0]

)

C_k

is at location

(N-1, N-1)

(ie. has value

grid[N-1][N-1]

)

If

C_i

is located at

(r, c)

, then

grid[r][c]

is empty (ie.

grid[r][c] == 0

).

Return the length of the shortest such clear path from top-left to bottom-right.  If
        such a path does not exist, return -1.

Example 1:

Input:

[[0,1],[1,0]]

Output:

2

Example 2:

Input:

[[0,0,0],[1,1,0],[1,1,0]]

Output:

4

Difficulty:

Medium

Lock:

Normal

Company:

Amazon

Facebook

Google

Uber

Problem Solution

1091-Shortest-Path-in-Binary-Matrix

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

