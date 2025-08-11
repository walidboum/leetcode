# 1130. Minimum Cost Tree From Leaf Values

**Source:** [https://leetcode.ca/all/1130.html](https://leetcode.ca/all/1130.html)

**Companies:** Amazon, Mathworks

## Description

Given an array

arr

of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;

The values of

arr

correspond to the values of
            each

leaf

in an in-order traversal of the tree.

(Recall
                that a node is a leaf if and only if it has 0 children.)

The value of each non-leaf node is equal to the product of the largest leaf value
            in its left and right subtree respectively.

Among all possible binary trees considered, return the smallest possible sum of the
        values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit
        integer.

Example 1:

Input:

arr = [6,2,4]

Output:

32

Explanation:

There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4

Constraints:

2 <= arr.length <= 40

1 <= arr[i] <= 15

It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less
            than

2^31

).

Difficulty:

Medium

Lock:

Normal

Company:

Amazon

Mathworks

Problem Solution

1130-Minimum-Cost-Tree-From-Leaf-Values

All Problems:

Link to All Problems

All contents and pictures on this website come from the Internet and are updated regularly every week. They are for personal study and research only, and should not be used for commercial purposes. Thank you for your cooperation.

