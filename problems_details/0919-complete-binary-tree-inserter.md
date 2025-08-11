# 919. Complete Binary Tree Inserter

**Source:** [https://leetcode.ca/all/919.html](https://leetcode.ca/all/919.html)

**Companies:** Amazon, Google

## Description

A

complete

binary tree is a binary tree in which every level, except possibly the
        last, is completely filled, and all nodes are as far left as possible.

Write a data structure

CBTInserter

that is initialized with a complete
        binary tree and supports the following operations:

CBTInserter(TreeNode root)

initializes the data structure on a given tree with
            head node

root

;

CBTInserter.insert(int v)

will insert a

TreeNode

into the
            tree with value

node.val = v

so that the tree remains complete,

and returns the value of the parent of the inserted

TreeNode

;

CBTInserter.get_root()

will return the head node of the tree.

Example 1:

Input:

inputs =

["CBTInserter","insert","get_root"]

, inputs =

[[[1]],[2],[]]

Output:

[null,1,[1,2]]

Example 2:

Input:

inputs =

["CBTInserter","insert","insert","get_root"]

, inputs =

[[[1,2,3,4,5,6]],[7],[8],[]]

Output:

[null,3,4,[1,2,3,4,5,6,7,8]]

Difficulty:

Medium

Lock:

Normal

Company:

Amazon

Google

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

