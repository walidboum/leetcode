# 1666. Change the Root of a Binary Tree

**Source:** [https://leetcode.ca/all/1666.html](https://leetcode.ca/all/1666.html)

**Companies:** Google

## Description

Given the

root

of a binary tree and a

leaf

node, reroot
            the tree so that the

leaf

is the new root.

You can reroot the tree with the following steps for each node

cur

on
                the path

starting from the

leaf

up to the

root

âââ

excluding the root

:

If

cur

has a left child, then that child becomes

cur

's
                    right child. Note that it is guaranteed that

cur

will have at most
                    one child.

cur

's original parent becomes

cur

's left child.

Return

the new root

of the rerooted tree.

Note:

Ensure that your solution sets the

Node.parent

pointers correctly after rerooting or you will receive "Wrong Answer".

Example 1:

Input:

root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 7

Output:

[7,2,null,5,4,3,6,null,null,null,1,null,null,0,8]

Example 2:

Input:

root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 0

Output:

[0,1,null,3,8,5,null,null,null,6,2,null,null,7,4]

Constraints:

The number of nodes in the tree is in the range

[2, 100]

.

-10

9

<= Node.val <= 10

9

All

Node.val

are

unique

.

leaf

exist in the tree.

Difficulty:

Medium

Lock:

Prime

Company:

Google

Problem Solution

1666-Change-the-Root-of-a-Binary-Tree

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

