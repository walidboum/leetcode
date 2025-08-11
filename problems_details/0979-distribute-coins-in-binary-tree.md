# 979. Distribute Coins in Binary Tree

**Source:** [https://leetcode.ca/all/979.html](https://leetcode.ca/all/979.html)

**Companies:** Amazon, Google, Microsoft, Uber

## Description

Given the

root

of a binary tree with

N

nodes, each

node

in the tree has

node.val

coins, and there are

N

coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another. 
        (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

Example 1:

Input:

[3,0,0]

Output:

2

Explanation:

From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:

Input:

[0,3,0]

Output:

3

Explanation:

From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.

Example 3:

Input:

[1,0,2]

Output:

2

Example 4:

Input:

[1,0,0,null,3]

Output:

4

Note:

1<= N <= 100

0 <= node.val <= N

Difficulty:

Medium

Lock:

Normal

Company:

Amazon

Google

Microsoft

Uber

Problem Solution

979-Distribute-Coins-in-Binary-Tree

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

