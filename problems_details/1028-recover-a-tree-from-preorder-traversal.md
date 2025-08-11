# 1028. Recover a Tree From Preorder Traversal

**Source:** [https://leetcode.ca/all/1028.html](https://leetcode.ca/all/1028.html)

**Companies:** Amazon, LinkedIn

## Description

We run a preorder depth first search on the

root

of a binary tree.

At each node in this traversal, we output

D

dashes (where

D

is the

depth

of this node), then we output the value of this node.

(If the
            depth of a node is

D

, the depth of its immediate child is

D+1

. 
            The depth of the root node is

0

.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output

S

of this traversal, recover the tree and return its

root

.

Example 1:

Input:

"1-2--3--4-5--6--7"

Output:

[1,2,5,3,4,6,7]

Example 2:

Input:

"1-2--3---4-5--6---7"

Output:

[1,2,5,3,null,6,null,4,null,7]

Difficulty:

Hard

Lock:

Normal

Company:

Amazon

LinkedIn

Problem Solution

1028-Recover-a-Tree-From-Preorder-Traversal

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

