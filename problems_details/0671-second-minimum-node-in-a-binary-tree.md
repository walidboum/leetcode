# 671. Second Minimum Node In a Binary Tree

**Source:** [https://leetcode.ca/all/671.html](https://leetcode.ca/all/671.html)

**Companies:** Amazon, LinkedIn, Microsoft, Uber

## Description

Given a non-empty special binary tree consisting of nodes with the non-negative value, where
        each node in this tree has exactly

two

or

zero

sub-node. If the
        node has two sub-nodes, then this node's value is the smaller value among its two
        sub-nodes. More formally, the property

root.val = min(root.left.val,
            root.right.val)

always holds.

Given such a binary tree, you need to output the

second minimum

value in the set made
        of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input:

2
   / \
  2   5
     / \
    5   7

Output:

5

Explanation:

The smallest value is 2, the second smallest value is 5.

Example 2:

Input:

2
   / \
  2   2

Output:

-1

Explanation:

The smallest value is 2, but there isn't any second smallest value.

Difficulty:

Easy

Lock:

Normal

Company:

Amazon

LinkedIn

Microsoft

Uber

Problem Solution

671-Second-Minimum-Node-In-a-Binary-Tree

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

