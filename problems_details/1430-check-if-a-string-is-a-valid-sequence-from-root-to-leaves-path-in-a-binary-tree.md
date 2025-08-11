# 1430. Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

**Source:** [https://leetcode.ca/all/1430.html](https://leetcode.ca/all/1430.html)

**Companies:** 23&me

## Description

Given a binary tree where each path going from the root to any leaf form a

valid
            sequence

, check if a given string is a

valid sequence

in
            such binary tree.

We get the given string from the concatenation of an array of integers

arr

and the concatenation of all values of the nodes along a path
                results in a

sequence

in the given binary tree.

Example 1:

Input:

root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]

Output:

true

Explanation:

The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
Other valid sequences are:
0 -> 1 -> 1 -> 0
0 -> 0 -> 0

Example 2:

Input:

root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]

Output:

false

Explanation:

The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.

Example 3:

Input:

root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]

Output:

false

Explanation:

The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.

Constraints:

1 <= arr.length <= 5000

0 <= arr[i] <= 9

Each node's value is between [0 - 9].

Difficulty:

Medium

Lock:

Prime

Company:

23&me

Problem Solution

1430-Check-If-a-String-Is-a-Valid-Sequence-from-Root-to-Leaves-Path-in-a-Binary-Tree

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

