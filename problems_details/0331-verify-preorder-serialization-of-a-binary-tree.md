# 331. Verify Preorder Serialization of a Binary Tree

**Source:** [https://leetcode.ca/all/331.html](https://leetcode.ca/all/331.html)

**Companies:** Google

## Description

One way to serialize a binary tree is to use pre-order traversal. When we encounter a
        non-null node, we record the node's value. If it is a null node, we record using a
        sentinel value such as

#

.

_9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

For example, the above binary tree can be serialized to the string

"9,3,4,#,#,1,#,#,2,#,6,#,#"

,
        where

#

represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal
        serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character

'#'

representing

null

pointer.

You may assume that the input format is always valid, for example it could never contain two
        consecutive commas such as

"1,,3"

.

Example 1:

Input:

"9,3,4,#,#,1,#,#,2,#,6,#,#"

Output:

true

Example 2:

Input:

"1,#"

Output:

false

Example 3:

Input:

"9,#,#,1"

Output:

false

Difficulty:

Medium

Lock:

Normal

Company:

Google

Problem Solution

331-Verify-Preorder-Serialization-of-a-Binary-Tree

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

