# 773. Sliding Puzzle

**Source:** [https://leetcode.ca/all/773.html](https://leetcode.ca/all/773.html)

**Companies:** Airbnb, Amazon, Google, Uber

## Description

On a 2x3

board

, there are 5 tiles represented by the integers 1 through 5, and
        an empty square represented by 0.

A move consists of choosing

0

and a 4-directionally adjacent number and
        swapping it.

The state of the board is

solved

if and only if the

board

is

[[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the
        board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input:

board = [[1,2,3],[4,0,5]]

Output:

1

Explanation:

Swap the 0 and the 5 in one move.

Input:

board = [[1,2,3],[5,4,0]]

Output:

-1

Explanation:

No number of moves will make the board solved.

Input:

board = [[4,1,2],[5,0,3]]

Output:

5

Explanation:

5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Input:

board = [[3,2,4],[1,5,0]]

Output:

14

Note:

board

will be a 2 x 3 array as described above.

board[i][j]

will be a permutation of

[0, 1, 2, 3, 4, 5]

.

Difficulty:

Hard

Lock:

Normal

Company:

Airbnb

Amazon

Google

Uber

Problem Solution

773-Sliding-Puzzle

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

